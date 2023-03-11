from typing import List
from flask import Flask, jsonify
from kafka_producer.producer import KafkaPurchaseProducer
import requests
from util.logger import get_logger
from requests.exceptions import HTTPError
from models.models import Purchase


class RestController:
    def __init__(self, app: Flask, producer: KafkaPurchaseProducer, customer_management_url: str):
        """
        Initializes a new instance of the RestController class.

        Args:
            app (Flask): The Flask application instance.
            producer (KafkaPurchaseProducer): The KafkaPurchaseProducer instance to use for publishing purchase events.
        """
        self.app = app
        self.logger = get_logger(__name__)
        self.producer = producer
        self.customer_management_url = customer_management_url

        self.register_endpoints()

    def register_endpoints(self):
        """
        Registers the API endpoints for the RestController class.
        """
        self.app.route('/customers/<int:customer_id>/purchase/<int:item_id>', methods=['POST'])(self.purchase_item)
        self.app.route('/customers/<customer_id>/purchases', methods=['GET'])(self.get_customer_purchases)


    def purchase_item(self, customer_id, item_id):
        """
        Publishes a purchase event to Kafka.

        Args:
            customer_id (int): The ID of the customer making the purchase.
            item_id (int): The ID of the item being purchased.

        Returns:
            A JSON response indicating that the purchase event has been published to Kafka.
        """
        self.producer.publish_purchase(customer_id, item_id)
        return jsonify({"message": "Purchase registered successfully"})
    
    def get_customer_purchases(self, customer_id: int) -> List[Purchase]:
        """
        Gets the purchases made by the customer with the given ID.

        Args:
            customer_id (int): The ID of the customer.

        Returns:
            List[Purchase]: A list of purchase objects made by the customer.
        """
        url = f"{self.customer_management_url}/customers/{customer_id}/purchases"
        try:
            response = requests.get(url)
            response.raise_for_status()
            purchases = [Purchase(**p) for p in response.json()]
            return purchases
        except HTTPError as e:
            self.logger.error(f"Failed to retrieve purchases for customer with ID {customer_id}. Response code: {e.response.status_code}")
        except Exception as e:
            self.logger.error(f"An error occurred while retrieving purchases for customer with ID {customer_id}: {e}")
        return []
            
        
