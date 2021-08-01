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

1. Fork this repo.
2. Create an entry to the DEFAULT_CF_CONFIG dictionary for each new coin you want to add.
3. Run `make generate`.
4. Submit a pull request.

DEFAULT_CF_CONFIG dictionary: https://github.com/foospidy/cryptoflow/blob/main/dags/cryptoflow/default_config.py#L4

Example entry:

```
"BTC": {
        "btd": {
            "amount_usd": 5,
            "dip_price": 33000,
            "schedule": "*/60 * * * *",
            "smallest_unit": 8
        },
        "dca": {
            "amount_usd": 10,
            "schedule": "0 5 * * 1"
        }
    },
```
