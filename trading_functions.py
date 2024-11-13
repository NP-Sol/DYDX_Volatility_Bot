from v4_client_py import IndexerClient
from v4_client_py.clients import CompositeClient
from v4_client_py.clients.constants import Network
from v4_client_py.clients.constants import ValidatorConfig, IndexerConfig
from v4_client_py.clients.constants import *
from v4_client_py.clients.dydx_subaccount import Subaccount
from v4_client_py.chain.aerial.wallet import LocalWallet
from v4_client_py.clients.helpers.chain_helpers import (
    ORDER_FLAGS_LONG_TERM,
    OrderType,
    OrderSide,
    OrderTimeInForce,
    OrderExecution,
)
from v4_proto.dydxprotocol.clob.order_pb2 import Order



import pandas as pd
import math
import time
import requests
import json
import os

from datetime import datetime

from trading_constants import *
from trading_strategy import *

## Time function
def timestamp_to_date(timestamp):
	return datetime.fromtimestamp(timestamp/1000).strftime('%Y-%m-%d-%H:%M:%S')

##Json functions
def add_to_json_file(file_name, new_row):
    if type(new_row) == dict:
        with open(file_name, 'a', encoding='utf-8') as file:
            file.write(json.dumps(new_row) + '\n')
    else:
        raise ValueError("Le fichier doit contenir une liste ou un dictionnaire")

def init_json(file): 
    dossier = os.path.dirname(file)
    if not os.path.exists(dossier) and dossier:
        os.makedirs(dossier)
        print(f"Dossier créé : {dossier}")
    
    if not os.path.exists(file):
        print(f"Le fichier JSON vide a été créé à l'emplacement : {file}")
    else:
        print(f"Le fichier existe déjà à l'emplacement : {file}")
    print("L'initialisation s'est passée correctement")

def read_last_line(file_path):
    with open(file_path, 'rb') as file:
        file.seek(0, 2)
        file_size = file.tell()

        buffer_size = 1024
        buffer = b''
        position = file_size
        while position > 0:
            seek_position = max(0, position - buffer_size)
            file.seek(seek_position)
            chunk = file.read(min(buffer_size, position))
            buffer = chunk + buffer
            position = seek_position

            if b'\n' in buffer:
                last_line = buffer.split(b'\n')[-2].decode().strip()
                return last_line

    return None

##dydx setup functions
def network_setup():
    NETWORK=Network(
        env='mainnet',
        validator_config=ValidatorConfig(
            grpc_endpoint=VALIDATOR_GRPC_ENDPOINT,
            aerial_url=AERIAL_CONFIG_URL,
            url_prefix=AERIAL_GRPC_OR_REST_PREFIX,
            chain_id=CHAIN_ID, 
            ssl_enabled=True
        ),
        indexer_config=IndexerConfig(
            rest_endpoint=INDEXER_REST_ENDPOINT,
            websocket_endpoint=INDEXER_WS_ENDPOINT,
        ),
        faucet_endpoint='',
    )
    return NETWORK

def comp_client_setup(NETWORK):
    NETWORK = network_setup()
    comp_client = CompositeClient(
    NETWORK,
    )
    return comp_client

def index_client_setup(NETWORK):
    NETWORK = network_setup()
    index_client = IndexerClient(
        config=NETWORK.indexer_config,
    )
    return index_client

def wallet_setup(PASSPHRASE):
    wallet = LocalWallet.from_mnemonic(PASSPHRASE, BECH32_PREFIX)
    return wallet

##Init functions
def init_get_trades(PATH_DATA,MARKET,index_client,address,subaccount_number):
    file_name = f'{PATH_DATA}/TRADES/TRADE_HISTORY_{MARKET}.json'
    fills_response = index_client.account.get_subaccount_fills(address, subaccount_number)
    fills = fills_response.data['fills']    

    fills.reverse()
    
    for trade in fills:
        add_to_json_file(file_name, trade)   

def init_get_funding_payment(PATH_DATA,MARKET,index_client,address,subaccount_number):
    market_funding_response = index_client.markets.get_perpetual_market_funding(MARKET)
    market_funding = market_funding_response.data['historicalFunding']

    position = get_position(MARKET,index_client,address,subaccount_number)
    file_name = f'{PATH_DATA}/FUNDING_PAYMENTS/FUNDING_PAYMENTS_{MARKET}.json'
    
    market_funding.reverse()
    for funding in market_funding:
        funding['payment']= -float(funding['rate'])*float(funding['price'])*position
        add_to_json_file(file_name,funding)

