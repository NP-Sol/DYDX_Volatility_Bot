VALIDATOR_GRPC_ENDPOINT = 'dydx-grpc.publicnode.com:443'
AERIAL_CONFIG_URL = 'https://dydx-grpc.publicnode.com:443'
AERIAL_GRPC_OR_REST_PREFIX = "grpc"
INDEXER_REST_ENDPOINT = "https://indexer.dydx.trade/"
INDEXER_WS_ENDPOINT = "wss://indexer.dydx.trade/v4/ws"
CHAIN_ID = "dydx-mainnet-1"
ENV = 'mainnet'

intervals = ['1DAY', '4HOURS', '1HOUR', '30MINS', '15MINS', '5MINS', '1MIN']

PAIR_LIST = ['BTC-USD', 'ETH-USD', 'LINK-USD', 'MATIC-USD', 'CRV-USD', 'SOL-USD', 'ADA-USD', 'AVAX-USD', 
            'FIL-USD', 'LTC-USD', 'DOGE-USD', 'ATOM-USD', 'DOT-USD', 'UNI-USD', 'BCH-USD', 'TRX-USD', 
            'NEAR-USD', 'MKR-USD', 'XLM-USD', 'ETC-USD', 'COMP-USD', 'WLD-USD', 'APE-USD', 'APT-USD', 
            'ARB-USD', 'BLUR-USD', 'LDO-USD', 'OP-USD', 'PEPE-USD', 'SEI-USD', 'SHIB-USD', 'SUI-USD', 
            'XRP-USD', 'TIA-USD', 'JUP-USD', 'AAVE-USD', 'BNB-USD', 'JTO-USD', 'ORDI-USD', 'EOS-USD', 
            'ICP-USD', 'DYM-USD', 'STRK-USD', 'FET-USD', 'WOO-USD', 'PYTH-USD', 'BONK-USD', 'AGIX-USD', 
            'RENDER-USD', 'STX-USD', 'INJ-USD', 'IMX-USD', 'HBAR-USD', 'ALGO-USD', 'GRT-USD', 'MANA-USD', 
            'RUNE-USD', 'AXL-USD', 'AEVO-USD', 'ASTR-USD', 'SNX-USD', 'ARKM-USD', 'DYDX-USD', 'CHZ-USD', 
            'WIF-USD', 'ETHFI-USD', 'TON-USD', 'W-USD', 'MOTHER-USD', 'MOG-USD', 'TREMP-USD', 'BODEN-USD', 
            'ZRO-USD', 'ZK-USD', 'TLOS-USD', 'ONDO-USD', 'ENA-USD', 'IO-USD', 'AR-USD', 'KAS-USD', 'NOT-USD', 
            'ENS-USD', 'FLOKI-USD', 'TAO-USD', 'FTM-USD', 'SAFE-USD', 'TAIKO-USD', 'AKT-USD', 'CAKE-USD', 
            'BRETT-USD', 'SATS-USD', 'BLAST-USD', 'XMR-USD', 'THETA-USD', 'ENJ-USD', '1INCH-USD', 'XTZ-USD', 
            'UMA-USD', 'CVX-USD', 'SUSHI-USD', 'ZRX-USD', 'PENDLE-USD', 'DEGEN-USD', 'MNT-USD', 'JASMY-USD', 
            'CORE-USD', 'PEOPLE-USD', 'GMX-USD', 'POPCAT-USD', 'PRIME-USD', 'GALA-USD', 'AXS-USD', 'XAI-USD', 
            'MEW-USD', 'BEAM-USD', 'NEO-USD', 'EGLD-USD', 'ALT-USD', 'PIXEL-USD', 'TURBO-USD', 'BOME-USD', 
            'TRB-USD', 'ZEN-USD', 'BICO-USD', 'OM-USD', 'DMAIL-USD', 'MAVIA-USD', 'ZERO-USD', 'VRTX-USD', 
            'MICHI-USD', 'AURORA-USD', 'FOXY-USD', 'PAXG-USD', 'GME-USD', 'DRIFT-USD', 'EURC-USD', 
            'RETARDIO-USD', 'DAI-USD', 'OSMO-USD', 'NEIRO-USD', 'HNT-USD', 'TRY-USD', 'SUNDOG-USD', 
            'TRUMPWIN-USD', 'CETUS-USD', 'ZBCN-USD']

