from flask import Flask
from event_management_service.controllers.event_controller import event_blueprint
from config.logging_config import configure_logging
from eureka_registration import EurekaRegistration
import atexit

microservice_name = 'event-management-service'
logger = configure_logging(microservice_name)

app = Flask(__name__)


# Configure Eureka Registration
eureka_registration = EurekaRegistration(
    app_name="event-management-service",
    instance_host="localhost",  # Replace with your actual host
    instance_port=5000,          # Replace with your actual port
    eureka_server_url="http://localhost:8761/"  # Replace with your Eureka server URL
)

# Register with Eureka on startup
eureka_registration.register_with_eureka()

# Unregister from Eureka on shutdown
atexit.register(eureka_registration.unregister_from_eureka)

# Register blueprints
app.register_blueprint(event_blueprint, url_prefix='/events')


if __name__ == "__main__":
    # logger.info('Starting main app....')
    app.run(debug=True)
