# amqps://ukccxsmd:AYilVOjPABNBBA84wbaNFrgWtqfnS-3N@puffin.rmq2.cloudamqp.com/ukccxsmd

import pika

params = pika.URLParameters('amqps://ukccxsmd:AYilVOjPABNBBA84wbaNFrgWtqfnS-3N@puffin.rmq2.cloudamqp.com/ukccxsmd')

connection = pika.BlockingConnection(params)

channel = connection.channel()


def publish(method, body):
    pass
