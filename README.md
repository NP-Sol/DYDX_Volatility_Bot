# DYDX_Volatility_Bot

!!! NOT FINANCIAL ADVICE !!!
- THIS PROGRAM IN NO WAY ENCOURAGES INVESTMENT OF ANY KIND !
- DO YOUR OWN RESEARCH AND MAKE SURE YOU FULLY UNDERSTAND BEFORE USING IT !
- ANY LOSS ARISING FROM ITS USE CANNOT BE ATTRIBUTED TO ANY OF ITS AUTHORS OR CONTRIBUTORS !

This program is a trading automaton whose purpose is to arbitrate asset volatility by balancing a portfolio containing half of any asset and half of our reference asset (in this case, the USD).
The automaton works with the DYDX platform API and can manage several portfolios simultaneously. It also allows you to be notified on Discord of each action taken.
Installation takes place in 3 stages:

1/ Download all the scripts from the repository into a folder of your choice.

2/ Make sure you have Python (>3.8) and the following libraries installed:
- v4_client_py  (and all dependencies)
- v4_proto (and all dependencies)
- pandas
- math
- time
- requests
- json
- os
- datetime
- time
- asyncio
- traceback

3/ Run the script 'get_public_data_init.py' and you are ready to configure the automaton !

To run the program, you will need a DYDX V4 account and (optional) a Discord account.
Follow the next step to finish the configuration :

1/ Add your Dydx address in the 'address.py' file (--> this will become an environment variable in a future version)

2/ Add your Dydx mnemonic in the 'key.py' file (--> this will also become an environment variable in a future version for obvious reasons)

3/ Add discord WebHooks in the 'trading_constants.py' file (or comment any call of the discord functions in 'main_trading.py' and 'tradiing_functions.py'

Now you are ready to run your first portfolio. There are (again) 3 steps :
1/ Open the 'initialize.py' file and modify the fields 'MARKET' and 'PTF_NAME' and run it.

2/ Open the 'capitalization.py' file and modify the fields 'MARKET' and 'PTF_NAME' with the same input as in 'initialize.py', then set up the initial state of the portfolio with the fields 'dollar_added' and 'asset_added' and then run it

3/ Open the 'main_trading.py' file and modify the fields 'MARKET' and 'PTF_NAME' as done before. Save it as 'main_trading_{MARKET}.py' and then run it.

Repeat those 3 steps to create other portfolios (yet you can only run one portfolio per asset and dydx account).

- BE CAREFUL, THE ALGORITHM DOESN'T CONTAIN ANY RISK MANAGEMENT MODULE!
- LOSSES AND LIQUIDATION COULD OCCUR IN CASE OF A BAD CONFIGURATION ! 

