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
                "amount_usd": 5,
                "dip_price": 2.4,
                "schedule": "*/60 * * * *",
                "smallest_unit": 2
            },
            "dca": {
                "amount_usd": 10,
                "schedule": null
            }
        },
        "AAVE": {
            "btd": {
                "amount_usd": 5,
                "dip_price": 300,
                "schedule": "*/60 * * * *",
                "smallest_unit": 5
            },
            "dca": {
                "amount_usd": 10,
                "schedule": null
            }
        },
        "ADA": {
            "btd": {
                "amount_usd": 5,
                "dip_price": 1.3,
                "schedule": "*/60 * * * *",
                "smallest_unit": 2
            },
            "dca": {
                "amount_usd": 10,
                "schedule": "0 5 * * 1"
            }
        },
        "ALGO": {
            "btd": {
                "amount_usd": 5,
                "dip_price": 0.9,
                "schedule": "*/60 * * * *",
                "smallest_unit": 0
            },
            "dca": {
                "amount_usd": 10,
                "schedule": null
            }
        },
        "AMP": {
            "btd": {
                "amount_usd": 5,
                "dip_price": 0.05,
                "schedule": "*/60 * * * *",
                "smallest_unit": 6
            },
            "dca": {
                "amount_usd": 10,
                "schedule": null
            }
        },
        "ANKR": {
            "btd": {
                "amount_usd": 5,
                "dip_price": 0.07,
                "schedule": "*/60 * * * *",
                "smallest_unit": 0
            },
            "dca": {
                "amount_usd": 10,
                "schedule": null
            }
        },
        "ATOM": {
            "btd": {
                "amount_usd": 5,
                "dip_price": 14,
                "schedule": "*/60 * * * *",
                "smallest_unit": 8
            },
            "dca": {
                "amount_usd": 10,
                "schedule": null
            }
        },
        "BAL": {
            "btd": {
                "amount_usd": 5,
                "dip_price": 35,
                "schedule": "*/60 * * * *",
                "smallest_unit": 1
            },
            "dca": {
                "amount_usd": 10,
                "schedule": null
            }
        },
        "BAND": {
            "btd": {
                "amount_usd": 5,
                "dip_price": 9,
                "schedule": "*/60 * * * *",
                "smallest_unit": 2
            },
            "dca": {
                "amount_usd": 10,
                "schedule": null
            }
        },
        "BAT": {
            "btd": {
                "amount_usd": 5,
                "dip_price": 0.45,
                "schedule": "*/60 * * * *",
                "smallest_unit": 2
            },
            "dca": {
                "amount_usd": 10,
                "schedule": null
            }
        },
        "BCH": {
            "btd": {
                "amount_usd": 5,
                "dip_price": 475,
                "schedule": "*/60 * * * *",
                "smallest_unit": 8
            },
            "dca": {
                "amount_usd": 10,
                "schedule": null
            }
        },
        "BNT": {
            "btd": {
                "amount_usd": 5,
                "dip_price": 3,
                "schedule": "*/60 * * * *",
                "smallest_unit": 6
            },
            "dca": {
                "amount_usd": 10,
                "schedule": null
            }
        },
        "BOND": {
            "btd": {
                "amount_usd": 5,
                "dip_price": 27,
                "schedule": "*/60 * * * *",
                "smallest_unit": 3
            },
            "dca": {
                "amount_usd": 10,
                "schedule": null
            }
        },
        "BTC": {
            "btd": {
                "amount_usd": 5,
                "dip_price": 33000,
                "schedule": "*/60 * * * *",
                "smallest_unit": 8
            },
            "dca": {
                "amount_usd": 10,
                "schedule": "0 5 * * 1"
            }
        },
        "CGLD": {
            "btd": {
                "amount_usd": 5,
                "dip_price": 4.1,
                "schedule": "*/60 * * * *",
                "smallest_unit": 2
            },
            "dca": {
                "amount_usd": 10,
                "schedule": null
            }
        },
        "COMP": {
            "btd": {
                "amount_usd": 5,
                "dip_price": 490,
                "schedule": "*/60 * * * *",
                "smallest_unit": 3
            },
            "dca": {
                "amount_usd": 10,
                "schedule": null
            }
        },
        "CRV": {
            "btd": {
                "amount_usd": 5,
                "dip_price": 2,
                "schedule": "*/60 * * * *",
                "smallest_unit": 2
            },
            "dca": {
                "amount_usd": 10,
                "schedule": null
            }
        },
        "CTSI": {
            "btd": {
                "amount_usd": 5,
                "dip_price": 90,
                "schedule": "*/60 * * * *",
                "smallest_unit": 1
            },
            "dca": {
                "amount_usd": 10,
                "schedule": null
            }
        },
        "CTX": {
            "btd": {
                "amount_usd": 5,
                "dip_price": 5,
                "schedule": "*/60 * * * *",
                "smallest_unit": 8
            },
            "dca": {
                "amount_usd": 10,
                "schedule": null
            }
        },
        "CVC": {
            "btd": {
                "amount_usd": 5,
                "dip_price": 0.32,
                "schedule": "*/60 * * * *",
                "smallest_unit": 8
            },
            "dca": {
                "amount_usd": 10,
                "schedule": null
            }
        },
        "DAI": {
            "btd": {
                "amount_usd": 5,
                "dip_price": 0.9999,
                "schedule": "*/60 * * * *",
                "smallest_unit": 5
            },
            "dca": {
                "amount_usd": 10,
                "schedule": null
            }
        },
        "DASH": {
            "btd": {
                "amount_usd": 5,
                "dip_price": 150,
                "schedule": "*/60 * * * *",
                "smallest_unit": 3
            },
            "dca": {
                "amount_usd": 10,
                "schedule": null
            }
        },
        "DNT": {
            "btd": {
                "amount_usd": 5,
                "dip_price": 0.2,
                "schedule": "*/60 * * * *",
                "smallest_unit": 8
            },
            "dca": {
                "amount_usd": 10,
                "schedule": null
            }
        },
        "DOGE": {
            "btd": {
                "amount_usd": 5,
                "dip_price": 0.35,
                "schedule": "*/60 * * * *",
                "smallest_unit": 6
            },
            "dca": {
                "amount_usd": 10,
                "schedule": null
            }
        },
        "DOT": {
            "btd": {
                "amount_usd": 5,
                "dip_price": 15,
                "schedule": "*/60 * * * *",
                "smallest_unit": 3
            },
            "dca": {
                "amount_usd": 10,
                "schedule": null
            }
        },
        "ENJ": {
            "btd": {
                "amount_usd": 5,
                "dip_price": 1.25,
                "schedule": "*/60 * * * *",
                "smallest_unit": 2
            },
            "dca": {
                "amount_usd": 10,
                "schedule": null
            }
        },
        "EOS": {
            "btd": {
                "amount_usd": 5,
                "dip_price": 3.75,
                "schedule": "*/60 * * * *",
                "smallest_unit": 1
            },
            "dca": {
                "amount_usd": 10,
                "schedule": null
            }
        },
        "ETH": {
            "btd": {
                "amount_usd": 10,
                "dip_price": 2000,
                "schedule": "*/10 * * * *",
                "smallest_unit": 8
            },
            "dca": {
                "amount_usd": 100,
                "schedule": "0 5 * * 1"
            }
        },
        "FIL": {
            "btd": {
                "amount_usd": 5,
                "dip_price": 70,
                "schedule": "*/60 * * * *",
                "smallest_unit": 3
            },
            "dca": {
                "amount_usd": 10,
                "schedule": null
            }
        },
        "FORTH": {
            "btd": {
                "amount_usd": 5,
                "dip_price": 19.2,
                "schedule": "*/60 * * * *",
                "smallest_unit": 3
            },
            "dca": {
                "amount_usd": 10,
                "schedule": null
            }
        },
        "GRT": {
            "btd": {
                "amount_usd": 5,
                "dip_price": 0.82,
                "schedule": "*/60 * * * *",
                "smallest_unit": 1
            },
            "dca": {
                "amount_usd": 10,
                "schedule": null
            }
        },
        "ICP": {
            "btd": {
                "amount_usd": 5,
                "dip_price": 125,
                "schedule": "*/60 * * * *",
                "smallest_unit": 4
            },
            "dca": {
                "amount_usd": 10,
                "schedule": null
            }
        },
        "KNC": {
            "btd": {
                "amount_usd": 5,
                "dip_price": 2,
                "schedule": "*/60 * * * *",
                "smallest_unit": 1
            },
            "dca": {
                "amount_usd": 10,
                "schedule": null
            }
        },
        "LINK": {
            "btd": {
                "amount_usd": 5,
                "dip_price": 17.5,
                "schedule": "*/60 * * * *",
                "smallest_unit": 8
            },
            "dca": {
                "amount_usd": 10,
                "schedule": null
            }
        },
        "LRC": {
            "btd": {
                "amount_usd": 5,
                "dip_price": 0.4,
                "schedule": "*/60 * * * *",
                "smallest_unit": 6
            },
            "dca": {
                "amount_usd": 10,
                "schedule": null
            }
        },
        "MANA": {
            "btd": {
                "amount_usd": 5,
                "dip_price": 0.85,
                "schedule": "*/60 * * * *",
                "smallest_unit": 2
            },
            "dca": {
                "amount_usd": 10,
                "schedule": null
            }
        },
        "MATIC": {
            "btd": {
                "amount_usd": 15,
                "dip_price": 1,
                "schedule": "*/60 * * * *",
                "smallest_unit": 5
            },
            "dca": {
                "amount_usd": 10,
                "schedule": null
            }
        },
        "MIR": {
            "btd": {
                "amount_usd": 5,
                "dip_price": 3.45,
                "schedule": "*/60 * * * *",
                "smallest_unit": 2
            },
            "dca": {
                "amount_usd": 10,
                "schedule": null
            }
        },
        "MKR": {
            "btd": {
                "amount_usd": 5,
                "dip_price": 3500,
                "schedule": "*/60 * * * *",
                "smallest_unit": 6
            },
            "dca": {
                "amount_usd": 10,
                "schedule": null
            }
        },
        "NKN": {
            "btd": {
                "amount_usd": 5,
                "dip_price": 0.35,
                "schedule": "*/60 * * * *",
                "smallest_unit": 1
            },
            "dca": {
                "amount_usd": 10,
                "schedule": null
            }
        },
        "NMR": {
            "btd": {
                "amount_usd": 5,
                "dip_price": 42,
                "schedule": "*/60 * * * *",
                "smallest_unit": 3
            },
            "dca": {
                "amount_usd": 10,
                "schedule": null
            }
        },
        "NU": {
            "btd": {
                "amount_usd": 5,
                "dip_price": 0.3,
                "schedule": "*/60 * * * *",
                "smallest_unit": 6
            },
            "dca": {
                "amount_usd": 10,
                "schedule": null
            }
        },
        "OGN": {
            "btd": {
                "amount_usd": 5,
                "dip_price": 70,
                "schedule": "*/60 * * * *",
                "smallest_unit": 2
            },
            "dca": {
                "amount_usd": 10,
                "schedule": null
            }
        },
        "OMG": {
            "btd": {
                "amount_usd": 5,
                "dip_price": 5.6,
                "schedule": "*/60 * * * *",
                "smallest_unit": 8
            },
            "dca": {
                "amount_usd": 10,
                "schedule": null
            }
        },
        "OXT": {
            "btd": {
                "amount_usd": 5,
                "dip_price": 0.3,
                "schedule": "*/60 * * * *",
                "smallest_unit": 0
            },
            "dca": {
                "amount_usd": 10,
                "schedule": null
            }
        },
        "PAXG": {
            "btd": {
                "amount_usd": 5,
                "dip_price": 1800,
                "schedule": "*/60 * * * *",
                "smallest_unit": 8
            },
            "dca": {
                "amount_usd": 10,
                "schedule": null
            }
        },
        "REN": {
            "btd": {
                "amount_usd": 5,
                "dip_price": 0.5,
                "schedule": "*/60 * * * *",
                "smallest_unit": 6
            },
            "dca": {
                "amount_usd": 10,
                "schedule": null
            }
        },
        "REP": {
            "btd": {
                "amount_usd": 5,
                "dip_price": 25.5,
                "schedule": "*/60 * * * *",
                "smallest_unit": 6
            },
            "dca": {
                "amount_usd": 10,
                "schedule": null
            }
        },
        "RLC": {
            "btd": {
                "amount_usd": 5,
                "dip_price": 4.8,
                "schedule": "*/60 * * * *",
                "smallest_unit": 2
            },
            "dca": {
                "amount_usd": 10,
                "schedule": null
            }
        },
        "SAND": {
            "btd": {
                "amount_usd": 5,
                "dip_price": 0.28,
                "schedule": "*/60 * * * *",
                "smallest_unit": 6
            },
            "dca": {
                "amount_usd": 10,
                "schedule": null
            }
        },
        "SKL": {
            "btd": {
                "amount_usd": 5,
                "dip_price": 0.35,
                "schedule": "*/60 * * * *",
                "smallest_unit": 1
            },
            "dca": {
                "amount_usd": 10,
                "schedule": null
            }
        },
        "SNX": {
            "btd": {
                "amount_usd": 5,
                "dip_price": 14.9,
                "schedule": "*/60 * * * *",
                "smallest_unit": 3
            },
            "dca": {
                "amount_usd": 10,
                "schedule": null
            }
        },
        "SOL": {
            "btd": {
                "amount_usd": 5,
                "dip_price": 30,
                "schedule": "*/60 * * * *",
                "smallest_unit": 3
            },
            "dca": {
                "amount_usd": 10,
                "schedule": null
            }
        },
        "STORJ": {
            "btd": {
                "amount_usd": 5,
                "dip_price": 1.0,
                "schedule": "*/60 * * * *",
                "smallest_unit": 2
            },
            "dca": {
                "amount_usd": 10,
                "schedule": null
            }
        },
        "SUSHI": {
            "btd": {
                "amount_usd": 5,
                "dip_price": 13.7,
                "schedule": "*/60 * * * *",
                "smallest_unit": 2
            },
            "dca": {
                "amount_usd": 10,
                "schedule": null
            }
        },
        "TRB": {
            "btd": {
                "amount_usd": 5,
                "dip_price": 60,
                "schedule": "*/60 * * * *",
                "smallest_unit": 3
            },
            "dca": {
                "amount_usd": 10,
                "schedule": null
            }
        },
        "UMA": {
            "btd": {
                "amount_usd": 5,
                "dip_price": 17,
                "schedule": "*/60 * * * *",
                "smallest_unit": 3
            },
            "dca": {
                "amount_usd": 10,
                "schedule": null
            }
        },
        "UNI": {
            "btd": {
                "amount_usd": 5,
                "dip_price": 24,
                "schedule": "*/60 * * * *",
                "smallest_unit": 6
            },
            "dca": {
                "amount_usd": 10,
                "schedule": null
            }
        },
        "WBTC": {
            "btd": {
                "amount_usd": 5,
                "dip_price": 45000,
                "schedule": "*/60 * * * *",
                "smallest_unit": 8
            },
            "dca": {
                "amount_usd": 10,
                "schedule": null
            }
        },
        "XLM": {
            "btd": {
                "amount_usd": 5,
                "dip_price": 0.25,
                "schedule": "*/60 * * * *",
                "smallest_unit": 0
            },
            "dca": {
                "amount_usd": 10,
                "schedule": null
            }
        },
        "XTZ": {
            "btd": {
                "amount_usd": 5,
                "dip_price": 3.75,
                "schedule": "*/60 * * * *",
                "smallest_unit": 8
            },
            "dca": {
                "amount_usd": 10,
                "schedule": null
            }
        },
        "YFI": {
            "btd": {
                "amount_usd": 5,
                "dip_price": 30000,
                "schedule": "*/60 * * * *",
                "smallest_unit": 8
            },
            "dca": {
                "amount_usd": 10,
                "schedule": null
            }
        },
        "ZEC": {
            "btd": {
                "amount_usd": 5,
                "dip_price": 175,
                "schedule": "*/60 * * * *",
                "smallest_unit": 8
            },
            "dca": {
                "amount_usd": 10,
                "schedule": null
            }
        },
        "ZRX": {
            "btd": {
                "amount_usd": 5,
                "dip_price": 0.75,
                "schedule": "*/60 * * * *",
                "smallest_unit": 5
            },
            "dca": {
                "amount_usd": 10,
                "schedule": null
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
