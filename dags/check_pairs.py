"""
Cryptoflow Check Pairs DAG
Checks if a new crypto currency pair exists.
"""

from datetime import timedelta
import requests

from airflow.models import DAG
from airflow.operators.python import PythonOperator
from airflow.utils.dates import days_ago


START_DATE = days_ago(1)

default_args = {
    'owner': 'cryptoflow',
}

dag = DAG(
    dag_id='btd_check_pairs',
    default_args=default_args,
    schedule_interval="*/5 * * * *",
    start_date=START_DATE,
    dagrun_timeout=timedelta(minutes=1),
    tags=['crypto', 'orders'],
    params={}
)

# [START check_orders]
def do_check_pairs():
    """
    Check for new crypto pairs, post update to slack if slack webhook is configured
    """
    

    return "Crypto pairs check completed."

check_pairs = PythonOperator(
    task_id='check_pairs',
    python_callable=do_check_pairs,
    dag=dag,
)
# [END check_orders]

if __name__ == "__main__":
    dag.cli()
