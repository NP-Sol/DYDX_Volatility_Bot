import pandas as pd
import math
from datetime import datetime
import time
import requests
import json
import os

from trading_constants import *
from trading_functions import *
from address import ADDRESS
from key import PASSPHRASE

#A modifier pour initialiser un portefeuille
MARKET = "LINK-USD"
PTF_NAME = "LINK_1124"
subaccount_number = 0

PATH = os.path.dirname(os.path.realpath(__file__))
PATH_DATA = f'{PATH}/TRADING_DATA'

PATH_TRADES = f'{PATH_DATA}/TRADES/TRADE_HISTORY_{MARKET}.json'
PATH_FUNDING = f'{PATH_DATA}/FUNDING_PAYMENTS/FUNDING_PAYMENTS_{MARKET}.json'
PATH_PNL = f'{PATH_DATA}/PNL_HISTORY.json'

init_ptf(PATH_DATA,MARKET,PTF_NAME)
init_json(PATH_TRADES)
init_json(PATH_FUNDING)
init_json(PATH_PNL)

NETWORK =network_setup()
index_client = index_client_setup(NETWORK)

init_get_trades(PATH_DATA,MARKET,index_client,ADDRESS,subaccount_number)
init_get_funding_payment(PATH_DATA,MARKET,index_client,ADDRESS,subaccount_number)