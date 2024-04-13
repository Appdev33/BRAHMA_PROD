from flask import Flask
from notification_service.controller.notification_controller import notification_blueprint
from notification_service.utils.kafka_consumer import consume_notification_messages
from config.logging_config import configure_logging


microservice_name = 'notification-service'
logger = configure_logging(microservice_name)

app = Flask(__name__)

# Register notification blueprint
app.register_blueprint(notification_blueprint, url_prefix='/notifications')

# # Example usage:
# bootstrap_servers = 'localhost:29092,localhost:39092'  # Specify your Kafka bootstrap servers
# topic = 'hello-topic'  # Specify the Kafka topic for events
# consume_event_messages(bootstrap_servers, topic)

if __name__ == "__main__":
    # Start Kafka consumer
    bootstrap_servers = 'localhost:29092,localhost:39092'  # Specify your Kafka bootstrap servers
    topic = 'hello-topic'  # Specify the Kafka topic for notifications
    try:
        consume_notification_messages(bootstrap_servers, topic)
    except Exception as e:
        logger.error(f"Error starting Kafka consumer: {e}")
    # logger.info('Starting the notifcation app....')
    # Run Flask app
    app.run(debug=True)