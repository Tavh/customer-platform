from database.models import Customer, Purchase
from typing import List, Optional
from sqlalchemy.orm import Session
import logging


class CustomerDAL:
    def __init__(self, session: Session):
        # Create a logger instance for this module
        self.logger = logging.getLogger(__name__)
        self.session = session

    def create_customer(self, name: str) -> Customer:
        """
        Creates a new customer with the given name.

        Args:
            name (str): The name of the customer.

        Returns:
            Customer: The created customer object.
        """
        customer = Customer(name=name)
        self.session.add(customer)
        self.session.commit()
        self.logger.info(f"Created customer: {customer}")
        return customer

    def get_customer_by_id(self, customer_id: int) -> Optional[Customer]:
        """
        Gets the customer with the given ID.

        Args:
            customer_id (int): The ID of the customer.

        Returns:
            Optional[Customer]: The customer object with the given ID, or None if not found.
        """
        customer = self.session.query(Customer).filter_by(id=customer_id).first()
        if customer is None:
            self.logger.warning(f"No customer found with ID {customer_id}")
        else:
            self.logger.info(f"Retrieved customer: {customer}")
        return customer
    
    def get_customer_purchases(self, customer_id: int) -> List[Purchase]:
        """
        Gets the purchases made by the customer with the given ID.

        Args:
            customer_id (int): The ID of the customer.

        Returns:
            List[Purchase]: A list of purchase objects made by the customer.
        """
        purchases = self.session.query(Purchase).filter_by(customer_id=customer_id).all()
        self.logger.info(f"Retrieved {len(purchases)} purchases for customer with ID {customer_id}")
        return purchases
