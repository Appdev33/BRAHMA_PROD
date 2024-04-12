from notification_service.notifications.email_notification import send_email
# from notification_service.notifications.sms_notification import send_sms
# from notification_service.notifications.telegram_notification import send_telegram_message
# from notification_service.notifications.whatsapp_notification import send_whatsapp_message
from notification_service.utils.logging_config import logger

class NotificationService:
    @staticmethod
    def send_notification(notification_type, recipient, message):

        if notification_type == 'email':
            send_email(recipient, message)
            logger.info(f"Email notification sent to {recipient}")
        elif notification_type == 'sms':
            # send_sms(recipient, message)
            logger.info(f"SMS notification sent to {recipient}")
        elif notification_type == 'telegram':
            # send_telegram_message(recipient, message)
            logger.info(f"Telegram notification sent to {recipient}")
        elif notification_type == 'whatsapp':
            # send_whatsapp_message(recipient, message)
            logger.info(f"WhatsApp notification sent to {recipient}")
        else:
            logger.error("Invalid notification type")
