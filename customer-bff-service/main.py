import os
from flask import Flask
from kafka_producer.producer import KafkaPurchaseProducer
from api.rest_controller import RestController
from util.logger import get_logger

# Get configuration from environment variables
bootstrap_servers = os.environ['BOOTSTRAP_SERVERS']
topic = os.environ['TOPIC']
customer_management_url = os.environ['CUSTOMER_MANAGEMENT_URL']

logger = get_logger(__name__)

# Log the configuration
logger.info(f"Starting with config: bootstrap_servers={bootstrap_servers}, customer_management_url={customer_management_url} topic={topic}")

# Create a Flask app
app = Flask(__name__)

# Create a KafkaPurchaseProducer instance for producing purchase events to Kafka
producer = KafkaPurchaseProducer(bootstrap_servers=bootstrap_servers, topic=topic)

# Create a RestController instance to handle incoming HTTP requests
rest_controller = RestController(app=app, customer_management_url=customer_management_url, producer=producer)

# Register the REST endpoints with the RestController
rest_controller.register_endpoints()

if __name__ == "__main__":
    # Start the Flask app
    app.run(host='0.0.0.0', debug=True)
