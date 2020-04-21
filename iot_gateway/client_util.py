# uses MQTT protocol, which communicates over port 8883
# ensure port 8883 is open on firewall
# for help ad workarounds:
# https://docs.microsoft.com/en-us/azure/iot-hub/iot-hub-mqtt-support#connecting-to-iot-hub
from azure.iot.device import IoTHubDeviceClient, Message
import json


connection_string_file = open('connection_string.json')
connection_json = json.loads(connection_string_file.read())

CONNECTION_STRING = connection_json['connection_string']
CONNECTION_HOSTNAME = connection_json['HostName']
CONNECTION_DEVICE = connection_json['DeviceId']


def init_client_device():
    client = IoTHubDeviceClient.create_from_connection_string(CONNECTION_STRING)
    return client

# decice is device id,
# location is location of edge device
# time is epoch time data was collected
# data is a json  of data from device:
# data should be of the form:
# {"temperature" : 'XX',
#  "turbidity"   : 'XX',
#  "tds"         : 'XX',
#  "other"       : 'XX'
# }
# creates a json dictionary and dumps it into a string, passes string to azure Message()
# ensure the message is a dictionary before applying json.dumps()
def create_message(device, location, time, data):
    # data is itself a  python dictionary
    json_message = {
        "device" : device,
        "location" : location,
        "time" : time,
        "data" : data
    }
    formated_message = json.dumps(json_message)
    message = Message(formated_message)
    return message

def send_message(client, message):
    try:
        print("Sending Message: " + str(message))
        client.send_message(message)
        print("Message sent Successfully")
        return 0
    except:
        print("Message sent Failed")
        return 1

############### additional functions ###############

# cloud host name, iot hub name on azure platform
def get_host():
    return CONNECTION_HOSTNAME

# represents the name of this device from cloud perspective
def get_device():
    return CONNECTION_DEVICE
