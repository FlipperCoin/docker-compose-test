import pika
import json
import base64
import random
from time import sleep

def init_rabbit():
    # Connect to rabbit
    connection = pika.BlockingConnection(
        pika.ConnectionParameters(host='rabbitmq')
    )
    channel = connection.channel()

    # Declare rabbit objects
    channel.exchange_declare(
        exchange='produced_data_ex', 
        exchange_type='fanout'
    )
    
    return channel

def generate_data():
    return bytes([i for i in range(0,random.randrange(10,50))])

def json_data(data):
    b64data : str = (base64.b64encode(data)).decode('utf-8')

    return json.dumps(
        {
            'data': b64data
        }
    )

def output(channel, msg):
    channel.basic_publish(
        exchange='produced_data_ex',
        routing_key='',
        body=msg
    )

def main():
    channel = init_rabbit()

    while True:
        data = generate_data()
        output(channel, json_data(data))
        sleep(0.5)

if __name__ == "__main__":
    main()