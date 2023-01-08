# amqps://ukccxsmd:AYilVOjPABNBBA84wbaNFrgWtqfnS-3N@puffin.rmq2.cloudamqp.com/ukccxsmd

import pika, json, django, os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "admin.settings")
django.setup()

from products.models import Product

params = pika.URLParameters('amqps://ukccxsmd:AYilVOjPABNBBA84wbaNFrgWtqfnS-3N@puffin.rmq2.cloudamqp.com/ukccxsmd')

connection = pika.BlockingConnection(params)

channel = connection.channel()

channel.queue_declare(queue='admin')


def callback(ch, method, properties, body):
    print('Received in admin')
    id = json.loads(body)
    print(id)
    product = Product.objects.get(id=id)
    product.likes = product.likes + 1
    product.save()
    print('Product liked +1')


channel.basic_consume(queue='admin', on_message_callback=callback, auto_ack=True)

print('Started Consuming')

channel.start_consuming()

channel.close()
