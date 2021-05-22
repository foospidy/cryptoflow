# cryptoflow

Crypto Flow - Airflow tasks for buying the dip and dollar cost averaging

## Quick Start

Assumed you can setup your own Apache Airflow environment.

1. Install Apache Airflow
2. Copy Cryptoflow files to your dags folder (run or see `make dags` command in Makefile)
3. Configure variables

## Configuration

See variables_example.json for example configuration.

### Configure Exchanges

To configure an exchange, simply add Airflow varibles for your exchange API keys.

Currently supported exchanges are:

#### Coinbase Pro

- COINBASEPRO_KEY
- COINBASEPRO_PASSPHRASE
- COINBASEPRO_SECRET

#### Gemini

- GEMINI_KEY
- GEMINI_SECRET

### Configure Slack Webhook

- CRYPTOFLOW_SLACK_WEBHOOK

### Configuring Cryptoflow

If you added the CRYPTOFLOW_CONFIG variable you can adjust buy options there. Alternatively, you can update the buy options in `cryptoflow/config.py`. 

## Adding New Coins

There are two types of DAGs:

- Buy The Dip: btd_\<ticker\>.py
- Dollar Cost Average: dca_\<ticker\>.py

To add a new coin DAG, copy an existing DAG (btd or dca) and rename it with the coin ticker.
