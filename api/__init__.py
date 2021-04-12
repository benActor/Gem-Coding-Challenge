from api.config import Config
from api.init_app import app, socketio
from api.power_plants.route import production


app.register_blueprint(production)


def create_app():
    return app, socketio


