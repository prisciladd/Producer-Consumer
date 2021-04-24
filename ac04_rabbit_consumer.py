import pika

connection = pika.adapters.blocking_connection.BlockingConnection(
pika.connection.ConnectionParameters(host="localhost"))

channel = connection.channel()

channel.exchange_declare(exchange='logs', exchange_type='fanout')

result = channel.queue_declare(queue='' ,exclusive=True)
queue_name = result.method.queue

channel.queue_bind(exchange='logs', queue=queue_name)

print('[*] Esperando logs. Para sair pressione CTRL+C')

def callback(ch,method,properties,body):
    print('[x] %r' % body)

channel.basic_consume(
    queue=queue_name,on_message_callback=callback, auto_ack=True)

channel.start_consuming()
