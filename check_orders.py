"""
Cryptoflow Check Orders DAG
Checks if previously submitted orders have completed. A Slack
message will be posted for completed orders if Slack is configured.
"""

from datetime import timedelta

import airflow
from airflow.models import DAG
from airflow.operators.python import PythonOperator
from airflow.utils.dates import days_ago

from cryptoflow.buythedip import CheckOrders


default_args = {
    'owner': 'cryptoflow',
}

dag = DAG(
    dag_id='btd_check_orders',
    default_args=default_args,
    schedule_interval="*/5 * * * *",
    start_date=START_DATE,
    dagrun_timeout=timedelta(minutes=1),
    tags=['crypto', 'orders'],
    params={}
)

# [START check_orders]
def do_check_orders():
    """
    Check pending orders, post update to slack if slack webhook is configured
    """
    orders = CheckOrders()

    orders.check_status()

    return "Order status check completed."

check_orders = PythonOperator(
    task_id='check_orders',
    python_callable=do_check_orders,
    dag=dag,
)
# [END check_orders]

if __name__ == "__main__":
    dag.cli()
