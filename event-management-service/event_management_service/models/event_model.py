from config.logging_config import configure_logging

logger = configure_logging('event-management-service')


class Event:
    def __init__(self, event_type, **kwargs):
        self.event_type = event_type
        self.payload = kwargs
        # You can add more attributes as needed
        logger.info('Initialising Event Class')
        
    def save(self):
        # Add logic to save the event to a database or perform any other actions
        print("Event saved:", self.event_type, self.payload)
