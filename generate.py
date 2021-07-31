"""
Generate btd and dca files from config
"""

import sys
import shutil
import json
sys.path.append("dags/")

from cryptoflow.default_config import DEFAULT_CF_CONFIG

#print(json.dumps(DEFAULT_CF_CONFIG))

for ticker in DEFAULT_CF_CONFIG:
    print(ticker)
    # create btd file for ticker
    shutil.copyfile('btd_template.py', 'dags/btd_{}'.format(ticker.lower()))

