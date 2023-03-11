install: 
	pip install -r requirements.txt

test: 
	python -m unittest discover -s database -p '*_test.py'

run-local: 
	BOOTSTRAP_SERVERS=localhost:29092 DATABASE_URL=postgresql://postgres:postgres@localhost:5431/customers TOPIC=purchases STAGE=dev FLASK_APP=main.py flask run --port=5000