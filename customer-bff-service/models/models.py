from dataclasses import dataclass
from typing import List


@dataclass
class Customer:
    """
    Represents a customer who can make purchases.
    """
    id: int
    name: str
    purchases: List["Purchase"]

    def to_json(self):
        """
        Returns a JSON representation of this customer, including their ID, name, and all of their purchases.

        Returns:
            str: A JSON string representing this customer.
        """
        return {
            'id': self.id,
            'name': self.name,
            'purchases': [purchase.to_json() for purchase in self.purchases]
        }


@dataclass
class Item:
    """
    Represents an item that can be purchased.
    """
    id: int
    name: str
    price: float

    def to_json(self):
        """
        Returns a JSON representation of this item, including its ID, name, and price.

        Returns:
            str: A JSON string representing this item.
        """
        return {
            'id': self.id,
            'name': self.name,
            'price': self.price
        }


@dataclass
class Purchase:
    """
    Represents a purchase made by a customer for an item.
    """
    id: int
    purchase_time: str
    price_at_purchase_time: float
    customer: Customer
    item: Item

    def to_json(self):
        """
        Returns a JSON representation of this purchase, including its ID, purchase time, price at purchase time,
        and the customer and item objects involved in the purchase.

        Returns:
            dict: A dictionary representing this purchase.
        """
        return {
            'id': self.id,
            'purchase_time': self.purchase_time,
            'price_at_purchase_time': self.price_at_purchase_time,
            'customer': {
                'id': self.customer.id,
                'name': self.customer.name
            },
            'item': {
                'id': self.item.id,
                'name': self.item.name,
                'price': self.item.price
            }
        }
