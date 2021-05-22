env:
	python3 -m venv .env
	.env/bin/python3 -m pip install --upgrade pip
	.env/bin/pip install apache-airflow
	.env/bin/pip install mysqlclient
	.env/bin/pip install cbpro
	.env/bin/pip install gemini_python
	.env/bin/pip install pylint

clean:
	rm -rf .env

lint:
	pylint btd_btc.py
	pylint dca_btc.py
	pylint check_orders.py
	pylint cryptoflow/__init__.py
	pylint cryptoflow/bittrex.py
	pylint cryptoflow/buyatmarket.py
	pylint cryptoflow/buythedip.py
	pylint cryptoflow/config.py
	pylint cryptoflow/slack.py
	
dags:
	cp -R cryptoflow ~/airflow/dags/
	cp *.py ~/airflow/dags/
	~/airflow/.env/bin/python -c "from airflow.models import DagBag; d = DagBag();"

install-airflow:
	mkdir ~/airflow
	cd ~/airflow
	python3 -m venv .env
	.env/bin/python3 -m pip install --upgrade pip
	.env/bin/pip install apache-airflow
	.env/bin/pip install mysqlclient
	.env/bin/pip install cbpro
	.env/bin/pip install gemini_python
