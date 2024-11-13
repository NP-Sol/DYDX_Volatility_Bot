import pandas as pd


from datetime import datetime
import time
import json
import requests
import math
import os

from trading_functions import *

PATH = os.path.dirname(os.path.realpath(__file__))
PATH_DATA = f'{PATH}/TRADING_DATA'

## Fonction pour ajouter des valeurs dans le portefeuille (USD ou Asset).

#PTF='DOGE_0424'
#MARKET = 'DOGE-USD'

# PTF='DOGE_1124'
# MARKET = 'DOGE-USD'

PTF='BTC_1124'
MARKET = 'BTC-USD'

dollar_added = 50
asset_added = 0

ref ='capitalization #1'

L = maj_ptf_capitalization(PATH_DATA,MARKET,PTF, dollar_added, asset_added,ref)

print(f"Augmentation de capital de {dollar_added} $ et {asset_added} d'asset dans le portefeuille {MARKET}")
print(f"La nouvelle composition du portefeuille est {L[0]} {MARKET} et {L[1]} $")
print(f"La nouvelle valeur du portefeuille est {L[2]} $ pour # {L[3]} Shares, avec une valeur de {L[2]/L[3 ]} $ /Shares")
print(f"Le nombre de Shares a augmenté de {L[4]}")
