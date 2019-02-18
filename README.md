## A RabbitMQ Item Publisher for Scrapy Framework.

Scrapy-RabbitMQ-Publisher allows you to save publish items to RabbitMQ.

## Installation

Using pip, type in your command-line prompt

```
pip install scrapy-rabbitmq-publisher
```
 
Or clone the repo and inside the `scrapy-rabbitmq-publisher` directory, type

```
python setup.py install
```

## Usage

Add following code to your scrapy settings.

```python
RABBITMQ_HOST = "localhost"
RABBITMQ_PORT = 5672
RABBITMQ_USER = "guest"
RABBITMQ_PASSWORD = "guest"
RABBITMQ_VIRTUAL_HOST = "/"
RABBITMQ_EXCHANGE = "scrapy"
RABBITMQ_ROUTING_KEY = "item"
RABBITMQ_QUEUE = "item"

ITEM_PIPELINES = {
    "scrapy_rabbitmq.pipelines.RabbitMQItemPublisherPipeline": 1,
}
```

## Copyright & License

Copyright (c) 2019 Artem Rys - Released under The MIT License.