#Minimum Order Size
ORDER_SIZE = {'BTC-USD': 0.0001, 
              'ETH-USD': 0.001, 
              'LINK-USD': 1.0, 
              'MATIC-USD': 10.0, 
              'CRV-USD': 10.0, 
              'SOL-USD': 0.1, 
              'ADA-USD': 10.0, 
              'AVAX-USD': 0.1, 
              'FIL-USD': 1.0, 
              'LTC-USD': 0.1, 
              'DOGE-USD': 100.0, 
              'ATOM-USD': 1.0, 
              'DOT-USD': 1.0, 
              'UNI-USD': 1.0, 
              'BCH-USD': 0.01, 
              'TRX-USD': 100.0, 
              'NEAR-USD': 1.0, 
              'MKR-USD': 0.001, 
              'XLM-USD': 10.0, 
              'ETC-USD': 0.1, 
              'COMP-USD': 0.1, 
              'WLD-USD': 1.0, 
              'APE-USD': 1.0, 
              'APT-USD': 1.0, 
              'ARB-USD': 1.0, 
              'BLUR-USD': 10.0, 
              'LDO-USD': 1.0, 
              'OP-USD': 1.0, 
              'PEPE-USD': 10000000.0, 
              'SEI-USD': 10.0, 
              'SHIB-USD': 1000000.0, 
              'SUI-USD': 10.0, 
              'XRP-USD': 10.0, 
              'TIA-USD': 0.1, 
              'JUP-USD': 10.0, 
              'AAVE-USD': 0.1, 
              'BNB-USD': 0.01, 
              'JTO-USD': 1.0, 
              'ORDI-USD': 0.1, 
              'EOS-USD': 10.0, 
              'ICP-USD': 0.1, 
              'DYM-USD': 1.0, 
              'STRK-USD': 1.0, 
              'FET-USD': 10.0, 
              'WOO-USD': 10.0, 
              'PYTH-USD': 10.0, 
              'BONK-USD': 100000.0, 
              'AGIX-USD': 10.0, 
              'RENDER-USD': 1.0, 
              'STX-USD': 1.0, 
              'INJ-USD': 0.1, 
              'IMX-USD': 1.0, 
              'HBAR-USD': 10.0, 
              'ALGO-USD': 10.0,               
              'GRT-USD': 10.0, 
              'MANA-USD': 10.0, 
              'RUNE-USD': 1.0, 
              'AXL-USD': 1.0, 
              'AEVO-USD': 1.0, 
              'ASTR-USD': 10.0, 
              'SNX-USD': 1.0, 
              'ARKM-USD': 1.0, 
              'DYDX-USD': 1.0, 
              'CHZ-USD': 10.0, 
              'WIF-USD': 1.0, 
              'ETHFI-USD': 1.0, 
              'TON-USD': 1.0, 
              'W-USD': 10.0, 
              'MOTHER-USD': 10.0, 
              'MOG-USD': 10000000.0, 
              'TREMP-USD': 10.0, 
              'BODEN-USD': 10.0, 
              'ZRO-USD': 1.0, 
              'ZK-USD': 10.0, 
              'TLOS-USD': 10.0, 
              'ONDO-USD': 1.0, 
              'ENA-USD': 10.0, 
              'IO-USD': 1.0, 
              'AR-USD': 0.1, 
              'KAS-USD': 10.0, 
              'NOT-USD': 100.0, 
              'ENS-USD': 0.1, 
              'FLOKI-USD': 10000.0, 
              'TAO-USD': 0.01, 
              'FTM-USD': 10.0, 
              'SAFE-USD': 1.0, 
              'TAIKO-USD': 1.0, 
              'AKT-USD': 1.0, 
              'CAKE-USD': 1.0, 
              'BRETT-USD': 10.0, 
              'SATS-USD': 10000000.0, 
              'BLAST-USD': 100.0, 
              'XMR-USD': 0.01, 
              'THETA-USD': 1.0, 
              'ENJ-USD': 10.0, 
              '1INCH-USD': 10.0, 
              'XTZ-USD': 10.0, 
              'UMA-USD': 1.0, 
              'CVX-USD': 1.0,
              'SUSHI-USD': 10.0, 
              'ZRX-USD': 10.0, 
              'PENDLE-USD': 1.0, 
              'DEGEN-USD': 1000.0, 
              'MNT-USD': 10.0, 
              'JASMY-USD': 100.0, 
              'CORE-USD': 1.0, 
              'PEOPLE-USD': 100.0, 
              'GMX-USD': 0.1, 
              'POPCAT-USD': 10.0, 
              'PRIME-USD': 1.0, 
              'GALA-USD': 100.0, 
              'AXS-USD': 1.0, 
              'XAI-USD': 10.0, 
              'MEW-USD': 1000.0, 
              'BEAM-USD': 100.0, 
              'NEO-USD': 0.1, 
              'EGLD-USD': 0.1, 
              'ALT-USD': 10.0, 
              'PIXEL-USD': 10.0, 
              'TURBO-USD': 1000.0, 
              'BOME-USD': 1000.0, 
              'TRB-USD': 0.01, 
              'ZEN-USD': 1.0, 
              'BICO-USD': 10.0, 
              'OM-USD': 10.0, 
              'DMAIL-USD': 10.0, 
              'MAVIA-USD': 1.0, 
              'ZERO-USD': 10000.0, 
              'VRTX-USD': 10.0, 
              'MICHI-USD': 10.0, 
              'AURORA-USD': 10.0, 
              'FOXY-USD': 100.0, 
              'PAXG-USD': 0.001, 
              'GME-USD': 1000.0, 
              'DRIFT-USD': 10.0, 
              'EURC-USD': 1.0, 
              'RETARDIO-USD': 10.0, 
              'DAI-USD': 10.0, 
              'OSMO-USD': 10.0, 
              'NEIRO-USD': 100.0, 
              'HNT-USD': 1.0, 
              'TRY-USD': 100.0, 
              'SUNDOG-USD': 10.0, 
              'TRUMPWIN-USD': 1.0, 
              'CETUS-USD': 100.0, 
              'ZBCN-USD': 10000.0}

