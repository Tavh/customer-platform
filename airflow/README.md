# Airflow

This module deployds a full airflow eco-system, and adds a DAG that
enriches customer-platform data

To deploy airflow, follow these steps:

1. Clone this repository
2. Make a "bridge" network between customer-platform and airflow:
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

7. Search the "user_total_spent" DAG

8. Toggle the DAG to activate:

<img width="1480" alt="Screenshot 2023-03-11 at 0 19 43" src="https://user-images.githubusercontent.com/44731477/224442075-37ac7f1e-3ecd-41a9-b5ad-1c4401afcef6.png">

9. This DAG writes into "user_total_spent" table, to view the written data, open up a database viewing tool
    and run the following query:
```

SELECT customer_id, total_spent FROM user_total_spent;
```

<img width="497" alt="Screenshot 2023-03-11 at 0 36 15" src="https://user-images.githubusercontent.com/44731477/224441110-0bdb8abc-2f16-4664-a2ef-5c8d84610cdf.png">
