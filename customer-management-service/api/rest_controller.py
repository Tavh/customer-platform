from flask import Flask, jsonify
from database.customer_dal import CustomerDAL


class RestController:
    """
    A REST API controller that handles requests related to customers and their purchases.
    """
    def __init__(self, app: Flask, customer_dal: CustomerDAL):
        """
        Initializes a new instance of the RestController class.

        Args:
            app (Flask): The Flask app instance.
            customer_dal (CustomerDAL): An instance of the CustomerDAL class that can be used to retrieve customer data.
        """
        self.app = app
        self.customer_dal = customer_dal

        self.register_endpoints()

    def register_endpoints(self):
        """
        Registers the REST API endpoints for this controller.
        """
        self.app.route('/customers/<customer_id>/purchases', methods=['GET'])(self.get_customer_purchases)
        self.app.route('/customers/<int:customer_id>/purchases', methods=['GET'])(self.get_customer_purchases)

    def get_customer_purchases(self, customer_id):
        """
        Handles a GET request to retrieve all purchases made by the customer with the given ID.

        Args:
            customer_id (int): The ID of the customer to retrieve purchases for.

        Returns:
            str: A JSON string representing the list of purchases made by the customer.
        """
        purchases = self.customer_dal.get_customer_purchases(customer_id=customer_id)
        return jsonify([p.to_json() for p in purchases])
