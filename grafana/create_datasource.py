import requests
import os

# Grafana API endpoint
grafana_url = 'http://localhost:3000/api'

# Get API key from environment variable
grafana_api_key = os.environ.get('GRAFANA_API_KEY')

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


# Grafana headers with API key
grafana_headers = {
    'Authorization': f'Bearer {grafana_api_key}',
    'Content-Type': 'application/json'
}

# Delete existing Grafana datasource
datasource_name = datasource_config['name']
datasources_url = f'{grafana_url}/datasources'
response = requests.get(datasources_url, headers=grafana_headers)
for datasource in response.json():
    if datasource['name'] == datasource_name:
        datasource_uid = datasource['uid']
        datasource_delete_url = f'{datasources_url}/uid/{datasource_uid}'
        requests.delete(datasource_delete_url, headers=grafana_headers)
        print(f'Deleted existing Grafana datasource: {datasource_name}')
        break

# # Create Grafana datasource
# response = requests.post(datasources_url, headers=grafana_headers, json=datasource_config)
# response.raise_for_status()
# print(f'Created Grafana datasource: {response.json()["name"]}')
