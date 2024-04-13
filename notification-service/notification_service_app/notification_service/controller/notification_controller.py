from flask import Blueprint, request
from notification_service.services.notification_service import NotificationService
from config.logging_config import configure_logging

logger = configure_logging('notification-service')

notification_blueprint = Blueprint('notifications', __name__)

@notification_blueprint.route('/send', methods=['POST'])
def send_notification():
    data = request.json
    # recipient = data.get('recipient')
    # message = data.get('message')
    # recipient = data.get('recipient')
    message = data.get('message')
    notification_type = data.get('notification_type')
    if not recipient or not message or not notification_type:
        return {'error': 'Recipient, message, and notification_type are required'}, 400
    notification_type ='email'  
    logger.info('Sending notifcation to email....')
    NotificationService.send_notification(notification_type,'','')
    return {'message': 'Notification sent successfully'}, 200
