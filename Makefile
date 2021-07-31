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
	.env/bin/pylint --init-hook='import sys; sys.path.append("dags/")' btd_template.py
	.env/bin/pylint --init-hook='import sys; sys.path.append("dags/")' dca_template.py
	.env/bin/pylint dags/check_orders.py
	.env/bin/pylint dags/cryptoflow/__init__.py
	.env/bin/pylint dags/cryptoflow/buyatmarket.py
	.env/bin/pylint dags/cryptoflow/buythedip.py
	.env/bin/pylint dags/cryptoflow/config.py
	.env/bin/pylint dags/cryptoflow/slack.py
	
dags:
	cp -R dags/cryptoflow ~/airflow/dags/
	cp dags/*.py ~/airflow/dags/
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
