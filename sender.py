#!/usr/bin/python3
# sender.py
from azure.servicebus import ServiceBusClient, ServiceBusMessage
from dotenv import load_dotenv
import argparse
import os
import json

# Load environment variables from .env file
load_dotenv()

# Set up command line argument parsing
parser = argparse.ArgumentParser(description='Send a message to the specified Service Bus queue.')
parser.add_argument('--queue', help='The name of the Service Bus queue', required=True)
parser.add_argument('--file', help='The file path of the JSON file to be sent', required=True)
args = parser.parse_args()

queue_name = args.queue
connection_string = os.getenv('SERVICE_BUS_CONNECTION_STRING')

def load_json_file(filename):
    with open(filename) as job:
        data = json.load(job)
    return json.dumps(data)

def send_message(connection_string, queue_name, json_data):
    with ServiceBusClient.from_connection_string(connection_string) as client:
        with client.get_queue_sender(queue_name) as sender:
            single_message = ServiceBusMessage(json_data)
            sender.send_messages(single_message)
            print("Message sent: ", single_message)

# Load the JSON data from the specified file
json_data = load_json_file(args.file)

# Send the message
send_message(connection_string, queue_name, json_data)

# Example usage: python sender.py --queue your_queue_name --file path_to_your_file.json

