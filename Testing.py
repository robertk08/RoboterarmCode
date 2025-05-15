import time
from JsonSync import ControlCommand, ConnectionService

i = 0
# This code will turn the device on and off 10 times, with a 1-second delay between each action.

while i < 10:
    # Turn the device "on"
    command_on = ControlCommand(device="LED", action=1)  #  action=1 means "on"
    ConnectionService.send_request(command_on)
    print("Device turned ON")
    time.sleep(1)  # Wait for 1 second

    # Turn the device "off"
    command_off = ControlCommand(device="LED", action=0)  #  action=0 means "off"
    ConnectionService.send_request(command_off)
    print("Device turned OFF")
    time.sleep(1) 
    i += 1