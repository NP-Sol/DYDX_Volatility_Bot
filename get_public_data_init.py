from v4_client_py import IndexerClient
from v4_client_py.clients.constants import Network
from v4_client_py.clients.constants import ValidatorConfig, IndexerConfig
from v4_client_py.clients.constants import *

import pandas as pd
import time
import json
import os

from trading_constants import PAIR_LIST, intervals
from trading_constants import VALIDATOR_GRPC_ENDPOINT,AERIAL_CONFIG_URL,AERIAL_GRPC_OR_REST_PREFIX,INDEXER_REST_ENDPOINT,INDEXER_WS_ENDPOINT,CHAIN_ID,ENV
from datetime import datetime

PATH = os.path.dirname(os.path.realpath(__file__))
PATH_DATA = f'{PATH}/TRADING_DATA'
if not os.path.exists(PATH_DATA):
    os.makedirs(PATH_DATA)

directory = os.path.dirname(f'{PATH_DATA}/CANDLES/')
if not os.path.exists(directory):
    os.makedirs(directory)

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

index_client = IndexerClient(
    config=NETWORK.indexer_config,
)

def timestamp_to_date(timestamp):
	return datetime.fromtimestamp(timestamp/1000).strftime('%Y-%m-%d-%H:%M:%S')

def add_to_json_file(file_name, new_row):
    if type(new_row) == dict:
        with open(file_name, 'a', encoding='utf-8') as file:
            file.write(json.dumps(new_row) + '\n')
    else:
        raise ValueError("Le fichier doit contenir un dictionnaire")

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

def is_first_date_more_recent(date1, date2):
    # Convertir les deux chaînes de caractères en objets datetime
    format_iso = "%Y-%m-%dT%H:%M:%S.%fZ"
    datetime1 = datetime.strptime(date1, format_iso)
    datetime2 = datetime.strptime(date2, format_iso)

    # Comparer les deux dates
    return datetime1 > datetime2

def init_get_funding_rate(MARKET):
    market_funding_response = index_client.markets.get_perpetual_market_funding(MARKET)
    market_funding = market_funding_response.data['historicalFunding']
    
    directory = os.path.dirname(f'{PATH_DATA}/FUNDING_RATE/')
    if not os.path.exists(directory):
        os.makedirs(directory)

    file_name = f'{directory}/FUNDING_HISTORY_{MARKET}.json'

    market_funding.reverse()
    for funding in market_funding:
        add_to_json_file(file_name, funding)
    
def get_funding_rate(MARKET):
    market_funding_response = index_client.markets.get_perpetual_market_funding(MARKET)
    market_funding = market_funding_response.data['historicalFunding']
    
    directory = os.path.dirname(f'{PATH_DATA}/FUNDING_RATE/')
    if not os.path.exists(directory):
        os.makedirs(directory)

    file_name = f'{directory}/FUNDING_HISTORY_{MARKET}.json'
    last_line =read_last_line(file_name)

    market_funding.reverse()
    for funding in market_funding:
        if is_first_date_more_recent(funding['effectiveAt'],last_line['effectiveAt']):
            add_to_json_file(file_name, funding)

def init_get_candles(MARKET,res):
    market_candles_response = index_client.markets.get_perpetual_market_candles(MARKET, res)
    candles = market_candles_response.data['candles']

    directory = os.path.dirname(f'{PATH_DATA}/CANDLES/{MARKET}/')
    if not os.path.exists(directory):
        os.makedirs(directory)

    file_name = f'{directory}/CANDLES_{res}.json'
    
    candles.reverse()
    
    for candle in candles:
        candle.pop("orderbookMidPriceOpen", None)
        candle.pop("orderbookMidPriceClose", None)
        add_to_json_file(file_name, candle)

def get_candles(MARKET,res):
    market_candles_response = index_client.markets.get_perpetual_market_candles(MARKET, res)
    candles = market_candles_response.data['candles']
    
    directory = os.path.dirname(f'{PATH_DATA}/CANDLES/{MARKET}/')
    if not os.path.exists(directory):
        os.makedirs(directory)

    file_name = f'{directory}/CANDLES_{res}.json'
    last_line =read_last_line(file_name)

    candles.reverse()

    for candle in candles:
        candle.pop("orderbookMidPriceOpen", None)
        candle.pop("orderbookMidPriceClose", None)
        if is_first_date_more_recent(candle['startedAt'],last_line['startedAt']):
            add_to_json_file(file_name, candle)

for pair in PAIR_LIST:
    for inter in intervals:
        init_get_candles(pair,inter)
    print(f'Ok - Candles {pair}-{timestamp_to_date(int(time.time())*1000)}')
    time.sleep(1)
print(f'{timestamp_to_date(int(time.time())*1000)} - Ok - Candles')

for pair in PAIR_LIST:
    init_get_funding_rate(pair)
print(f'Ok - Funding {timestamp_to_date(int(time.time())*1000)}')
