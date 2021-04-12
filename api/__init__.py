from flask import Flask
from api.config import Config
from api.power_plants.route import production


app = Flask(__name__)
app.config.from_object(Config)
app.register_blueprint(production)

