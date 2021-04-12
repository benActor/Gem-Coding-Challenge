from flask import request, jsonify, Blueprint
from api.power_plants.utils import PowerplantSvc
from api.init_app import socketio

production = Blueprint('production', __name__)


@production.route("/productionplan", methods=["POST"])
def production_plan():
    if request.is_json:
        pwp_svc = PowerplantSvc(request.json)
        response = [{"name": p.name, "p": pwp_svc.get_pwp_load(p)} for p in pwp_svc.get_optimal_combination()]
        socketio.emit("json", {"payload": request.json, "response": response})
        return jsonify(response)