def init_get_pnl(PATH_DATA,index_client,address, subaccount_number):
    historical_pnl_response = index_client.account.get_subaccount_historical_pnls(address, subaccount_number)
    historical_pnl = historical_pnl_response.data['historicalPnl']

    file_name = f'{PATH_DATA}/PNL_HISTORY.json'

    pnl_data = historical_pnl.data['historicalPnl']
    pnl_data.reverse()

    for pnl in pnl_data:
        add_to_json_file(file_name, pnl)

def init_ptf(PATH_DATA,MARKET,PTF):

    directory = os.path.dirname(f'{PATH_DATA}/PORTFOLIO/{PTF}/')
    if not os.path.exists(directory):
        os.makedirs(directory)

    file_name = f'{PATH_DATA}/PORTFOLIO/{PTF}/PTF_{MARKET}.json'
    new_row = {'timestamp': int(time.time()),
                MARKET : 0,
                'USD' : 0,
                'EVENEMENT':'INIT',
                f'VAR -{MARKET}':0,
                'VAR - USD':0,
                'Value':0,
                'Shares':0,
                'Delta_shares':0,
                'ref': 'INIT'}
    
    with open(file_name, 'a', encoding='utf-8') as file:
        file.write(json.dumps(new_row) + '\n')


##Get datas functions 
def get_position(MARKET,index_client,address,subaccount_number):
    perpetual_positions_response = index_client.account.get_subaccount_perpetual_positions(address, subaccount_number)
    perpetual_positions = perpetual_positions_response.data['positions']
    position = [entry for entry in perpetual_positions if entry['market']==MARKET and entry['status']=='OPEN']
    pos = 0
    if len(position) >= 1:
        pos = float(position[0]['size'])
    return pos

def get_trades(PATH_DATA,MARKET,index_client,PTF,address,subaccount_number):
    file_name = f'{PATH_DATA}/TRADES/TRADE_HISTORY_{MARKET}.json'

    fills_response = index_client.account.get_subaccount_fills(address, subaccount_number)
    fills = fills_response.data['fills']

    data = pd.read_json(file_name,lines=True)
    
    maj = False
   
    orders_id = data['id'].tolist()
    fills.reverse()
    for trade in fills:
        if trade['id'] not in orders_id and trade['market'] == MARKET:
            add_to_json_file(file_name, trade)
            message = f"Exec - {trade['side']} - {trade['size']} - {trade['market']} - @ {trade['price']} $ opened at {trade['createdAt']}"
            send_message_to_discord(message,MARKET)
            maj_ptf_trade(PATH_DATA,trade,PTF)
            maj = True
    return maj

def get_funding_payment(PATH_DATA,MARKET,index_client,PTF,address,subaccount_number):
    market_funding_response = index_client.markets.get_perpetual_market_funding(MARKET)
    market_funding = market_funding_response.data['historicalFunding']
    
    position = get_position(MARKET,index_client,address,subaccount_number)
    file_name = f'{PATH_DATA}/FUNDING_PAYMENTS/FUNDING_PAYMENTS_{MARKET}.json'
    
    market_funding.reverse()
    
    data = pd.read_json(file_name,lines=True)
    effective_time = data['effectiveAt'].tolist()
    for funding in market_funding:
        if funding['effectiveAt'] not in effective_time:
            funding['payment']= -float(funding['rate'])*float(funding['price'])*position
            add_to_json_file(file_name, funding)
            message =f'Funding of {funding["payment"]} on {position} {MARKET}(rate {funding["rate"]} %)'
            send_message_to_discord(message,'funding')
            maj_ptf_funding(PATH_DATA,funding,PTF)

def get_pnl(PATH_DATA,index_client,address, subaccount_number):
    historical_pnl_response = index_client.account.get_subaccount_historical_pnls(address, subaccount_number)
    pnl_data = historical_pnl_response.data['historicalPnl']
    print(pnl_data)
    file_name = f'{PATH_DATA}/PNL_HISTORY.json'

    pnl_data.reverse()
    
    with open(file_name, 'r') as f:
        data = json.load(f)
        
    effective_time = [pnl['createdAt'] for pnl in data]
    
    for pnl in pnl_data:
        if pnl['createdAt'] not in effective_time:
            add_to_json_file(file_name, pnl)

## Accounting functions - portfolio updating

