"""
Slack helper module for Cryptoflow!
"""
import requests
from airflow.models import Variable


def slack_webhook(text=""):
    """ Send to slack if webhook configured """
    # pylint: disable=broad-except
    try:
        headers = { "Content-Type": "application/json" }
        data = { "text": text }
        response = requests.post(Variable.get("CRYPTOFLOW_SLACK_WEBHOOK"),
                                 headers=headers,
                                 json=data)
        print(f"Slack webhook sent: {response.status_code}")

    except Exception as err:
        print(f"slack_webhook Error: {err}")
