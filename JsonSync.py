import json
import requests
from dataclasses import dataclass, asdict
from typing import List, Optional

# Equivalent to your ControlCommand struct
@dataclass
class ControlCommand:
    device: str
    action: int
    values: Optional[List[List[int]]] = None

class ConnectionService:
    @staticmethod
    def send_request(command: ControlCommand, arduino_ip: str = "192.168.4.1"):
        url = f"http://{arduino_ip}/control"
        
        # Convert ControlCommand instance to JSON string
        json_data = json.dumps(asdict(command))
        print(f"Request JSON: {json_data}")

        try:
            response = requests.post(url, headers={"Content-Type": "application/json"}, data=json_data)
            print(f"Response Status Code: {response.status_code}")
            print(f"Response Data: {response.text}")
        except requests.RequestException as e:
            print(f"Request failed: {e}")

# Example usage:
# cmd = ControlCommand(device="LED", action=1, values=[[255, 0, 0]])
# ConnectionService.send_request(cmd)