TICK_SIZE = {'BTC-USD': '1',
             'ETH-USD': '0.1',
             'LINK-USD': '0.001',
             'MATIC-USD': '0.0001',
             'CRV-USD': '0.0001',
             'SOL-USD': '0.01',
             'ADA-USD': '0.0001',
             'AVAX-USD': '0.01',
             'FIL-USD': '0.001',
             'LTC-USD': '0.01',
             'DOGE-USD': '0.00001',
             'ATOM-USD': '0.001',
             'DOT-USD': '0.001',
             'UNI-USD': '0.001',
             'BCH-USD': '0.1',
             'TRX-USD': '0.00001',
             'NEAR-USD': '0.001',
             'MKR-USD': '1',
             'XLM-USD': '0.0001',
             'ETC-USD': '0.01',
             'COMP-USD': '0.01',
             'WLD-USD': '0.001',
             'APE-USD': '0.001',
             'APT-USD': '0.001',
             'ARB-USD': '0.001',
             'BLUR-USD': '0.0001',
             'LDO-USD': '0.001',
             'OP-USD': '0.001',
             'PEPE-USD': '0.0000000001', 
             'SEI-USD': '0.0001',
             'SHIB-USD': '0.000000001',
             'SUI-USD': '0.0001',
             'XRP-USD': '0.0001',
             'TIA-USD': '0.01',
             'JUP-USD': '0.0001',
             'AAVE-USD': '0.01',
             'BNB-USD': '0.1',
             'JTO-USD': '0.001',
             'ORDI-USD': '0.01',
             'EOS-USD': '0.0001', 
             'ICP-USD': '0.01',
             'DYM-USD': '0.001',
             'STRK-USD': '0.001',
             'FET-USD': '0.0001',
             'WOO-USD': '0.0001',
             'PYTH-USD': '0.0001',
             'BONK-USD': '0.00000001',
             'AGIX-USD': '0.0001',
             'RENDER-USD': '0.001',
             'STX-USD': '0.001',
             'INJ-USD': '0.01',
             'IMX-USD': '0.001',
             'HBAR-USD': '0.0001',
             'ALGO-USD': '0.0001',
             'GRT-USD': '0.0001',
             'MANA-USD': '0.0001',
             'RUNE-USD': '0.001',
             'AXL-USD': '0.001', 
             'AEVO-USD': '0.001', 
             'ASTR-USD': '0.0001', 
             'SNX-USD': '0.001', 
             'ARKM-USD': '0.001', 
             'DYDX-USD': '0.001', 
             'CHZ-USD': '0.0001', 
             'WIF-USD': '0.001', 
             'ETHFI-USD': '0.001', 
             'TON-USD': '0.001', 
             'W-USD': '0.0001', 
             'MOTHER-USD': '0.0001', 
             'MOG-USD': '0.0000000001', 
             'TREMP-USD': '0.0001', 
             'BODEN-USD': '0.0001', 
             'ZRO-USD': '0.001', 
             'ZK-USD': '0.0001', 
             'TLOS-USD': '0.0001', 
             'ONDO-USD': '0.001', 
             'ENA-USD': '0.0001', 
             'IO-USD': '0.001', 
             'AR-USD': '0.01', 
             'KAS-USD': '0.0001', 
             'NOT-USD': '0.00001', 
             'ENS-USD': '0.01', 
             'FLOKI-USD': '0.0000001', 
             'TAO-USD': '0.1', 
             'FTM-USD': '0.0001', 
             'SAFE-USD': '0.001', 
             'TAIKO-USD': '0.001', 
             'AKT-USD': '0.001', 
             'CAKE-USD': '0.001', 
             'BRETT-USD': '0.0001', 
             'SATS-USD': '0.0000000001', 
             'BLAST-USD': '0.00001', 
             'XMR-USD': '0.1', 
             'THETA-USD': '0.001', 
             'ENJ-USD': '0.0001', 
             '1INCH-USD': '0.0001', 
             'XTZ-USD': '0.0001', 
             'UMA-USD': '0.001', 
             'CVX-USD': '0.001', 
             'SUSHI-USD': '0.0001', 
             'ZRX-USD': '0.0001', 
             'PENDLE-USD': '0.001', 
             'DEGEN-USD': '0.000001', 
             'MNT-USD': '0.0001', 
             'JASMY-USD': '0.00001', 
             'CORE-USD': '0.001', 
             'PEOPLE-USD': '0.00001', 
             'GMX-USD': '0.01', 
             'POPCAT-USD': '0.0001', 
             'PRIME-USD': '0.001', 
             'GALA-USD': '0.00001', 
             'AXS-USD': '0.001', 
             'XAI-USD': '0.0001', 
             'MEW-USD': '0.000001', 
             'BEAM-USD': '0.00001', 
             'NEO-USD': '0.01', 
             'EGLD-USD': '0.01', 
             'ALT-USD': '0.0001', 
             'PIXEL-USD': '0.0001', 
             'TURBO-USD': '0.000001', 
             'BOME-USD': '0.000001', 
             'TRB-USD': '0.1', 
             'ZEN-USD': '0.001', 
             'BICO-USD': '0.0001', 
             'OM-USD': '0.0001', 
             'DMAIL-USD': '0.0001', 
             'MAVIA-USD': '0.001', 
             'ZERO-USD': '0.0000001', 
             'VRTX-USD': '0.0001', 
             'MICHI-USD': '0.0001', 
             'AURORA-USD': '0.0001', 
             'FOXY-USD': '0.00001', 
             'PAXG-USD': '1', 
             'GME-USD': '0.000001', 
             'DRIFT-USD': '0.0001', 
             'EURC-USD': '0.001', 
             'RETARDIO-USD': '0.0001', 
             'DAI-USD': '0.0001', 
             'OSMO-USD': '0.0001', 
             'NEIRO-USD': '0.00001', 
             'HNT-USD': '0.001', 
             'TRY-USD': '0.00001', 
             'SUNDOG-USD': '0.0001',
             'TRUMPWIN-USD': '0.001',
             'CETUS-USD': '0.00001',
             'ZBCN-USD': '0.0000001'}

