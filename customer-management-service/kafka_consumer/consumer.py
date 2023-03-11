from json import loads
from database.purchase_dal import PurchaseDAL
from threading import Thread
from util.logger import get_logger
from kafka import KafkaConsumer
import threading 


class KafkaPurchaseConsumer:
    """
    A Kafka consumer that listens for purchase events and creates new purchases in the database when they are received.
    """
    def __init__(self, purchase_dal: PurchaseDAL, topic: str, bootstrap_servers: str):
        """
        Initializes a new instance of the KafkaPurchaseConsumer class.

        Args:
            purchase_dal (PurchaseDAL): An instance of the PurchaseDAL class that can be used to create new purchases in the database.
            topic (str): The Kafka topic to listen on for purchase events.
            bootstrap_servers (str): A comma-separated string of Kafka server addresses to bootstrap from.
        """
        # Create a dedicated logger
        self.logger = get_logger(__name__)

        self.purchase_dal = purchase_dal
        self.consumer = KafkaConsumer(
            topic,
            bootstrap_servers=bootstrap_servers,
            auto_offset_reset='earliest',
            enable_auto_commit=False,
            group_id="purchase-consumers",
            value_deserializer=lambda x: loads(x.decode('utf-8'))
        )
        self.start()

    def consume(self):
        """
        Starts the Kafka consumer and listens for incoming messages.
        """
        for message in self.consumer:
            message = message.value
            self.logger.debug(f"Consumed message from '{self.consumer.topics}': {message} on thread: {threading.get_ident()}")
            if message['event_type'] == 'purchase':
                customer_id = message['customer_id']
                item_id = message['item_id']
                purchase = self.purchase_dal.create_purchase(customer_id=customer_id, item_id=item_id)
                self.logger.info(f"Created purchase: {purchase.to_json()}")
                self.consumer.commit()

    def start(self):
        """
        Starts the Kafka consumer in a new thread.
        """
        thread = Thread(target=self.consume)
        thread.start()
