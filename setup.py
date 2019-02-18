import os
import sys

import scrapy_rabbitmq_publisher

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

from codecs import open

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

if sys.argv[-1] == "publish":
    os.system("python setup.py sdist upload")
    sys.exit()

packages = [
    "scrapy_rabbitmq_publisher",
]

requires = [
    "pika",
    "Scrapy>=0.14",
]

setup(
    name="scrapy-rabbitmq-publisher",
    author="Artem Rys",
    description="Scrapy Item Pipeline to send items to RabbitMQ",
    version="0.1.1",
    author_email="rysartem@gmail.com",
    license="MIT",
    url="https://github.com/artemrys/scrapy-rabbitmq-publisher",
    install_requires=requires,
    packages=packages
)