def maj_ptf_trade(PATH_DATA,trade,PTF):
    MARKET = trade['market']
    file_name = f'{PATH_DATA}/PORTFOLIO/{PTF}/PTF_{MARKET}.json'
    print("maj_trade")
    ptf = pd.read_json(file_name,lines=True)
    print("maj_trade_ok")
    LAST_ASSET_VALUE = ptf.iloc[-1].loc[MARKET]
    LAST_USD_VALUE = ptf.iloc[-1].loc['USD']
    LAST_VALUE = ptf.iloc[-1].loc['Value']

    if trade['side'] == 'BUY':
        VAR_ASSET = float(trade['size'])
        VAR_USD = -float(trade['size'])*float(trade['price'])-float(trade['fee'])
    
    elif trade['side'] == 'SELL':
        VAR_ASSET = -float(trade['size'])
        VAR_USD = float(trade['size'])*float(trade['price'])-float(trade['fee'])
    
    NEW_VALUE = float(LAST_USD_VALUE + VAR_USD +(LAST_ASSET_VALUE + VAR_ASSET)*float(trade['price']))

    NEW_SHARES = int(ptf.iloc[-1].loc['Shares'])

    new_row = {'timestamp': int(time.time()), 
                MARKET : LAST_ASSET_VALUE + VAR_ASSET,
                'USD' : LAST_USD_VALUE + VAR_USD,
                'EVENEMENT':trade['side'],
                f'VAR -{MARKET}':VAR_ASSET,
                'VAR - USD': VAR_USD,
                'Value':NEW_VALUE,
                'Shares':NEW_SHARES,
                'Delta_shares':0,
                'ref':trade['orderId']
              }
    
    add_to_json_file(file_name, new_row)
    
def maj_ptf_funding(PATH_DATA,funding,PTF):
    MARKET = funding['ticker']
    file_name = f'{PATH_DATA}/PORTFOLIO/{PTF}/PTF_{MARKET}.json'
    print("maj_funding")
    ptf = pd.read_json(file_name,lines=True)
    print("maj_funding_ok")
    LAST_ASSET_VALUE = float(ptf.iloc[-1].loc[MARKET])
    LAST_USD_VALUE = float(ptf.iloc[-1].loc['USD'])
    
    LAST_VALUE = float(ptf.iloc[-1].loc['Value'])
    NEW_VALUE = float(LAST_VALUE + float(funding['payment']))

    NEW_SHARES = int(ptf.iloc[-1].loc['Shares'])

    new_row = {'timestamp': int(time.time()), 
                MARKET : LAST_ASSET_VALUE,
                'USD' : LAST_USD_VALUE + float(funding['payment']),
                'EVENEMENT':'FUNDING',
                f'VAR -{MARKET}': 0,
                'VAR - USD': float(funding['payment']),
                'Value':NEW_VALUE,
                'Shares':NEW_SHARES,
                'Delta_shares':0,
                'ref':funding['effectiveAt']
              }
    with open(file_name, 'a', encoding='utf-8') as file:
        file.write(json.dumps(new_row) + '\n')
   
def maj_ptf_capitalization(PATH_DATA,MARKET,PTF, dollar_added, asset_added,ref):
    file_name = f'{PATH_DATA}/PORTFOLIO/{PTF}/PTF_{MARKET}.json'
    print("maj_ptf")
    ptf = pd.read_json(file_name,lines=True)
    print("maj_ptf_ok")
    LAST_ASSET_VALUE = ptf.iloc[-1].loc[MARKET]
    LAST_USD_VALUE = ptf.iloc[-1].loc['USD']
    LAST_SHARES = ptf.iloc[-1].loc['Shares']
    
    if LAST_ASSET_VALUE != 0:
        LAST_PRICE = LAST_USD_VALUE/LAST_ASSET_VALUE
    else :
        LAST_PRICE = 0

    NEW_ASSET = float(LAST_ASSET_VALUE + asset_added)
    NEW_USD = float(LAST_USD_VALUE + dollar_added)

    LAST_VALUE = round(LAST_USD_VALUE + LAST_ASSET_VALUE*LAST_PRICE,6)
    NEW_VALUE = round(NEW_USD + NEW_ASSET*LAST_PRICE,6)
    
    if LAST_SHARES == 0:
        NEW_SHARES = 10000
    else:
        NEW_SHARES = int(LAST_SHARES*NEW_VALUE/LAST_VALUE)

    DELTA_SHARES = int(NEW_SHARES - LAST_SHARES)
    
    new_row = {'timestamp': int(time.time()), 
            MARKET : NEW_ASSET,
            'USD' : NEW_USD,
            'EVENEMENT':'CAPITALIZATION',
            f'VAR -{MARKET}': asset_added,
            'VAR - USD': dollar_added,
            'Value':NEW_VALUE,
            'Shares':NEW_SHARES,
            'Delta_shares':DELTA_SHARES,
            'ref':ref
            }
    
    with open(file_name, 'a', encoding='utf-8') as file:
        file.write(json.dumps(new_row) + '\n')
    
    return [NEW_ASSET,NEW_USD,NEW_VALUE,NEW_SHARES,DELTA_SHARES]

