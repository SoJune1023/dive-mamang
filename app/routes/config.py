import json
import logging
from pathlib import Path
from flask import Blueprint, request, jsonify

config_bp = Blueprint('config_bp', __name__)

@config_bp.route('/updateConfigValue', methods = ['POST'])
def updateConfigValue():
    try:
        payload = request.get_json(force = True)
        """ payload : dict
        {
            "willUpdate" : str,
            "newValue" : str
        }
        """
        will_update = payload.get("willUpdate")
        new_value = payload.get("new_value")

        if not will_update or not new_value:
            logging.info("Config value is missing.")
            return jsonify({"error": "value is missing"}), 400
    except Exception as e:
        logging.info(f"Config value is missing. Error code: {e}")
        return jsonify({"error": "value is missing"}), 400

    try:
        path = Path(__file__).parent.parent.parent / 'data' / 'user' / 'config.json'
        with open(path, 'r', encoding = 'utf-8') as f:
            data = json.load(f)
        
        data[will_update] = new_value

        with open(path, 'w', encoding = 'utf-8') as f:
            json.dump(data, f, ensure_ascii = False, indent = 4)

        return jsonify({"message": "Config updated"}), 200

    except Exception as e:
        logging.info(f"Could not change config value. Error code: {e}")
        return jsonify({"error": "Could not change config value"}), 500