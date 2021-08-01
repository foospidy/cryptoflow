"""
Config module for Cryptoflow!
"""
import json

from airflow.models import Variable

from cryptoflow.default_config import DEFAULT_CF_CONFIG


# pylint: disable=bare-except
try:
    CF_CONFIG = json.loads(Variable.get("CRYPTOFLOW_CONFIG"))
except:
    CF_CONFIG = DEFAULT_CF_CONFIG

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

def get_cf_config():
    """
    Return cryptoflow config
    """
    return CF_CONFIG

def configured_exchanges():
    """
    Return list of configured exchanges.
    """
    exchanges = []

    # pylint: disable=bare-except
    try:
        Variable.get("COINBASEPRO_KEY")
        exchanges.append("coinbasepro")
    except:
        pass

    # pylint: disable=bare-except
    try:
        Variable.get("GEMINI_KEY")
        exchanges.append("gemini")
    except:
        pass

    return exchanges
