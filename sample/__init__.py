from flask import Flask
import config
from kontent_delivery.client import DeliveryClient

app = Flask(__name__)

client = DeliveryClient(config.project_id, options=config.delivery_options)

import sample.home.views
