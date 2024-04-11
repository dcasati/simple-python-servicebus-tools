#!/usr/bin/python3
from azure.servicebus import ServiceBusClient, ServiceBusReceiveMode
import argparse
import os
import json
from dotenv import load_dotenv
import time

load_dotenv()

# Set up command line argument parsing
parser = argparse.ArgumentParser(description='Receive messages from the specified Service Bus queue.')
parser.add_argument('--queue', help='The name of the Service Bus queue', required=True)
parser.add_argument('--remove', help='Remove all messages from the queue', action='store_true')  

args = parser.parse_args()

connstr = os.getenv('SERVICE_BUS_CONNECTION_STRING')
queue_name = args.queue

try:
    with ServiceBusClient.from_connection_string(connstr) as client:
        print("Service Bus Receiver Started. Listening for messages on ", queue_name)  
        if args.remove:  
            with client.get_queue_receiver(queue_name, receive_mode=ServiceBusReceiveMode.RECEIVE_AND_DELETE) as receiver:  
                while True:  
                    messages = receiver.receive_messages(max_message_count=10, max_wait_time=30)  
                    for msg in messages:  
                        print("Removed message: ", msg)  
                    if not messages:  
                        break  
        else:  
            with client.get_queue_receiver(queue_name) as receiver:  
                while True:  
                    messages = receiver.peek_messages(max_message_count=10)  
                    for msg in messages:  
                        print("Peeked message: ", msg)  
                    time.sleep(10)  # Wait for 30 seconds before peeking again  
except Exception as e:
    print("An error occurred:", e)
