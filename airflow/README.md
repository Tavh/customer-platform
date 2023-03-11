# Airflow

This module deployds a full airflow eco-system, and adds a DAG that
enriches customer-platform data

To deploy airflow, follow these steps:


1. Prepare the DAG dependencies bhy running under /dags:
```
python3 -m venv venv
source venv/bin/activate
python3 -m pip install --upgrade pip
pip install -r requirements.txt
```
2. Make sure a "bridge" network exists to link between customer DB and airflow:
```
docker network create customer-airflow-bridge
``` 
3. Run the customer-platform, instructions are at: 
https://github.com/Tavh/customer-platform/blob/main/README.md

4. Run the airflow docker-compose in this repo's root
```
docker-compose up -d
```
<img width="399" alt="Screenshot 2023-03-11 at 0 37 46" src="https://user-images.githubusercontent.com/44731477/224442019-c1813182-6e26-4c59-9fd5-d20e5a15065f.png">

5. To view logs run (in this repo's root):
```
docker-compose logs -f
```
<img width="690" alt="Screenshot 2023-03-11 at 0 38 02" src="https://user-images.githubusercontent.com/44731477/224442051-11b87f8b-b07e-46aa-9194-4b2f8494fd35.png">


5. Once the compose is done, fire up a browser and navigate to http://localhost:8080

6. Login by using the 'airflow' as both username and password

7. Search the "customer_total_spent" DAG

8. Toggle the DAG to activate:

<img width="1480" alt="Screenshot 2023-03-11 at 0 19 43" src="https://user-images.githubusercontent.com/44731477/224442075-37ac7f1e-3ecd-41a9-b5ad-1c4401afcef6.png">

9. This DAG writes into "customer_total_spent" table, to view the written data, open up a database viewing tool
    and run the following query:
```

SELECT customer_id, total_spent FROM customer_total_spent;

```
<img width="541" alt="Screenshot 2023-03-11 at 15 43 41" src="https://user-images.githubusercontent.com/44731477/224488139-c7b8f3a0-6a1f-4299-8abc-f74299b5fbb0.png">

