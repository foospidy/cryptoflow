"""
Cryptoflow Dollar Cost Averaging DAG
"""
import os
import sys
from datetime import timedelta

from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.utils.dates import days_ago

from cryptoflow.buyatmarket import BuyAtMarket
from cryptoflow.config import get_dca_config


ASSET = os.path.basename(__file__).replace("dca_", "").replace(".py", "").upper()
AMOUNT_USD = get_dca_config(ASSET, 'amount_usd')
SCHEDULE = get_dca_config(ASSET, 'schedule')

args = {
    'owner': 'airflow',
}

dag = DAG(
    dag_id='dca_{}'.format(ASSET.lower()),
    default_args=args,
    schedule_interval="*/60 * * * *",
    start_date=days_ago(0),
    catchup=False,
    dagrun_timeout=timedelta(minutes=1),
    tags=['crypto', 'dollar_cost_average'],
    params={
        "amount_usd": "5"
    }
)

# [START dollar_cost_average]
def do_dollar_cost_average():
    """ Do dollar cost average buys """

    return_message = None
    buymarket = BuyAtMarket(ASSET, AMOUNT_USD)
    best_price = buymarket.get_best_price()

    print("BUY, HODL, BUY, HODL, BUY, HODL!!!")
    response = buymarket.buy_market(best_price, AMOUNT_USD)

    if response['success']:
        return_message = response['message']
    else:
        print(response['message'])
        sys.exit(1)

    return "Order placed: {}".format(return_message)

dollar_cost_average = PythonOperator(
    task_id='dollar_cost_average',
    python_callable=do_dollar_cost_average,
    op_kwargs={ "amount_usd": "5" },
    dag=dag,
)
# [END dollar_cost_average]
