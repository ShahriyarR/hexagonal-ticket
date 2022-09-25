from flask import Flask

from src.main.containers import Container
from .blueprints.api import blueprint


def create_app() -> Flask:
    container = Container()
    app = Flask(__name__)
    app.container = container
    app.register_blueprint(blueprint)
    return app
