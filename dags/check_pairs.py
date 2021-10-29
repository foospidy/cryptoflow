"""
Cryptoflow Check Pairs DAG
Checks if a new crypto currency pair exists.
"""

from datetime import timedelta

import cbpro
import gemini

from airflow.models import DAG
from airflow.models import Variable
from airflow.operators.python import PythonOperator
from airflow.utils.dates import days_ago

from cryptoflow.default_config import DEFAULT_CF_CONFIG
from cryptoflow.slack import slack_webhook


START_DATE = days_ago(1)

default_args = {
    'owner': 'cryptoflow',
}

dag = DAG(
    dag_id='btd_check_pairs',
    default_args=default_args,
    schedule_interval="0 * * * *",
    start_date=START_DATE,
    catchup=False,
    dagrun_timeout=timedelta(minutes=1),
    tags=['crypto', 'check', 'pairs'],
    params={}
)

# [START check_orders]
def do_check_pairs():
    """
    Check for new crypto pairs, post update to slack if slack webhook is configured
    """
    # Check coinbasepro pairs
    coinbasepro = cbpro.AuthenticatedClient(Variable.get('COINBASEPRO_KEY'),
                                                         Variable.get('COINBASEPRO_SECRET'),
                                                         Variable.get('COINBASEPRO_PASSPHRASE'))

    pairs = coinbasepro.get_products()

    for pair in pairs:
        if pair["base_currency"] not in DEFAULT_CF_CONFIG:
            msg = f"{pair['base_currency']} ({pair['base_min_size']}) is on coinbasepro "
            msg += "but not in config, add support!"
            print(msg)
            slack_webhook(text=msg)

    # Check gemini pairs
    gemini_client = gemini.PrivateClient(Variable.get('GEMINI_KEY'),
                                                      Variable.get('GEMINI_SECRET'))
    
    pairs = gemini_client.symbols()

    for pair in pairs:
        if pair.endswith("usd"):
            symbol = pair.replace("usd", "").upper()
            if symbol not in DEFAULT_CF_CONFIG:
                msg = f"{symbol} is on gemini but not in config, add support!"
                print(msg)
                slack_webhook(text=msg)

    return "Crypto pairs check completed."

check_pairs = PythonOperator(
    task_id='check_pairs',
    python_callable=do_check_pairs,
    dag=dag,
)
# [END check_orders]

if __name__ == "__main__":
    dag.cli()
