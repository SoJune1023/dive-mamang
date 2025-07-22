import json
from pathlib import Path
from flask import request, Blueprint

userNote_bp = Blueprint('userNote_bp', __name__)

@userNote_bp.route('/onUploadUserNote', methods = ['POST'])
def onUploadUserNote():
    try:
        payload = request.get_json(force = True)
        """ payload : dict
        {
            "user_note": <user_note_here>
        }
        """

        user_note = payload.get("user_note")

        if not user_note:
            raise ValueError ("User note is missing")

        path = Path(__file__).parent.parent.parent / 'data' / 'user' / 'userNote.json'
        with open(path, 'w', encoding = 'utf-8') as f:
            data = json.load(f)

        data["user_note"] = user_note

        with open(path, 'r', encoding = 'utf-8') as f:
            json.dump(data, f, ensure_ascii = False, indent = 4)
    except Exception as e:
        raise Exception (f"Something went worng. Error code: {e}")