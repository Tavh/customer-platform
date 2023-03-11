# Customer Management Service

An application for managing purchases made by customers.

## Getting Started

This module depends on an available and a Kafka Broker.
A docker-compose that deploys the entire system is available at: https://github.com/Tavh/customer-platform

To run this application locally:
1. Navigate to root (/customer-bff-service)
2. Run and install venv:
```
python3 -m venv venv
source venv/bin/activate
python3 -m pip install --upgrade pip
pip install -r requirements.txt
```
3. Make sure there is a running and available kafka broker
4. Run the following command (If needed, edit this command in Makefile):

```
make run-local
```

## Configuration

Requires the following env variables:

`BOOTSTRAP_SERVERS` = list of kafka broker strings (standard kafka format)
`TOPIC` = a kafka topic to produce to

## API Endpoints

The following API endpoints are available:

- `GET /customers/{customer_id}/purchases`: Returns a list of purchases made by the customer.
