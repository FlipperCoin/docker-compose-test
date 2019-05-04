import pika

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

    result = channel.queue_declare('', exclusive=True)
    channel.queue_bind(
        exchange='produced_data_ex',
        queue=result.method.queue
    )

    channel.basic_consume(
        queue=result.method.queue,
        on_message_callback=on_new_message,
        auto_ack=True
    )

    return channel

def on_new_message(ch, method, properties, body):
    print(body)

def main():
    channel = init_rabbit()

    channel.start_consuming()

if __name__ == "__main__":
    main()