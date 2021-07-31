"""
Generate btd and dca files from config
"""

import sys
import shutil
import json
sys.path.append("dags/")

from cryptoflow.default_config import DEFAULT_CF_CONFIG
from cryptoflow.default_config import AF_VARIABLES


for ticker in DEFAULT_CF_CONFIG:
    # create btd file for ticker
    shutil.copyfile('btd_template.py', 'dags/btd_{}.py'.format(ticker.lower()))
    # create dca file for ticker
    shutil.copyfile('dca_template.py', 'dags/dca_{}.py'.format(ticker.lower()))

# update variables_example.json
with open('variables_example.json', 'w') as variables_json:
    variables_json.write(json.dumps(AF_VARIABLES, indent=4))
