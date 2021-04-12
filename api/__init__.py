from flask import Flask
from api.config import Config
from api.power_plants.route import production


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)
    app.register_blueprint(production)
    return app
