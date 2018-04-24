"""Main logic package."""

from flask import Flask

app = Flask(__name__)

from fetch_data import handlers
