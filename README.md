# Customer Platform

A system for managing customers and their purchased items, demonstrates distributed, data oriented design.

<img width="735" alt="Screenshot 2023-03-12 at 0 14 05" src="https://user-images.githubusercontent.com/44731477/224513743-bd497786-4e79-426b-8dc4-cd9e28a03d9e.png">


** In the actual configuration some services that should be private are currently exposed to the host machine
for debugging purposes

## These are the main components of the platform:

- `customer-bff-service` - A client-facing web server, serves a specfiic 
    frontend, for example a mobile application. It exposes a REST API and is a Kafka Producer.
    When deployed, this service is reachable from outside the container network on port 5000.

- `customer-management-service` - The system's core service, manages the entities of the system in a relational database using SQLAlchemy. It exposes an internal REST API, interacts with the database using SQLAlchemy ORM and consumes messages from "purchases" topic. In dev stage, the service seeds it's own data for testing purposes.
    When deployed, it is not exposed to requests from outside the container network.

- `Kafka Broker` - A Pub-Sub system messaging system for data streaming, processing and async communication.
- `Zookeeper` - Provides state management for Kafka
- `CustomerDB` - PostgreSQL
- `Airflow` - A task management platform for developing, scheduling and monitoring batch-oriented workflows.
    Deployed separately from the other components (as it consists of 7 containers). loads a "calc_total_spent" DAG that periodically updates the database with customers' total spent sum.
- `Grafana` - A monitoring platform for datasources. Displays the calculated data from `customer_total_spent`
- `customer-frontend` - A simple react application that allows for purchasing and viewing purchased items, deployed
    independently.

## Deployment
To Deploy the platoform, only docker is required:

1. Clone this repository
2. Create a bridge network is required for communication with airflow later on:
```
docker network create customer-airflow-bridge
```

3. Run the docker-compose file (DOCKER_DEFAULT_PLATFORM is set to amd64 in case you're running an ARM CPU):

```
DOCKER_DEFAULT_PLATFORM=linux/amd64 docker-compose up -d --build
```
<img width="435" alt="Screenshot 2023-03-11 at 11 39 44" src="https://user-images.githubusercontent.com/44731477/224477143-5a109e9e-b5d7-4961-9c23-980695c2f1c0.png">

<img width="1029" alt="Screenshot 2023-03-11 at 11 39 56" src="https://user-images.githubusercontent.com/44731477/224477164-44d7545a-bef2-4be7-8ed1-9b5a1281b9a4.png">


If you wish to deploy the services independently:

`customer-bff-service` - https://github.com/Tavh/customer-platform/blob/main/customer-bff-service/README.md

`customer-management-service` - https://github.com/Tavh/customer-platform/blob/main/customer-management-service/README.md


## Performing requests:

There should already be prepared data in the database because of the seeder in 'customer-management-service'

Fetching a customer's purchases:
```
curl -X GET http://localhost:5000/customers/1/purchases
```
<img width="638" alt="Screenshot 2023-03-12 at 0 04 56" src="https://user-images.githubusercontent.com/44731477/224513461-ee3aa1ba-7448-4a8b-9987-e0a13179074f.png">

Making a purchase
```
curl -X POST http://localhost:5000/customers/1/purchase/1
```
<img width="643" alt="Screenshot 2023-03-12 at 0 05 10" src="https://user-images.githubusercontent.com/44731477/224513466-d40a1178-6e17-4536-aab5-a6dd4899958d.png">


By inspecting the logs in customer-management-service, we can see that the message was succesfully consumed
and a purhcase record was inserted to the database:

```
docker-compose logs customer-management-service
```

<img width="836" alt="Screenshot 2023-03-11 at 11 48 00" src="https://user-images.githubusercontent.com/44731477/224477389-9cdccffa-c731-4111-89f1-f3c033c85096.png">


<img width="778" alt="Screenshot 2023-03-11 at 11 46 56" src="https://user-images.githubusercontent.com/44731477/224477386-7d2e8bbf-92f7-4be6-9942-00b7048c13f1.png">


## Airflow:

<img width="1495" alt="Screenshot 2023-03-11 at 19 51 34" src="https://user-images.githubusercontent.com/44731477/224504001-a61333c8-378e-4c96-9fbf-f6ea440c4f19.png">

Airflow is deployed with a different docker-compose, for instructions, go to:
https://github.com/Tavh/customer-platform/blob/main/airflow/README.md

## Grafana
<img width="745" alt="Screenshot 2023-03-11 at 18 25 52" src="https://user-images.githubusercontent.com/44731477/224504008-3a5f27f9-2f73-4a43-8286-9009af1d8d14.png">

Grafana is deployed with the main docker-compose, but the datasource and dashboard are configured
separately, reffer to:

https://github.com/Tavh/customer-platform/blob/main/grafana/README.md

## Frontend
 <img width="1172" alt="Screenshot 2023-03-11 at 19 46 46" src="https://user-images.githubusercontent.com/44731477/224504017-d8d08e06-9fd6-4cb5-8f5a-f21fea647262.png">

The frontend is a simple react app, for guidance go to:
https://github.com/Tavh/customer-platform/blob/main/customer-frontend/README.md
