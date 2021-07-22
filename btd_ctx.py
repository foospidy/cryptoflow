"""
Cryptoflow Buy The Dip DAG
To add a new coin, copy this DAG and rename with the format:
btd_<coin symbol>.py

If the price is not below the configured dip price, the buy_the_dip
task will finish with the "skipped" status.

If the price is below the dip price, the not_dip task will finish
with the "skipped" status.

Anytime the buy_the_dip task ends up with the "failed" status, this
will be due to insufficient funds or some other API error. Please
report any issues.
"""
import os
import sys
from datetime import timedelta

import airflow
from airflow.models import DAG
from airflow.operators.python import PythonOperator
from airflow.operators.python import BranchPythonOperator
from airflow.operators.dummy import DummyOperator
from airflow.utils.dates import days_ago

from cryptoflow.buythedip import BuyTheDip
from cryptoflow.config import get_btd_config


ASSET = os.path.basename(__file__).replace("btd_", "").replace(".py", "").upper()
DIP_PRICE = get_btd_config(ASSET, 'dip_price')
AMOUNT_USD = get_btd_config(ASSET, 'amount_usd')
SMALLEST_UNIT = get_btd_config(ASSET, 'smallest_unit')
SCHEDULE = get_btd_config(ASSET, 'schedule')
START_DATE = airflow.utils.dates.days_ago(1)

default_args = {
    'owner': 'cryptoflow',
}

dag = DAG(
    dag_id='btd_{}'.format(ASSET.lower()),
    default_args=default_args,
    schedule_interval=SCHEDULE,
    start_date=START_DATE,
    catchup=False,
    dagrun_timeout=timedelta(minutes=1),
    tags=['crypto', 'buy_the_dip'],
    params={
        "dip_price": "0",
        "amount_usd": "5"
    }
)

# [START is_dip]
def do_is_dip(**kwargs):
    """ Check if price has dipped """
    task_instance = kwargs['ti']
    next_task = 'not_dip'

    # pylint: disable=bare-except
    try:
        dip_price = float(kwargs['dag_run'].conf['dip_price'])
    except:
        dip_price = float(kwargs['dip_price'])

    print("DIP PRICE:\t{}".format(dip_price))

    buydip = BuyTheDip(ASSET)
    best_price = buydip.get_best_price()

    if best_price['price'] <= dip_price:
        print("BUY, HODL, BUY, HODL, BUY, HODL!!!")
        task_instance.xcom_push(key='best_price', value=best_price)
        next_task = 'buy_the_dip'

    return next_task

is_dip = BranchPythonOperator(
    task_id='is_dip',
    python_callable=do_is_dip,
    op_kwargs={ "dip_price": DIP_PRICE },
    dag=dag,
)
# [END is_dip]

# [START buy_the_dip]
def do_buy_the_dip(**kwargs):
    """ Buy the dip! """
    task_instance = kwargs['ti']
    best_price = task_instance.xcom_pull(key='best_price')

    # pylint: disable=bare-except
    try:
        spend = float(kwargs['dag_run'].conf['amount_usd'])
    except:
        spend = float(kwargs['amount_usd'])

    buydip = BuyTheDip(ASSET)
    response = buydip.buy_dip(best_price, spend, SMALLEST_UNIT)

    if not response['success']:
        if response['message'] == "Insufficient funds":
            # Insufficient funds on coinbasepro, so let's
            # try to get the same price on gemini.
            print("Insufficient funds on coinbasepro, trying gemini...")
            best_price['exchange'] = "gemini"
            response = buydip.buy_dip(best_price, spend, SMALLEST_UNIT)
        
        if not response['success']:
            print(response['message'])
            sys.exit(1)

    return response['message']

buy_the_dip = PythonOperator(
    task_id='buy_the_dip',
    python_callable=do_buy_the_dip,
    op_kwargs={ "dip_price": "0", "amount_usd": "5" },
    dag=dag,
)
# [END buy_the_dip]

not_dip = DummyOperator(
    task_id='not_dip'
)

# pylint: disable=pointless-statement
is_dip >> [not_dip, buy_the_dip]
