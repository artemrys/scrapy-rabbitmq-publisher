import os
import sys

import scrapy_rabbitmq_publisher

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

from codecs import open

from os import path

this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

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
    version="0.1.4",
    author_email="rysartem@gmail.com",
    license="MIT",
    url="https://github.com/artemrys/scrapy-rabbitmq-publisher",
    install_requires=requires,
    packages=packages,
    long_description=long_description,
    long_description_content_type="text/markdown",
)
