# Grafana

The grafana server and management db should already be deployed by following the instructions under:
https://github.com/Tavh/customer-platform/blob/main/README.md

To add a Grafana datasource to the customers DB, follow these steps:

1. In your browser, go to: http://localhost:3000

2. Enter the default credentials: (username: admin, password: admin)
<img width="641" alt="Screenshot 2023-03-11 at 17 06 16" src="https://user-images.githubusercontent.com/44731477/224492051-8eb9eaa0-88e9-477b-bc05-6872198740e8.png">

3. Skip setting new credentials:
<img width="547" alt="Screenshot 2023-03-11 at 17 08 54" src="https://user-images.githubusercontent.com/44731477/224492081-aa3ac352-a7b2-4b26-99c6-49ce2c0ba83e.png">

4. Navigate to configuration -> API Keys:

<img width="458" alt="Screenshot 2023-03-11 at 17 29 03" src="https://user-images.githubusercontent.com/44731477/224493087-f4ae0a1c-7402-4197-b674-1851a03d0177.png">

5. Create a new API Key with administration privileges
<img width="880" alt="Screenshot 2023-03-11 at 17 29 25" src="https://user-images.githubusercontent.com/44731477/224493144-d19d3850-ada3-421b-bc31-b9ffcf06affb.png">

6. Copy the key:
<img width="828" alt="Screenshot 2023-03-11 at 17 31 02" src="https://user-images.githubusercontent.com/44731477/224493172-2f26fada-f088-42ca-ba00-1c9336e0da27.png">

7. Under /grafana, run:
```
GRAFANA_API_KEY=<copied api key> python create_datasource.py
```

8. Navigate to datasources:
<img width="303" alt="Screenshot 2023-03-11 at 17 33 14" src="https://user-images.githubusercontent.com/44731477/224493339-a4d99ee5-21d2-45df-b520-9a9cb26c523f.png">

9. Enter the created datasource configuration: 
<img width="629" alt="Screenshot 2023-03-11 at 17 33 26" src="https://user-images.githubusercontent.com/44731477/224493355-fc45a34b-994f-49ab-a52e-0ddf5c82a5a7.png">

11. The postgres server we deployed doesn't enable SSL, the only way to disable SSL/TLS mode in Grafana appears to be manually:
<img width="553" alt="Screenshot 2023-03-11 at 17 35 23" src="https://user-images.githubusercontent.com/44731477/224493466-8883a508-e5e4-46ff-95c5-aa7787367560.png">

12. Click on "Save & Test" to finish the datasource creation:
<img width="471" alt="Screenshot 2023-03-11 at 17 38 26" src="https://user-images.githubusercontent.com/44731477/224493569-83f543c9-855e-42c6-9e19-5eec113a2e67.png">


13. To create a panel that displays customers and their total spent sum, run the create_dashboard.py script under /grafana:
```
GRAFANA_API_KEY=<copied api key> python create_dashboard.py
```

Now, navigate to dashboards -> Customer Data to view the panel:

<img width="252" alt="Screenshot 2023-03-11 at 18 25 41" src="https://user-images.githubusercontent.com/44731477/224495905-ca16cc4a-8fca-4ec7-9ff1-21e76e8e77a8.png">

<img width="549" alt="Screenshot 2023-03-11 at 18 25 46" src="https://user-images.githubusercontent.com/44731477/224495906-5d53d56b-c6ec-4820-a3e4-7867cae3843b.png">

<img width="745" alt="Screenshot 2023-03-11 at 18 25 52" src="https://user-images.githubusercontent.com/44731477/224495908-d6703955-959f-4429-ac58-caa384a960ed.png">



  
