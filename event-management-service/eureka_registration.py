import requests
import json
import atexit

class EurekaRegistration:
    def __init__(self, app_name, instance_host, instance_port, eureka_server_url):
        self.app_name = app_name
        self.instance_host = instance_host
        self.instance_port = instance_port
        self.eureka_server_url = eureka_server_url

    def register_with_eureka(self):
        registration_payload = {
            "instance": {
                "hostName": self.instance_host,
                "app": self.app_name,
                "ipAddr": self.instance_host,
                "status": "UP",
                "port": {
                    "$": self.instance_port,
                    "@enabled": "true"
                },
                "dataCenterInfo": {
                    "@class": "com.netflix.appinfo.InstanceInfo$DefaultDataCenterInfo",
                    "name": "MyOwn"
                }
            }
        }

        headers = {'Content-Type': 'application/json'}

        try:
            response = requests.post(f"{self.eureka_server_url}/eureka/apps/{self.app_name}", 
                                     data=json.dumps(registration_payload), headers=headers)
            response.raise_for_status()
            print("Service registered successfully with Eureka server.")
        except Exception as e:
            print(f"Failed to register service with Eureka server: {e}")

    def unregister_from_eureka(self):
        try:
            unregister_url = f"{self.eureka_server_url}/eureka/apps/{self.app_name}/{self.instance_host}:{self.instance_port}"
            response = requests.delete(unregister_url)
            response.raise_for_status()
            print("Service unregistered successfully from Eureka server.")
        except Exception as e:
            print(f"Failed to unregister service from Eureka server: {e}")

# Configure Eureka Registration
eureka_registration = EurekaRegistration(
    app_name="event-management-service",
    instance_host="localhost",  # Replace with your actual host
    instance_port=5000,          # Replace with your actual port
    eureka_server_url="http://localhost:8761"  # Replace with your Eureka server URL
)
