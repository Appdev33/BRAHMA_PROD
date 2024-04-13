from confluent_kafka import Consumer, KafkaError
import json
from notification_service.services.notification_service import NotificationService
from config.logging_config import configure_logging

logger = configure_logging('notification-service')

def consume_notification_messages(bootstrap_servers, topic):
    """Consume notification messages from Kafka and process them."""
    consumer = Consumer({
        'bootstrap.servers': bootstrap_servers,
        'group.id': 'notification_consumer_group',
        'auto.offset.reset': 'earliest'
    })

    consumer.subscribe([topic])

    while True:
        msg = consumer.poll(timeout=1.0)
        if msg is None:
            continue
        if msg.error():
            if msg.error().code() == KafkaError._PARTITION_EOF:
                # End of partition event
                logger.info(f"Reached end of partition {msg.partition()}")
            elif msg.error():
                # Handle other errors
                logger.error(f"Error: {msg.error()}")
        else:
            # Process the message
            try:
                event_data = json.loads(msg.value().decode('utf-8'))
                event_type = event_data['type']

                # Process the event type as needed
                print(f"Received event: {event_data}")
                notification_data = json.loads(msg.value().decode('utf-8'))
                notification_type ='email'  
                NotificationService.send_notification(notification_type, '', '')
                # logger.info(f"Notification message processed: {event_payload}")
            except Exception as e:
                logger.error(f"Error processing notification message: {e}")

    consumer.close()
