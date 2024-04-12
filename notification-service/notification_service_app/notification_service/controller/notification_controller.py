from flask import Blueprint, request
from notification_service.services.notification_service import NotificationService

notification_blueprint = Blueprint('notifications', __name__)

@notification_blueprint.route('/send', methods=['POST'])
def send_notification():
    data = request.json
    # recipient = data.get('recipient')
    # message = data.get('message')
    print('###################%s',data)
    recipient = data.get('recipient')
    message = data.get('message')
    notification_type = data.get('notification_type')
    if not recipient or not message or not notification_type:
        return {'error': 'Recipient, message, and notification_type are required'}, 400
    notification_type ='email'  
    NotificationService.send_notification(notification_type, recipient, message)
    return {'message': 'Notification sent successfully'}, 200
