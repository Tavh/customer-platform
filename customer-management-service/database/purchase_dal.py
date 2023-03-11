from database.models import Purchase, Item, Customer
from sqlalchemy.orm import Session
import logging

class PurchaseDAL:
    def __init__(self, session: Session):
        self.session = session
        self.logger = logging.getLogger(__name__)

    def create_purchase(self, customer_id: int, item_id: int) -> Purchase:
        """
        Creates a new purchase with the given customer ID and item ID.

        Args:
            customer_id (int): The ID of the customer who made the purchase.
            item_id (int): The ID of the item that was purchased.

        Returns:
            Purchase: The created purchase object.
        """
        # Get the customer and item objects from the database
        customer = self.session.query(Customer).get(customer_id)
        item = self.session.query(Item).get(item_id)

        # If either the customer or the item is not found, return None
        if not customer or not item:
            self.logger.warning(f"Failed to create purchase: customer or item not found with ID {customer_id} or {item_id}")
            return None

        price_at_purchase_time = item.price

        purchase = Purchase(
            customer_id=customer_id,
            item_id=item_id,
            price_at_purchase_time=price_at_purchase_time
        )

        self.session.add(purchase)
        self.session.commit()
        self.logger.info(f"Created purchase: {purchase}")
        return purchase
