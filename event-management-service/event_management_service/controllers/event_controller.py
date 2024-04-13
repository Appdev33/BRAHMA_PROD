from flask import Blueprint, request
from event_management_service.services.event_service import EventService
from config.logging_config import configure_logging

logger = configure_logging('event-management-service')

event_blueprint = Blueprint('events', __name__)

@event_blueprint.route('/create', methods=['POST'])
def create_event():
    data = request.json
    event_type = data.get('event_type')
    payload = data.get('payload')
    if not event_type:
        return {'error': 'Event type is required'}, 400
    
    if not payload:
        return {'error': 'Payload is required'}, 400
    
    EventService.process_event(event_type, **payload)
    logger.info('Event created successfully....')
    
    return {'message': 'Event created successfully'}, 201


@event_blueprint.route('/', methods=['GET'])
def hello_world():
    return 'Hello, World!'