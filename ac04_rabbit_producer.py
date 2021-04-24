import pika
import sys

connection = pika.adapters.blocking_connection.BlockingConnection(
pika.connection.ConnectionParameters(host="localhost"))
#credentials = pika.PlainCredentials('guest', 'guest')
#connection = pika.ConnectionParameters('rabbit-server1',
                                       #5672,
                                       #'/',
                                       #credentials)

channel = connection.channel()

channel.exchange_declare(exchange='logs', exchange_type='fanout')

message= ''.join(sys.argv[1:]) or 'info: Hello World!'
channel.basic_publish(exchange='logs', routing_key='', body=message)
print("[x] Sent %r" % message)

connection.close()
