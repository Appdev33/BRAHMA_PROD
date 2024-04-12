from flask import Blueprint, request
from event_management_service.services.event_service import EventService

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
    
    return {'message': 'Event created successfully'}, 201


@event_blueprint.route('/', methods=['GET'])
def hello_world():
    return 'Hello, World!'