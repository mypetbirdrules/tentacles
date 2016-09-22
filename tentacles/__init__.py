#!/usr/bin/env python3
from flask import Flask
app = Flask(__name__)

import tentacles.views # Make sure views are imported after the app's creation
