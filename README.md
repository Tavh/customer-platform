# Customer Platform

A system for managing customers and their purchased items, demonstrates distributed, data oriented design.

## The platform contains the following components:

- `customer-bff-service` - A client-facing web server, follows the "BFF" architectural style, serves a dedicated 
frontend, for example a mobile application. It exposes a REST API and is a Kafka Producer.

- `customer-management-service` - The system's core service, manages the entities of the system in a relational database.
It exposes a REST API, interacts with the database using SQLAlchemy ORM and consumes topics from Kafka.
In dev stage, the service seeds it's own data for testing purposes

- `Kafka Broker` - A Pub-Sub system messaging system for data streaming, processing and async communication.
- `Zookeeper` - Provides state management for Kafka
- `PostgreSQL` - A Powerful Relational database

To Deploy the platoform, only docker is required:

1. Clone this repository with it's submodules
2. Navigate to /docker-compose
3. If you're running an ARM CPU, run:
```
export DOCKER_DEFAULT_PLATFORM=linux/amd64
```
4. Run the following command


```
docker-compose up -d --build
```
<img width="435" alt="Screenshot 2023-03-11 at 11 39 44" src="https://user-images.githubusercontent.com/44731477/224477143-5a109e9e-b5d7-4961-9c23-980695c2f1c0.png">

<img width="1029" alt="Screenshot 2023-03-11 at 11 39 56" src="https://user-images.githubusercontent.com/44731477/224477164-44d7545a-bef2-4be7-8ed1-9b5a1281b9a4.png">


If you wish to deploy the services independently:

`customer-bff-service` - https://github.com/Tavh/customer-bff-service/blob/main/README.md

`customer-management-service` - https://github.com/Tavh/customer-management-service/blob/main/README.md


## Performing requests:

There should already be prepared data in the database because of the seeder in 'customer-management-service'

Fetching a customer's purchases:
```
curl -X GET http://localhost:6000/customers/1/purchases
```
<img width="639" alt="Screenshot 2023-03-11 at 11 40 37" src="https://user-images.githubusercontent.com/44731477/224477191-cf6be8ef-a376-4e3d-b7db-e9a1c0919862.png">

Making a purchase
```
curl -X POST http://localhost:6000/customers/1/purchase/1
```
<img width="653" alt="Screenshot 2023-03-11 at 11 40 20" src="https://user-images.githubusercontent.com/44731477/224477242-1abb6990-5670-4ea7-8117-09a5c88927b5.png">

By inspecting the logs in customer-management-service, we can see that the message was succesfully consumed
and a purhcase record was inserted to the database:

```
docker-compose logs customer-management-service
```

<img width="836" alt="Screenshot 2023-03-11 at 11 48 00" src="https://user-images.githubusercontent.com/44731477/224477389-9cdccffa-c731-4111-89f1-f3c033c85096.png">


<img width="778" alt="Screenshot 2023-03-11 at 11 46 56" src="https://user-images.githubusercontent.com/44731477/224477386-7d2e8bbf-92f7-4be6-9942-00b7048c13f1.png">


