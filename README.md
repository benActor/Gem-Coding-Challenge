# Gem-Coding-Challenge

## Description
This Code Implements an API to Solve powerplant-coding-challenge.

The API is developped using FLASK.

## Execution
To launch the Api pull the

1. pull the code and move to directory coding-challenge

2. run *_pip install -r requirements.txt_*

3. run *_python app.py_*

The API exposes a route for POST REQUEST at _/productionplan_

Parameters to be passed as JSON-DOCUMENT with the following structure

{ "load": float, "fuels": { "gas(euro/MWh)": float, "kerosine(euro/MWh)": float, "co2(euro/ton)": float, "wind(%)": float }, "powerplants": [ { "name": String, "type": String", "efficiency": float, "pmin": integer, "pmax": integer }, ... ] }
