from confluent_kafka import Producer
import json

def delivery_report(err, msg):
    """Called once for each message produced to indicate delivery result."""
    if err is not None:
        print(f'Message delivery failed: {err}')
    else:
        print(f'Message delivered to {msg.topic()} [{msg.partition()}]')

def produce_event_message(bootstrap_servers, topic, event_type, **kwargs):
    """Produce event message to Kafka."""
    # Create Kafka Producer
    producer = Producer({'bootstrap.servers': bootstrap_servers})

    try:
        # Serialize message to bytes
        message = json.dumps({'type': event_type, **kwargs}).encode('utf-8')

        # Produce event message
        producer.produce(topic, value=message, callback=delivery_report)

        # Wait for all messages to be delivered
        producer.flush()
    finally:
        # Close the producer after flushing all messages
        producer.flush()
        producer.poll(1)  # Poll to handle delivery reports and callbacks
        producer.flush()  # Flush one more time to ensure all pending messages are delivered
        producer = None  # Set producer to None to release resources

def process_event(event_type, **kwargs):
    """Process event and produce message to Kafka."""
    # Kafka broker configuration
    bootstrap_servers = 'localhost:29092,localhost:39092'  # Assuming you want to produce to both Kafka brokers
    # Topic to produce messages to
    topic = 'hello-topic'

    # Produce event message
    produce_event_message(bootstrap_servers, topic, event_type, **kwargs)
