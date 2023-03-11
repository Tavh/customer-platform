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

datasource_config = {
    "name": "Customers DB",
    "type": "postgres",
    "access": "proxy",
    "url": "db:5432",
    "database": "customers",
    "user": "postgres",
    "password": "postgres"
}

# Define dashboard config with datasource
dashboard_config = {
    "dashboard": {
        "id": None,
        "uid": None,
        "title": "Customer Data",
        "timezone": "browser",
        "schemaVersion": 22,
        "version": 0,
        "refresh": "10s",
        "panels": [
            {
                "type": "table",
                "title": "Customer Total Spent",
                "datasource": {
                    "uid": "cSbkpFaVz",
                    "type": "postgres"
                },
                "gridPos": {
                    "x": 0,
                    "y": 0,
                    "w": 12,
                    "h": 8
                },
                "id": 3,
                "targets": [
                    {
                        "datasource": {
                            "type": "postgres",
                            "uid": "cSbkpFaVz"
                        },
                        "refId": "A",
                        "format": "table",
                        "rawSql": "SELECT customer_id, total_spent FROM customer_total_spent LIMIT 50 ",
                        "editorMode": "builder",
                        "sql": {
                            "columns": [
                                {
                                    "type": "function",
                                    "parameters": [
                                        {
                                            "type": "functionParameter",
                                            "name": "customer_id"
                                        }
                                    ]
                                },
                                {
                                    "type": "function",
                                    "parameters": [
                                        {
                                            "type": "functionParameter",
                                            "name": "total_spent"
                                        }
                                    ]
                                }
                            ],
                            "groupBy": [
                                {
                                    "type": "groupBy",
                                    "property": {
                                        "type": "string"
                                    }
                                }
                            ],
                            "limit": 50
                        },
                        "table": "customer_total_spent"
                    }
                ],
                "options": {
                    "showHeader": True,
                    "footer": {
                        "show": False,
                        "reducer": [
                            "sum"
                        ],
                        "countRows": False,
                        "fields": ""
                    }
                },
                "fieldConfig": {
                    "defaults": {
                        "custom": {
                            "align": "auto",
                            "cellOptions": {
                                "type": "auto"
                            },
                            "inspect": False
                        },
                        "mappings": [],
                        "thresholds": {
                            "mode": "absolute",
                            "steps": [
                                {
                                    "value": None,
                                    "color": "green"
                                },
                                {
                                    "value": 80,
                                    "color": "red"
                                }
                            ]
                        },
                        "color": {
                            "mode": "thresholds"
                        }
                    },
                    "overrides": []
                },
                "pluginVersion": "9.4.3"
            }
        ]
    },
    "folderId": 0,
    "overwrite": False,
    "inputs": [
        {
            "name": "DS_CUSTDB",
            "type": "datasource",
            "pluginId": "postgres",
            "value": datasource_config["name"]
        }
    ]
}


# Create dashboard
dashboard_create_url = f'{grafana_url}/dashboards/db'
response = requests.post(dashboard_create_url, headers=grafana_headers, json=dashboard_config)
response.raise_for_status()
print(f'Created Grafana dashboard: {response.json()["slug"]}')



