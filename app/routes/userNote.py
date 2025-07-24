import json
import logging
from pathlib import Path
from flask import request, Blueprint, jsonify

userNote_bp = Blueprint('userNote_bp', __name__)

@userNote_bp.route('/onUploadUserNote', methods = ['POST'])
def onUploadUserNote():
    # Get payload
    try:
        payload = request.get_json(force = True)
        """ payload : dict
        {
            "user_note": <user_note_here>
        }
        """

        # Check if user_note is emtpy
        user_note = payload.get("user_note")
        if not user_note:
            return jsonify({"error": "User note is missing"}), 400

        # Open data/user/userNote.json
        path = Path(__file__).parent.parent.parent / 'data' / 'user' / 'userNote.json'
        with open(path, 'r', encoding = 'utf-8') as f:
            data = json.load(f)

        # Update new user_note
        data["user_note"] = user_note

        # Upload user_note
        with open(path, 'w', encoding = 'utf-8') as f:
            json.dump(data, f, ensure_ascii = False, indent = 4)

        logging.info(f"Success to upload user note.\nUser note: {user_note}")
        return jsonify({"message": "User note saved successfully."}), 200
    except Exception as e:
        logging.error(f"Failed to upload user note\nFile: {__file__}\nError code: {e}")
        return jsonify({"error": f"Something went wrong", "details": str(e)}), 500