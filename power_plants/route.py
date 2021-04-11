from app import app
from flask import request, jsonify, blueprints
from power_plants.utils import PowerplantSvc


@app.route("/productionplan", methods=["POST"])
def production_plan():
    if request.is_json:
        pwp_svc = PowerplantSvc(request.json)
        return jsonify([{"name": p.name, "p": p.pmax} for p in pwp_svc.get_optimal_combination()])





