from event_management_service.models.event_model import Event
from event_management_service.utils.kafka_producer import process_event
import logging

# Create a logger for the EventService class
logger = logging.getLogger(__name__)


class EventService:
    @staticmethod
    def process_event(event_type, **kwargs):
        # Process the event based on the event type and payload
        event = Event(event_type=event_type, **kwargs)
        process_event(event_type, **kwargs)
        
        logger.info(f'Event processed successfully: {event_type}, {kwargs}')
        logger.error(f'Event processed successfully: {event_type}, {kwargs}')
        event.save()  # Assuming there's a save method in the Event model
