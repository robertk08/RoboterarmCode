# main.py
from connection_service import ControlCommand, ConnectionService


command = ControlCommand(device="LED", action=1, values=[[255, 0, 0]])
ConnectionService.send_request(command)