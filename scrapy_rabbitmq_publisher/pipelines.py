import json

import pika
from scrapy.utils.serialize import ScrapyJSONEncoder


class RabbitMQItemPublisherPipeline(object):
    def __init__(self, host, port, user, password, virtual_host, exchange, routing_key, queue):
        self.host = host
        self.port = port
        self.user = user
        self.password = password
        self.virtual_host = virtual_host
        credentials = pika.PlainCredentials(self.user, self.password)
        parameters = pika.ConnectionParameters(self.host,
                                               self.port,
                                               self.virtual_host,
                                               credentials)
        self.connection = pika.BlockingConnection(parameters=parameters)
        self.channel = self.connection.channel()
        self.exchange = exchange
        self.routing_key = routing_key
        self.queue = queue
        self.channel.exchange_declare(exchange=exchange,
                                      exchange_type="direct",
                                      durable=True)
        self.channel.queue_declare(queue=queue,
                                   durable=True)
        self.channel.queue_bind(exchange=exchange,
                                routing_key=routing_key,
                                queue=queue)
        self.encoder = ScrapyJSONEncoder()

    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            host=crawler.settings.get("RABBITMQ_HOST"),
            port=crawler.settings.get("RABBITMQ_PORT"),
            user=crawler.settings.get("RABBITMQ_USER"),
            password=crawler.settings.get("RABBITMQ_PASSWORD"),
            virtual_host=crawler.settings.get("RABBITMQ_VIRTUAL_HOST"),
            exchange=crawler.settings.get("RABBITMQ_EXCHANGE"),
            routing_key=crawler.settings.get("RABBITMQ_ROUTING_KEY"),
            queue=crawler.settings.get("RABBITMQ_QUEUE"),
        )

    def close_spider(self, spider):
        self.channel.close()
        self.connection.close()

    def process_item(self, item, spider):
        data = self.encoder.encode(item)
        self.channel.basic_publish(
            exchange=self.exchange,
            routing_key=self.routing_key,
            body=data,
        )
        return item
