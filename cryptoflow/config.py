"""
Config module for Cryptoflow!
"""
import json
from airflow.models import Variable

# pylint: disable=bare-except
try:
    CF_CONFIG = json.loads(Variable.get("CRYPTOFLOW_CONFIG"))
except:
    CF_CONFIG = {
        "1INCH": {
            "btd": {
                "dip_price": 3.35,
                "amount_usd": 5,
                "smallest_unit": 2,
                "schedule": "*/60 * * * *"
            },
            "dca": {
                "amount_usd": 10,
                "schedule": None
            }
        },
        "AAVE": {
            "btd": {
                "dip_price": 350,
                "amount_usd": 5,
                "smallest_unit": 5,
                "schedule": "*/60 * * * *"
            },
            "dca": {
                "amount_usd": 10,
                "schedule": None
            }
        },
        "ADA": {
            "btd": {
                "dip_price": 1.70,
                "amount_usd": 5,
                "smallest_unit": 8,
                "schedule": "*/60 * * * *"
            },
            "dca": {
                "amount_usd": 10,
                "schedule": "0 5 * * 1"
            }
        },
        "ALGO": {
            "btd": {
                "dip_price": 1.25,
                "amount_usd": 5,
                "smallest_unit": 0,
                "schedule": "*/60 * * * *"
            },
            "dca": {
                "amount_usd": 10,
                "schedule": None
            }
        },
        "AMP": {
            "btd": {
                "dip_price": 0.05,
                "amount_usd": 5,
                "smallest_unit": 6,
                "schedule": "*/60 * * * *"
            },
            "dca": {
                "amount_usd": 10,
                "schedule": None
            }
        },
        "ANKR": {
            "btd": {
                "dip_price": 0.12,
                "amount_usd": 5,
                "smallest_unit": 0,
                "schedule": "*/60 * * * *"
            },
            "dca": {
                "amount_usd": 10,
                "schedule": None
            }
        },
        "ATOM": {
            "btd": {
                "dip_price": 14,
                "amount_usd": 5,
                "smallest_unit": 8,
                "schedule": "*/60 * * * *"
            },
            "dca": {
                "amount_usd": 10,
                "schedule": None
            }
        },
        "BAND": {
            "btd": {
                "dip_price": 9,
                "amount_usd": 5,
                "smallest_unit": 2,
                "schedule": "*/60 * * * *"
            },
            "dca": {
                "amount_usd": 10,
                "schedule": None
            }
        },
        "BAL": {
            "btd": {
                "dip_price": 35,
                "amount_usd": 5,
                "smallest_unit": 1,
                "schedule": "*/60 * * * *"
            },
            "dca": {
                "amount_usd": 10,
                "schedule": None
            }
        },
        "BAT": {
            "btd": {
                "dip_price": 0.45,
                "amount_usd": 5,
                "smallest_unit": 2,
                "schedule": "*/60 * * * *"
            },
            "dca": {
                "amount_usd": 10,
                "schedule": None
            }
        },
        "BCH": {
            "btd": {
                "dip_price": 700,
                "amount_usd": 5,
                "smallest_unit": 8,
                "schedule": "*/60 * * * *"
            },
            "dca": {
                "amount_usd": 10,
                "schedule": None
            }
        },
        "BNT": {
            "btd": {
                "dip_price": 5,
                "amount_usd": 5,
                "smallest_unit": 8,
                "schedule": "*/60 * * * *"
            },
            "dca": {
                "amount_usd": 10,
                "schedule": None
            }
        },
        "BTC": {
            "btd": {
                "dip_price": 41000,
                "amount_usd": 5,
                "smallest_unit": 8,
                "schedule": "*/30 * * * *"
            },
            "dca": {
                "amount_usd": 10,
                "schedule": "0 5 * * 1"
            }
        },
        "CGLD": {
            "btd": {
                "dip_price": 4.10,
                "amount_usd": 5,
                "smallest_unit": 2,
                "schedule": "*/60 * * * *"
            },
            "dca": {
                "amount_usd": 10,
                "schedule": None
            }
        },
        "COMP": {
            "btd": {
                "dip_price": 490,
                "amount_usd": 5,
                "smallest_unit": 8,
                "schedule": "*/60 * * * *"
            },
            "dca": {
                "amount_usd": 10,
                "schedule": None
            }
        },
        "CRV": {
            "btd": {
                "dip_price": 2,
                "amount_usd": 5,
                "smallest_unit": 2,
                "schedule": "*/60 * * * *"
            },
            "dca": {
                "amount_usd": 10,
                "schedule": None
            }
        },
        "CTSI": {
            "btd": {
                "dip_price": 90,
                "amount_usd": 5,
                "smallest_unit": 1,
                "schedule": "*/60 * * * *"
            },
            "dca": {
                "amount_usd": 10,
                "schedule": None
            }
        },
        "CVC": {
            "btd": {
                "dip_price": 0.32,
                "amount_usd": 5,
                "smallest_unit": 8,
                "schedule": "*/60 * * * *"
            },
            "dca": {
                "amount_usd": 10,
                "schedule": None
            }
        },
        "DAI": {
            "btd": {
                "dip_price": 0.999900,
                "amount_usd": 5,
                "smallest_unit": 5,
                "schedule": "*/60 * * * *"
            },
            "dca": {
                "amount_usd": 10,
                "schedule": None
            }
        },
        "DASH": {
            "btd": {
                "dip_price": 150,
                "amount_usd": 5,
                "smallest_unit": 3,
                "schedule": "*/60 * * * *"
            },
            "dca": {
                "amount_usd": 10,
                "schedule": None
            }
        },
        "DNT": {
            "btd": {
                "dip_price": 0.20,
                "amount_usd": 5,
                "smallest_unit": 8,
                "schedule": "*/60 * * * *"
            },
            "dca": {
                "amount_usd": 10,
                "schedule": None
            }
        },
        "DOGE": {
            "btd": {
                "dip_price": 0.35,
                "amount_usd": 5,
                "smallest_unit": 6,
                "schedule": "*/60 * * * *"
            },
            "dca": {
                "amount_usd": 10,
                "schedule": None
            }
        },
        "ENJ": {
            "btd": {
                "dip_price": 1.25,
                "amount_usd": 5,
                "smallest_unit": 2,
                "schedule": "*/60 * * * *"
            },
            "dca": {
                "amount_usd": 10,
                "schedule": None
            }
        },
        "EOS": {
            "btd": {
                "dip_price": 5,
                "amount_usd": 5,
                "smallest_unit": 1,
                "schedule": "*/60 * * * *"
            },
            "dca": {
                "amount_usd": 10,
                "schedule": None
            }
        },
        "ETH": {
            "btd": {
                "dip_price": 3000,
                "amount_usd": 10,
                "smallest_unit": 8,
                "schedule": "*/30 * * * *"
            },
            "dca": {
                "amount_usd": 100,
                "schedule": "0 5 * * 1"
            }
        },
        "FORTH": {
            "btd": {
                "dip_price": 19.20,
                "amount_usd": 5,
                "smallest_unit": 3,
                "schedule": "*/60 * * * *"
            },
            "dca": {
                "amount_usd": 10,
                "schedule": None
            }
        },
        "FIL": {
            "btd": {
                "dip_price": 70,
                "amount_usd": 5,
                "smallest_unit": 3,
                "schedule": "*/60 * * * *"
            },
            "dca": {
                "amount_usd": 10,
                "schedule": None
            }
        },
        "GRT": {
            "btd": {
                "dip_price": 0.82,
                "amount_usd": 5,
                "smallest_unit": 1,
                "schedule": "*/60 * * * *"
            },
            "dca": {
                "amount_usd": 10,
                "schedule": None
            }
        },
        "ICP": {
            "btd": {
                "dip_price": 125,
                "amount_usd": 5,
                "smallest_unit": 4,
                "schedule": "*/60 * * * *"
            },
            "dca": {
                "amount_usd": 10,
                "schedule": None
            }
        },
        "KNC": {
            "btd": {
                "dip_price": 2,
                "amount_usd": 5,
                "smallest_unit": 1,
                "schedule": "*/60 * * * *"
            },
            "dca": {
                "amount_usd": 10,
                "schedule": None
            }
        },
        "LINK": {
            "btd": {
                "dip_price": 29,
                "amount_usd": 5,
                "smallest_unit": 8,
                "schedule": "*/60 * * * *"
            },
            "dca": {
                "amount_usd": 10,
                "schedule": None
            }
        },
        "LRC": {
            "btd": {
                "dip_price": 0.40,
                "amount_usd": 5,
                "smallest_unit": 6,
                "schedule": "*/60 * * * *"
            },
            "dca": {
                "amount_usd": 10,
                "schedule": None
            }
        },
        "MANA": {
            "btd": {
                "dip_price": 0.85,
                "amount_usd": 5,
                "smallest_unit": 2,
                "schedule": "*/60 * * * *"
            },
            "dca": {
                "amount_usd": 10,
                "schedule": None
            }
        },
        "MATIC": {
            "btd": {
                "dip_price": 1.65,
                "amount_usd": 5,
                "smallest_unit": 6,
                "schedule": "*/60 * * * *"
            },
            "dca": {
                "amount_usd": 10,
                "schedule": None
            }
        },
        "MIR": {
            "btd": {
                "dip_price": 6,
                "amount_usd": 5,
                "smallest_unit": 2,
                "schedule": "*/60 * * * *"
            },
            "dca": {
                "amount_usd": 10,
                "schedule": None
            }
        },
        "MKR": {
            "btd": {
                "dip_price": 3500,
                "amount_usd": 5,
                "smallest_unit": 8,
                "schedule": "*/60 * * * *"
            },
            "dca": {
                "amount_usd": 10,
                "schedule": None
            }
        },
        "NKN": {
            "btd": {
                "dip_price": 0.35,
                "amount_usd": 5,
                "smallest_unit": 1,
                "schedule": "*/60 * * * *"
            },
            "dca": {
                "amount_usd": 10,
                "schedule": None
            }
        },
        "NMR": {
            "btd": {
                "dip_price": 42,
                "amount_usd": 5,
                "smallest_unit": 3,
                "schedule": "*/60 * * * *"
            },
            "dca": {
                "amount_usd": 10,
                "schedule": None
            }
        },
        "NU": {
            "btd": {
                "dip_price": 0.30,
                "amount_usd": 5,
                "smallest_unit": 6,
                "schedule": "*/60 * * * *"
            },
            "dca": {
                "amount_usd": 10,
                "schedule": None
            }
        },
        "OGN": {
            "btd": {
                "dip_price": 70,
                "amount_usd": 5,
                "smallest_unit": 2,
                "schedule": "*/60 * * * *"
            },
            "dca": {
                "amount_usd": 10,
                "schedule": None
            }
        },
        "OMG": {
            "btd": {
                "dip_price": 5.60,
                "amount_usd": 5,
                "smallest_unit": 8,
                "schedule": "*/60 * * * *"
            },
            "dca": {
                "amount_usd": 10,
                "schedule": None
            }
        },
        "OXT": {
            "btd": {
                "dip_price": 0.30,
                "amount_usd": 5,
                "smallest_unit": 0,
                "schedule": "*/60 * * * *"
            },
            "dca": {
                "amount_usd": 10,
                "schedule": None
            }
        },
        "PAXG": {
            "btd": {
                "dip_price": 1800,
                "amount_usd": 5,
                "smallest_unit": 8,
                "schedule": "*/60 * * * *"
            },
            "dca": {
                "amount_usd": 10,
                "schedule": None
            }
        },
        "REN": {
            "btd": {
                "dip_price": 0.50,
                "amount_usd": 5,
                "smallest_unit": 6,
                "schedule": "*/60 * * * *"
            },
            "dca": {
                "amount_usd": 10,
                "schedule": None
            }
        },
        "REP": {
            "btd": {
                "dip_price": 25.50,
                "amount_usd": 5,
                "smallest_unit": 6,
                "schedule": "*/60 * * * *"
            },
            "dca": {
                "amount_usd": 10,
                "schedule": None
            }
        },
        "RLC": {
            "btd": {
                "dip_price": 4.80,
                "amount_usd": 5,
                "smallest_unit": 2,
                "schedule": "*/60 * * * *"
            },
            "dca": {
                "amount_usd": 10,
                "schedule": None
            }
        },
        "SAND": {
            "btd": {
                "dip_price": 0.28,
                "amount_usd": 5,
                "smallest_unit": 6,
                "schedule": "*/60 * * * *"
            },
            "dca": {
                "amount_usd": 10,
                "schedule": None
            }
        },
        "SKL": {
            "btd": {
                "dip_price": 0.35,
                "amount_usd": 5,
                "smallest_unit": 1,
                "schedule": "*/60 * * * *"
            },
            "dca": {
                "amount_usd": 10,
                "schedule": None
            }
        },
        "SNX": {
            "btd": {
                "dip_price": 14.90,
                "amount_usd": 5,
                "smallest_unit": 3,
                "schedule": "*/60 * * * *"
            },
            "dca": {
                "amount_usd": 10,
                "schedule": None
            }
        },
        "STORJ": {
            "btd": {
                "dip_price": 1.00,
                "amount_usd": 5,
                "smallest_unit": 2,
                "schedule": "*/60 * * * *"
            },
            "dca": {
                "amount_usd": 10,
                "schedule": None
            }
        },
        "SUSHI": {
            "btd": {
                "dip_price": 13.70,
                "amount_usd": 5,
                "smallest_unit": 8,
                "schedule": "*/60 * * * *"
            },
            "dca": {
                "amount_usd": 10,
                "schedule": None
            }
        },
        "TRB": {
            "btd": {
                "dip_price": 60,
                "amount_usd": 5,
                "smallest_unit": 3,
                "schedule": "*/60 * * * *"
            },
            "dca": {
                "amount_usd": 10,
                "schedule": None
            }
        },
        "UMA": {
            "btd": {
                "dip_price": 17,
                "amount_usd": 5,
                "smallest_unit": 8,
                "schedule": "*/60 * * * *"
            },
            "dca": {
                "amount_usd": 10,
                "schedule": None
            }
        },
        "UNI": {
            "btd": {
                "dip_price": 24,
                "amount_usd": 5,
                "smallest_unit": 8,
                "schedule": "*/60 * * * *"
            },
            "dca": {
                "amount_usd": 10,
                "schedule": None
            }
        },
        "WBTC": {
            "btd": {
                "dip_price": 45000,
                "amount_usd": 5,
                "smallest_unit": 8,
                "schedule": "*/60 * * * *"
            },
            "dca": {
                "amount_usd": 10,
                "schedule": None
            }
        },
        "XTZ": {
            "btd": {
                "dip_price": 3.75,
                "amount_usd": 5,
                "smallest_unit": 8,
                "schedule": "*/60 * * * *"
            },
            "dca": {
                "amount_usd": 10,
                "schedule": None
            }
        },
        "YFI": {
            "btd": {
                "dip_price": 46900,
                "amount_usd": 5,
                "smallest_unit": 8,
                "schedule": "*/60 * * * *"
            },
            "dca": {
                "amount_usd": 10,
                "schedule": None
            }
        },
        "ZEC": {
            "btd": {
            "dip_price": 175,
            "amount_usd": 5,
            "smallest_unit": 8,
            "schedule": "*/60 * * * *"
            },
            "dca": {
                "amount_usd": 10,
                "schedule": None
            }
        },
        "ZRX": {
            "btd": {
                "dip_price": 1,
                "amount_usd": 5,
                "smallest_unit": 5,
                "schedule": "*/60 * * * *"
            },
            "dca": {
                "amount_usd": 10,
                "schedule": None
            }
        }
    }

def get_btd_config(asset=None, param="dip_price"):
    """
    Get buy the dip config for a given asset
    """
    if asset is not None and asset in CF_CONFIG:
        return CF_CONFIG[asset.upper()]['btd'][param]

    return None

def get_dca_config(asset=None, param="amount_usd"):
    """
    Get dollar cost average config for a given asset
    """
    if asset is not None and asset in CF_CONFIG:
        return CF_CONFIG[asset.upper()]['dca'][param]

    return None