##Dydx order functions
#MaJ
def make_trade(MARKET,PATH_DATA,index_client,comp_client,PTF,wallet):
    file_name =f'{PATH_DATA}/PORTFOLIO/{PTF}/PTF_{MARKET}.json'
    
    ptf = pd.read_json(file_name,lines=True)
    
    Q= ptf.iloc[-1].loc[MARKET]
    V = ptf.iloc[-1].loc['USD']
    X = ORDER_SIZE[MARKET]
    P = 1/float(TICK_SIZE[MARKET])
    P_plus_ = P_plus(Q, V, X, P)
    P_moins_ = P_moins(Q, V, X, P)
    
    orderbook = index_client.markets.get_perpetual_market_orderbook(MARKET)
    
    P_min_vente = float(orderbook.data['asks'][0]['price'])
    P_max_achat = float(orderbook.data['bids'][0]['price'])
    
    P_vente = max([P_plus_,P_min_vente])
    P_achat = min([P_moins_,P_max_achat])
    
    print(f'prix de vente : {P_vente}')
    print(f'prix d achat : {P_achat}')
    print(f'P+ = {P_plus_} et P- = {P_moins_}')

    buy_order_params = {
    'subaccount':Subaccount(wallet, 0),
    'market':MARKET,
    'type':OrderType.LIMIT,
    'side':OrderSide.BUY,
    'price':P_achat,
    'size':X,
    'client_id':int(datetime.now().timestamp()),
    'time_in_force':OrderTimeInForce.GTT,
    'good_til_block':get_current_block_height() +20000,
    'good_til_time_in_seconds':600000,#wip
    'execution':OrderExecution.DEFAULT,
    'post_only':False,
    'reduce_only':False,
    'trigger_price':None
    } 
    #print(buy_order_params)
    buy_order_response = comp_client.place_order(**buy_order_params)
    time.sleep(5)
    sell_order_params = {
    'subaccount':Subaccount(wallet, 0),
    'market':MARKET,
    'type':OrderType.LIMIT,
    'side':OrderSide.SELL,
    'price':P_vente,
    'size':X,
    'client_id':int(datetime.now().timestamp()),
    'time_in_force':OrderTimeInForce.GTT,
    'good_til_block':get_current_block_height() +20000,
    'good_til_time_in_seconds':600000,
    'execution':OrderExecution.DEFAULT,
    'post_only':False,
    'reduce_only':False,
    'trigger_price':None
    } 
    #print(sell_order_params)
    sell_order_response = comp_client.place_order(**sell_order_params)
    time.sleep(5)

def get_current_block_height():
    response = requests.get('https://indexer.dydx.trade/v4/height', headers={'Accept': 'application/json'})
    return int(response.json()['height'])

def convert_date_to_secs(good_til_block_time):
    # Convertir goodTilBlockTime en timestamp Unix
    dt = datetime.fromisoformat(good_til_block_time.replace('Z', '+00:00'))
    return int(dt.timestamp())

def delete_orders(MARKET,index_client,comp_client,address, subaccount_number,wallet):
    
    orders_response = index_client.account.get_subaccount_orders(address, subaccount_number,status="OPEN")
    orders = [order for order in orders_response.data if order['status']=='OPEN' and order['ticker']==MARKET]

    subaccount=Subaccount(wallet, 0)

    if orders:
        for order in orders:
            #print(order)
            clientid = int(order['clientId'])
            orderFlags =int(order['orderFlags'])
            good_til_block_time = convert_date_to_secs(order['goodTilBlockTime'])
            current_time = int(time.time())
            time_difference = good_til_block_time - current_time
            good_til_time_in_seconds = max(0, time_difference)
            current_block = get_current_block_height()
# order_response = index_client.account.get_order(order_id)
# order = order_response.data
# print(order)

            comp_client.cancel_order(
                subaccount,
                clientid,
                MARKET,
                orderFlags,
                good_til_time_in_seconds,
                current_block,
                )
            time.sleep(5)

def send_message_to_discord(message, MARKET):
    DISCORD_URL = CHANNELS_DISCORD[MARKET]
    requests.post(DISCORD_URL, json={"content": message})

def log_error(message, PATH_DATA,MARKET):
    moment = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    file_name=f'{PATH_DATA}/LOG/log{MARKET}.json'

    new_row = {"Time": moment, "message": message}

    with open(file_name, 'a', encoding='utf-8') as file:
        file.write(json.dumps(new_row) + '\n')