from kafka import KafkaProducer
from json import dumps
from util.logger import get_logger


class KafkaPurchaseProducer:
    """
    A Kafka producer that publishes purchase events to a Kafka topic.

    Args:
        bootstrap_servers (str): A comma-separated string of Kafka server addresses to bootstrap from.
        topic (str): The Kafka topic to publish purchase events to.
    """

    def __init__(self, bootstrap_servers: str, topic: str):
        # Create a dedicated logger
        self.logger = get_logger(__name__)
        # Create a Kafka producer
        self.producer = KafkaProducer(
            bootstrap_servers=bootstrap_servers,
            value_serializer=lambda x: dumps(x).encode('utf-8')
        )
        self.topic = topic

    def publish_purchase(self, customer_id, item_id):
        """
        Publishes a purchase event to the Kafka topic.

        Args:
            customer_id (int): The ID of the customer who made the purchase.
            item_id (int): The ID of the item that was purchased.
        """
        message = {
            'event_type': 'purchase',
            'customer_id': customer_id,
            'item_id': item_id
        }
        self.logger.info(f"Producing message: {message}\n to topic: {self.topic}")
        # Send the message to the Kafka topic
        self.producer.send(self.topic, value=message)
        # Wait for any outstanding messages to be delivered and delivery reports received
        self.producer.flush()
