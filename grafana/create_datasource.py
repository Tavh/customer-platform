import requests
import os

# Grafana API endpoint
grafana_url = 'http://localhost:3000/api'

# Get API key from environment variable
grafana_api_key = os.environ.get('GRAFANA_API_KEY')

# Grafana headers with API key
grafana_headers = {
    'Authorization': f'Bearer {grafana_api_key}',
    'Content-Type': 'application/json'
}

# Postgres datasource config
datasource_config = {
    "name": "Customers DB",
    "type": "postgres",
    "access": "proxy",
    "url": "db:5432",
    "database": "customers",
    "user": "postgres",
    "password": "postgres"
}


# Delete existing Grafana datasource
datasource_name = datasource_config['name']
datasources_url = f'{grafana_url}/datasources'


# Create Grafana datasource
response = requests.post(datasources_url, headers=grafana_headers, json=datasource_config)
response.raise_for_status()
print(f'Created Grafana datasource: {response.json()["name"]}')
