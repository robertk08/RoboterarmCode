from dataclasses import asdict
import json
import requests
from ControlCommand import ControlCommand

class ConnectionService:
    @staticmethod
    def send_request(command: ControlCommand, arduino_ip: str = "192.168.4.1"):
        url = f"http://{arduino_ip}/control"
        
        # Convert ControlCommand instance to JSON string
        json_data = json.dumps(asdict(command))
        print(f"Request JSON: {json_data}")

        try:
            requests.post(url, headers={"Content-Type": "application/json"}, data=json_data, timeout=2)
        except requests.exceptions.RequestException:
            pass

# Example usage:
# cmd = ControlCommand(device="LED", action=1, values=[[255, 0, 0]])
# ConnectionService.send_request(cmd)