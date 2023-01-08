# amqps://ukccxsmd:AYilVOjPABNBBA84wbaNFrgWtqfnS-3N@puffin.rmq2.cloudamqp.com/ukccxsmd

import pika, json

params = pika.URLParameters('amqps://ukccxsmd:AYilVOjPABNBBA84wbaNFrgWtqfnS-3N@puffin.rmq2.cloudamqp.com/ukccxsmd')

connection = pika.BlockingConnection(params)

channel = connection.channel()


def publish(method, body):
    properties = pika.BasicProperties(method)
    channel.basic_publish(exchange='', routing_key='admin', body=json.dumps(body), properties=properties)
