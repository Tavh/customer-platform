from typing import List, Optional
from database.models import Item
from sqlalchemy.orm import Session
import logging

class ItemDAL:
    def __init__(self, session: Session):
        self.session = session
        self.logger = logging.getLogger(__name__)

    def create_item(self, name: str, price: float) -> Item:
        """
        Creates a new item with the given name and price.

        Args:
            name (str): The name of the item.
            price (float): The price of the item.

        Returns:
            Item: The created item object.
        """
        item = Item(name=name, price=price)
        self.session.add(item)
        self.session.commit()
        self.logger.info(f"Created item: {item}")
        return item

    def get_item_by_id(self, item_id: int) -> Optional[Item]:
        """
        Gets the item with the given ID.

        Args:
            item_id (int): The ID of the item.

        Returns:
            Optional[Item]: The item object with the given ID, or None if not found.
        """
        item = self.session.query(Item).filter_by(id=item_id).first()
        if item is None:
            self.logger.warning(f"No item found with ID {item_id}")
        else:
            self.logger.info(f"Retrieved item: {item}")
        return item
