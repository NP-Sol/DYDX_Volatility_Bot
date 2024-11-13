#!pip install discord.py


import pandas as pd


from datetime import datetime
import time
import json
import requests
import math
import os
import asyncio

import traceback

from trading_functions import *
from trading_constants import *
from key import PASSPHRASE
from address import ADDRESS

PATH = os.path.dirname(os.path.realpath(__file__))
PATH_DATA = f'{PATH}/TRADING_DATA'

#Portefeuille
MARKET = 'BTC-USD'
PTF = 'BTC_1124'

NETWORK = network_setup()
comp_client = comp_client_setup(NETWORK)
index_client = index_client_setup(NETWORK)

Wallet = wallet_setup(PASSPHRASE)
Subaccount_number = 0
#print(f"Valeur de self.wallet: {Wallet}")

#MaJ
get_funding_payment(PATH_DATA,MARKET,index_client,PTF,ADDRESS,Subaccount_number)
maj = get_trades(PATH_DATA,MARKET,index_client,PTF,ADDRESS,Subaccount_number)

delete_orders(MARKET,index_client,comp_client,ADDRESS, Subaccount_number,Wallet)
make_trade(MARKET,PATH_DATA,index_client,comp_client,PTF,Wallet)

while True:
    try:
        get_funding_payment(PATH_DATA,MARKET,index_client,PTF,ADDRESS,Subaccount_number)
        maj = get_trades(PATH_DATA,MARKET,index_client,PTF,ADDRESS,Subaccount_number)
        #get_pnl(PATH_DATA,index_client,ADDRESS, Subaccount_number)
    
        if maj:
            delete_orders(MARKET,index_client,comp_client,ADDRESS, Subaccount_number,Wallet)
            make_trade(MARKET,PATH_DATA,index_client,comp_client,PTF,Wallet)

    except Exception as e:
        print("Une erreur s'est produite")
        message = f"Une erreur s'est produite: {e}"
        traceback.print_exc()
        send_message_to_discord(message, MARKET)
        #log_error(e,PATH_DATA,MARKET)

#        continue

    time.sleep(30)