#Webhooks discord
CHANNELS_DISCORD = {'BTC-USD': 'https://discord.com/api/webhooks/xxxxxxxxxxxxxxxxxxxxx/xxxxxxxxxxxxxxxxxxxx',
             'ETH-USD': 'https://discord.com/api/webhooks/xxxxxxxxxxxxxxxxxxxxx/xxxxxxxxxxxxxxxxxxxx',
             'LINK-USD': 'https://discord.com/api/webhooks/xxxxxxxxxxxxxxxxxxxxx/xxxxxxxxxxxxxxxxxxxx',
             'MATIC-USD': 'https://discord.com/api/webhooks/xxxxxxxxxxxxxxxxxxxxx/xxxxxxxxxxxxxxxxxxxx',
             'CRV-USD': 'https://discord.com/api/webhooks/xxxxxxxxxxxxxxxxxxxxx/xxxxxxxxxxxxxxxxxxxx',
             'SOL-USD': 'https://discord.com/api/webhooks/xxxxxxxxxxxxxxxxxxxxx/xxxxxxxxxxxxxxxxxxxx',
             'ADA-USD': 'https://discord.com/api/webhooks/xxxxxxxxxxxxxxxxxxxxx/xxxxxxxxxxxxxxxxxxxx',
             'AVAX-USD': 'https://discord.com/api/webhooks/xxxxxxxxxxxxxxxxxxxxx/xxxxxxxxxxxxxxxxxxxx',
             'FIL-USD': 'https://discord.com/api/webhooks/xxxxxxxxxxxxxxxxxxxxx/xxxxxxxxxxxxxxxxxxxx',
             'LTC-USD': 'https://discord.com/api/webhooks/xxxxxxxxxxxxxxxxxxxxx/xxxxxxxxxxxxxxxxxxxx',
             'DOGE-USD': 'https://discord.com/api/webhooks/xxxxxxxxxxxxxxxxxxxxx/xxxxxxxxxxxxxxxxxxxx',
             'ATOM-USD': 'https://discord.com/api/webhooks/xxxxxxxxxxxxxxxxxxxxx/xxxxxxxxxxxxxxxxxxxx',
             'DOT-USD': 'https://discord.com/api/webhooks/xxxxxxxxxxxxxxxxxxxxx/xxxxxxxxxxxxxxxxxxxx',
             'UNI-USD': 'https://discord.com/api/webhooks/xxxxxxxxxxxxxxxxxxxxx/xxxxxxxxxxxxxxxxxxxx',
             'BCH-USD': 'https://discord.com/api/webhooks/xxxxxxxxxxxxxxxxxxxxx/xxxxxxxxxxxxxxxxxxxx',
             'TRX-USD': 'https://discord.com/api/webhooks/xxxxxxxxxxxxxxxxxxxxx/xxxxxxxxxxxxxxxxxxxx',
             'NEAR-USD': 'https://discord.com/api/webhooks/xxxxxxxxxxxxxxxxxxxxx/xxxxxxxxxxxxxxxxxxxx',
             'MKR-USD': 'https://discord.com/api/webhooks/xxxxxxxxxxxxxxxxxxxxx/xxxxxxxxxxxxxxxxxxxx',
             'XLM-USD': 'https://discord.com/api/webhooks/xxxxxxxxxxxxxxxxxxxxx/xxxxxxxxxxxxxxxxxxxx',
             'ETC-USD': 'https://discord.com/api/webhooks/xxxxxxxxxxxxxxxxxxxxx/xxxxxxxxxxxxxxxxxxxx',
             'COMP-USD': 'https://discord.com/api/webhooks/xxxxxxxxxxxxxxxxxxxxx/xxxxxxxxxxxxxxxxxxxx',
             'WLD-USD': 'https://discord.com/api/webhooks/xxxxxxxxxxxxxxxxxxxxx/xxxxxxxxxxxxxxxxxxxx',
             'APE-USD': 'https://discord.com/api/webhooks/xxxxxxxxxxxxxxxxxxxxx/xxxxxxxxxxxxxxxxxxxx',
             'APT-USD': 'https://discord.com/api/webhooks/xxxxxxxxxxxxxxxxxxxxx/xxxxxxxxxxxxxxxxxxxx',
             'ARB-USD': 'https://discord.com/api/webhooks/xxxxxxxxxxxxxxxxxxxxx/xxxxxxxxxxxxxxxxxxxx',
             'BLUR-USD': 'https://discord.com/api/webhooks/xxxxxxxxxxxxxxxxxxxxx/xxxxxxxxxxxxxxxxxxxx',
             'LDO-USD': 'https://discord.com/api/webhooks/xxxxxxxxxxxxxxxxxxxxx/xxxxxxxxxxxxxxxxxxxx',
             'OP-USD': 'https://discord.com/api/webhooks/xxxxxxxxxxxxxxxxxxxxx/xxxxxxxxxxxxxxxxxxxx',
             'PEPE-USD': 'https://discord.com/api/webhooks/xxxxxxxxxxxxxxxxxxxxx/xxxxxxxxxxxxxxxxxxxx', 
             'SEI-USD': 'https://discord.com/api/webhooks/xxxxxxxxxxxxxxxxxxxxx/xxxxxxxxxxxxxxxxxxxx',
             'SHIB-USD': 'https://discord.com/api/webhooks/xxxxxxxxxxxxxxxxxxxxx/xxxxxxxxxxxxxxxxxxxx',
             'SUI-USD': 'https://discord.com/api/webhooks/xxxxxxxxxxxxxxxxxxxxx/xxxxxxxxxxxxxxxxxxxx',
             'XRP-USD': 'https://discord.com/api/webhooks/xxxxxxxxxxxxxxxxxxxxx/xxxxxxxxxxxxxxxxxxxx',
             'TIA-USD': 'https://discord.com/api/webhooks/xxxxxxxxxxxxxxxxxxxxx/xxxxxxxxxxxxxxxxxxxx',
             'JUP-USD': 'https://discord.com/api/webhooks/xxxxxxxxxxxxxxxxxxxxx/xxxxxxxxxxxxxxxxxxxx',
             'AAVE-USD': 'https://discord.com/api/webhooks/xxxxxxxxxxxxxxxxxxxxx/xxxxxxxxxxxxxxxxxxxx',
             'BNB-USD': 'https://discord.com/api/webhooks/xxxxxxxxxxxxxxxxxxxxx/xxxxxxxxxxxxxxxxxxxx',
             'JTO-USD': 'https://discord.com/api/webhooks/xxxxxxxxxxxxxxxxxxxxx/xxxxxxxxxxxxxxxxxxxx',
             'ORDI-USD': 'https://discord.com/api/webhooks/xxxxxxxxxxxxxxxxxxxxx/xxxxxxxxxxxxxxxxxxxx',
             'EOS-USD': 'https://discord.com/api/webhooks/xxxxxxxxxxxxxxxxxxxxx/xxxxxxxxxxxxxxxxxxxx', 
             'ICP-USD': 'https://discord.com/api/webhooks/xxxxxxxxxxxxxxxxxxxxx/xxxxxxxxxxxxxxxxxxxx',
             'DYM-USD': 'https://discord.com/api/webhooks/xxxxxxxxxxxxxxxxxxxxx/xxxxxxxxxxxxxxxxxxxx',
             'STRK-USD': 'https://discord.com/api/webhooks/xxxxxxxxxxxxxxxxxxxxx/xxxxxxxxxxxxxxxxxxxx',
             'FET-USD': 'https://discord.com/api/webhooks/xxxxxxxxxxxxxxxxxxxxx/xxxxxxxxxxxxxxxxxxxx',
             'WOO-USD': 'https://discord.com/api/webhooks/xxxxxxxxxxxxxxxxxxxxx/xxxxxxxxxxxxxxxxxxxx',
             'PYTH-USD': 'https://discord.com/api/webhooks/xxxxxxxxxxxxxxxxxxxxx/xxxxxxxxxxxxxxxxxxxx',
             'BONK-USD': 'https://discord.com/api/webhooks/xxxxxxxxxxxxxxxxxxxxx/xxxxxxxxxxxxxxxxxxxx',
             'AGIX-USD': 'https://discord.com/api/webhooks/xxxxxxxxxxxxxxxxxxxxx/xxxxxxxxxxxxxxxxxxxx',
             'RENDER-USD': 'https://discord.com/api/webhooks/xxxxxxxxxxxxxxxxxxxxx/xxxxxxxxxxxxxxxxxxxx',
             'STX-USD': 'https://discord.com/api/webhooks/xxxxxxxxxxxxxxxxxxxxx/xxxxxxxxxxxxxxxxxxxx',
             'INJ-USD': 'https://discord.com/api/webhooks/xxxxxxxxxxxxxxxxxxxxx/xxxxxxxxxxxxxxxxxxxx',
             'IMX-USD': 'https://discord.com/api/webhooks/xxxxxxxxxxxxxxxxxxxxx/xxxxxxxxxxxxxxxxxxxx',
             'HBAR-USD': 'https://discord.com/api/webhooks/xxxxxxxxxxxxxxxxxxxxx/xxxxxxxxxxxxxxxxxxxx',
             'ALGO-USD': 'https://discord.com/api/webhooks/xxxxxxxxxxxxxxxxxxxxx/xxxxxxxxxxxxxxxxxxxx',
             'GRT-USD': 'https://discord.com/api/webhooks/xxxxxxxxxxxxxxxxxxxxx/xxxxxxxxxxxxxxxxxxxx',
             'MANA-USD': 'https://discord.com/api/webhooks/xxxxxxxxxxxxxxxxxxxxx/xxxxxxxxxxxxxxxxxxxx',
             'RUNE-USD': 'https://discord.com/api/webhooks/xxxxxxxxxxxxxxxxxxxxx/xxxxxxxxxxxxxxxxxxxx',
             'AXL-USD': 'https://discord.com/api/webhooks/xxxxxxxxxxxxxxxxxxxxx/xxxxxxxxxxxxxxxxxxxx', 
             'AEVO-USD': 'https://discord.com/api/webhooks/xxxxxxxxxxxxxxxxxxxxx/xxxxxxxxxxxxxxxxxxxx', 
             'ASTR-USD': 'https://discord.com/api/webhooks/xxxxxxxxxxxxxxxxxxxxx/xxxxxxxxxxxxxxxxxxxx', 
             'SNX-USD': 'https://discord.com/api/webhooks/xxxxxxxxxxxxxxxxxxxxx/xxxxxxxxxxxxxxxxxxxx', 
             'ARKM-USD': 'https://discord.com/api/webhooks/xxxxxxxxxxxxxxxxxxxxx/xxxxxxxxxxxxxxxxxxxx', 
             'DYDX-USD': 'https://discord.com/api/webhooks/xxxxxxxxxxxxxxxxxxxxx/xxxxxxxxxxxxxxxxxxxx', 
             'CHZ-USD': 'https://discord.com/api/webhooks/xxxxxxxxxxxxxxxxxxxxx/xxxxxxxxxxxxxxxxxxxx', 
             'WIF-USD': 'https://discord.com/api/webhooks/xxxxxxxxxxxxxxxxxxxxx/xxxxxxxxxxxxxxxxxxxx', 
             'ETHFI-USD': 'https://discord.com/api/webhooks/xxxxxxxxxxxxxxxxxxxxx/xxxxxxxxxxxxxxxxxxxx', 
             'TON-USD': 'https://discord.com/api/webhooks/xxxxxxxxxxxxxxxxxxxxx/xxxxxxxxxxxxxxxxxxxx', 
             'W-USD': 'https://discord.com/api/webhooks/xxxxxxxxxxxxxxxxxxxxx/xxxxxxxxxxxxxxxxxxxx', 
             'MOTHER-USD': 'https://discord.com/api/webhooks/xxxxxxxxxxxxxxxxxxxxx/xxxxxxxxxxxxxxxxxxxx', 
             'MOG-USD': 'https://discord.com/api/webhooks/xxxxxxxxxxxxxxxxxxxxx/xxxxxxxxxxxxxxxxxxxx', 
             'TREMP-USD': 'https://discord.com/api/webhooks/xxxxxxxxxxxxxxxxxxxxx/xxxxxxxxxxxxxxxxxxxx', 
             'BODEN-USD': 'https://discord.com/api/webhooks/xxxxxxxxxxxxxxxxxxxxx/xxxxxxxxxxxxxxxxxxxx', 
             'ZRO-USD': 'https://discord.com/api/webhooks/xxxxxxxxxxxxxxxxxxxxx/xxxxxxxxxxxxxxxxxxxx', 
             'ZK-USD': 'https://discord.com/api/webhooks/xxxxxxxxxxxxxxxxxxxxx/xxxxxxxxxxxxxxxxxxxx', 
             'TLOS-USD': 'https://discord.com/api/webhooks/xxxxxxxxxxxxxxxxxxxxx/xxxxxxxxxxxxxxxxxxxx', 
             'ONDO-USD': 'https://discord.com/api/webhooks/xxxxxxxxxxxxxxxxxxxxx/xxxxxxxxxxxxxxxxxxxx', 
             'ENA-USD': 'https://discord.com/api/webhooks/xxxxxxxxxxxxxxxxxxxxx/xxxxxxxxxxxxxxxxxxxx', 
             'IO-USD': 'https://discord.com/api/webhooks/xxxxxxxxxxxxxxxxxxxxx/xxxxxxxxxxxxxxxxxxxx', 
             'AR-USD': 'https://discord.com/api/webhooks/xxxxxxxxxxxxxxxxxxxxx/xxxxxxxxxxxxxxxxxxxx', 
             'KAS-USD': 'https://discord.com/api/webhooks/xxxxxxxxxxxxxxxxxxxxx/xxxxxxxxxxxxxxxxxxxx', 
             'NOT-USD': 'https://discord.com/api/webhooks/xxxxxxxxxxxxxxxxxxxxx/xxxxxxxxxxxxxxxxxxxx', 
             'ENS-USD': 'https://discord.com/api/webhooks/xxxxxxxxxxxxxxxxxxxxx/xxxxxxxxxxxxxxxxxxxx', 
             'FLOKI-USD': 'https://discord.com/api/webhooks/xxxxxxxxxxxxxxxxxxxxx/xxxxxxxxxxxxxxxxxxxx', 
             'TAO-USD': 'https://discord.com/api/webhooks/xxxxxxxxxxxxxxxxxxxxx/xxxxxxxxxxxxxxxxxxxx', 
             'FTM-USD': 'https://discord.com/api/webhooks/xxxxxxxxxxxxxxxxxxxxx/xxxxxxxxxxxxxxxxxxxx', 
             'SAFE-USD': 'https://discord.com/api/webhooks/xxxxxxxxxxxxxxxxxxxxx/xxxxxxxxxxxxxxxxxxxx', 
             'TAIKO-USD': 'https://discord.com/api/webhooks/xxxxxxxxxxxxxxxxxxxxx/xxxxxxxxxxxxxxxxxxxx', 
             'AKT-USD': 'https://discord.com/api/webhooks/xxxxxxxxxxxxxxxxxxxxx/xxxxxxxxxxxxxxxxxxxx', 
             'CAKE-USD': 'https://discord.com/api/webhooks/xxxxxxxxxxxxxxxxxxxxx/xxxxxxxxxxxxxxxxxxxx', 
             'BRETT-USD': 'https://discord.com/api/webhooks/xxxxxxxxxxxxxxxxxxxxx/xxxxxxxxxxxxxxxxxxxx', 
             'SATS-USD': 'https://discord.com/api/webhooks/xxxxxxxxxxxxxxxxxxxxx/xxxxxxxxxxxxxxxxxxxx', 
             'BLAST-USD': 'https://discord.com/api/webhooks/xxxxxxxxxxxxxxxxxxxxx/xxxxxxxxxxxxxxxxxxxx', 
             'XMR-USD': 'https://discord.com/api/webhooks/xxxxxxxxxxxxxxxxxxxxx/xxxxxxxxxxxxxxxxxxxx', 
             'THETA-USD': 'https://discord.com/api/webhooks/xxxxxxxxxxxxxxxxxxxxx/xxxxxxxxxxxxxxxxxxxx', 
             'ENJ-USD': 'https://discord.com/api/webhooks/xxxxxxxxxxxxxxxxxxxxx/xxxxxxxxxxxxxxxxxxxx', 
             '1INCH-USD': 'https://discord.com/api/webhooks/xxxxxxxxxxxxxxxxxxxxx/xxxxxxxxxxxxxxxxxxxx', 
             'XTZ-USD': 'https://discord.com/api/webhooks/xxxxxxxxxxxxxxxxxxxxx/xxxxxxxxxxxxxxxxxxxx', 
             'UMA-USD': 'https://discord.com/api/webhooks/xxxxxxxxxxxxxxxxxxxxx/xxxxxxxxxxxxxxxxxxxx', 
             'CVX-USD': 'https://discord.com/api/webhooks/xxxxxxxxxxxxxxxxxxxxx/xxxxxxxxxxxxxxxxxxxx', 
             'SUSHI-USD': 'https://discord.com/api/webhooks/xxxxxxxxxxxxxxxxxxxxx/xxxxxxxxxxxxxxxxxxxx', 
             'ZRX-USD': 'https://discord.com/api/webhooks/xxxxxxxxxxxxxxxxxxxxx/xxxxxxxxxxxxxxxxxxxx', 
             'PENDLE-USD': 'https://discord.com/api/webhooks/xxxxxxxxxxxxxxxxxxxxx/xxxxxxxxxxxxxxxxxxxx', 
             'DEGEN-USD': 'https://discord.com/api/webhooks/xxxxxxxxxxxxxxxxxxxxx/xxxxxxxxxxxxxxxxxxxx', 
             'MNT-USD': 'https://discord.com/api/webhooks/xxxxxxxxxxxxxxxxxxxxx/xxxxxxxxxxxxxxxxxxxx', 
             'JASMY-USD': 'https://discord.com/api/webhooks/xxxxxxxxxxxxxxxxxxxxx/xxxxxxxxxxxxxxxxxxxx', 
             'CORE-USD': 'https://discord.com/api/webhooks/xxxxxxxxxxxxxxxxxxxxx/xxxxxxxxxxxxxxxxxxxx', 
             'PEOPLE-USD': 'https://discord.com/api/webhooks/xxxxxxxxxxxxxxxxxxxxx/xxxxxxxxxxxxxxxxxxxx', 
             'GMX-USD': 'https://discord.com/api/webhooks/xxxxxxxxxxxxxxxxxxxxx/xxxxxxxxxxxxxxxxxxxx', 
             'POPCAT-USD': 'https://discord.com/api/webhooks/xxxxxxxxxxxxxxxxxxxxx/xxxxxxxxxxxxxxxxxxxx', 
             'PRIME-USD': 'https://discord.com/api/webhooks/xxxxxxxxxxxxxxxxxxxxx/xxxxxxxxxxxxxxxxxxxx', 
             'GALA-USD': 'https://discord.com/api/webhooks/xxxxxxxxxxxxxxxxxxxxx/xxxxxxxxxxxxxxxxxxxx', 
             'AXS-USD': 'https://discord.com/api/webhooks/xxxxxxxxxxxxxxxxxxxxx/xxxxxxxxxxxxxxxxxxxx', 
             'XAI-USD': 'https://discord.com/api/webhooks/xxxxxxxxxxxxxxxxxxxxx/xxxxxxxxxxxxxxxxxxxx', 
             'MEW-USD': 'https://discord.com/api/webhooks/xxxxxxxxxxxxxxxxxxxxx/xxxxxxxxxxxxxxxxxxxx', 
             'BEAM-USD': 'https://discord.com/api/webhooks/xxxxxxxxxxxxxxxxxxxxx/xxxxxxxxxxxxxxxxxxxx', 
             'NEO-USD': 'https://discord.com/api/webhooks/xxxxxxxxxxxxxxxxxxxxx/xxxxxxxxxxxxxxxxxxxx', 
             'EGLD-USD': 'https://discord.com/api/webhooks/xxxxxxxxxxxxxxxxxxxxx/xxxxxxxxxxxxxxxxxxxx', 
             'ALT-USD': 'https://discord.com/api/webhooks/xxxxxxxxxxxxxxxxxxxxx/xxxxxxxxxxxxxxxxxxxx', 
             'PIXEL-USD': 'https://discord.com/api/webhooks/xxxxxxxxxxxxxxxxxxxxx/xxxxxxxxxxxxxxxxxxxx', 
             'TURBO-USD': 'https://discord.com/api/webhooks/xxxxxxxxxxxxxxxxxxxxx/xxxxxxxxxxxxxxxxxxxx', 
             'BOME-USD': 'https://discord.com/api/webhooks/xxxxxxxxxxxxxxxxxxxxx/xxxxxxxxxxxxxxxxxxxx', 
             'TRB-USD': 'https://discord.com/api/webhooks/xxxxxxxxxxxxxxxxxxxxx/xxxxxxxxxxxxxxxxxxxx', 
             'ZEN-USD': 'https://discord.com/api/webhooks/xxxxxxxxxxxxxxxxxxxxx/xxxxxxxxxxxxxxxxxxxx', 
             'BICO-USD': 'https://discord.com/api/webhooks/xxxxxxxxxxxxxxxxxxxxx/xxxxxxxxxxxxxxxxxxxx', 
             'OM-USD': 'https://discord.com/api/webhooks/xxxxxxxxxxxxxxxxxxxxx/xxxxxxxxxxxxxxxxxxxx', 
             'DMAIL-USD': 'https://discord.com/api/webhooks/xxxxxxxxxxxxxxxxxxxxx/xxxxxxxxxxxxxxxxxxxx', 
             'MAVIA-USD': 'https://discord.com/api/webhooks/xxxxxxxxxxxxxxxxxxxxx/xxxxxxxxxxxxxxxxxxxx', 
             'ZERO-USD': 'https://discord.com/api/webhooks/xxxxxxxxxxxxxxxxxxxxx/xxxxxxxxxxxxxxxxxxxx', 
             'VRTX-USD': 'https://discord.com/api/webhooks/xxxxxxxxxxxxxxxxxxxxx/xxxxxxxxxxxxxxxxxxxx', 
             'MICHI-USD': 'https://discord.com/api/webhooks/xxxxxxxxxxxxxxxxxxxxx/xxxxxxxxxxxxxxxxxxxx', 
             'AURORA-USD': 'https://discord.com/api/webhooks/xxxxxxxxxxxxxxxxxxxxx/xxxxxxxxxxxxxxxxxxxx', 
             'FOXY-USD': 'https://discord.com/api/webhooks/xxxxxxxxxxxxxxxxxxxxx/xxxxxxxxxxxxxxxxxxxx', 
             'PAXG-USD': 'https://discord.com/api/webhooks/xxxxxxxxxxxxxxxxxxxxx/xxxxxxxxxxxxxxxxxxxx', 
             'GME-USD': 'https://discord.com/api/webhooks/xxxxxxxxxxxxxxxxxxxxx/xxxxxxxxxxxxxxxxxxxx', 
             'DRIFT-USD': 'https://discord.com/api/webhooks/xxxxxxxxxxxxxxxxxxxxx/xxxxxxxxxxxxxxxxxxxx', 
             'EURC-USD': 'https://discord.com/api/webhooks/xxxxxxxxxxxxxxxxxxxxx/xxxxxxxxxxxxxxxxxxxx', 
             'RETARDIO-USD': 'https://discord.com/api/webhooks/xxxxxxxxxxxxxxxxxxxxx/xxxxxxxxxxxxxxxxxxxx', 
             'DAI-USD': 'https://discord.com/api/webhooks/xxxxxxxxxxxxxxxxxxxxx/xxxxxxxxxxxxxxxxxxxx', 
             'OSMO-USD': 'https://discord.com/api/webhooks/xxxxxxxxxxxxxxxxxxxxx/xxxxxxxxxxxxxxxxxxxx', 
             'NEIRO-USD': 'https://discord.com/api/webhooks/xxxxxxxxxxxxxxxxxxxxx/xxxxxxxxxxxxxxxxxxxx', 
             'HNT-USD': 'https://discord.com/api/webhooks/xxxxxxxxxxxxxxxxxxxxx/xxxxxxxxxxxxxxxxxxxx', 
             'TRY-USD': 'https://discord.com/api/webhooks/xxxxxxxxxxxxxxxxxxxxx/xxxxxxxxxxxxxxxxxxxx', 
             'SUNDOG-USD': 'https://discord.com/api/webhooks/xxxxxxxxxxxxxxxxxxxxx/xxxxxxxxxxxxxxxxxxxx',
             'TRUMPWIN-USD': 'https://discord.com/api/webhooks/xxxxxxxxxxxxxxxxxxxxx/xxxxxxxxxxxxxxxxxxxx',
             'CETUS-USD': 'https://discord.com/api/webhooks/xxxxxxxxxxxxxxxxxxxxx/xxxxxxxxxxxxxxxxxxxx',
             'ZBCN-USD': 'https://discord.com/api/webhooks/xxxxxxxxxxxxxxxxxxxxx/xxxxxxxxxxxxxxxxxxxx'
             }
