import json
from flask import Blueprint, request, jsonify

import utils
import services
import loadConfig

chat_bp = Blueprint('chat_bp', __name__)

@chat_bp.route('/onSend', methods = ['POST'])
def onSend():
    try:
        payload = request.get_json(force = True)
        """ payload : dict
        {
            "message"(str) : <user_message>,
            "user_note"(str) : <user_note>
        }
        """

        message = payload.get("message")
        user_note = payload.get("user_note")

        prompt = utils.prompt_loader()
        gpt_prompt = utils.prompt_builder(prompt + user_note)

    except Exception as e:
        pass

    # API_KEY가 올바른 값인지 검증
    gpt_key = loadConfig.API_KEY
    if not gpt_key:
        # TODO: raise error and skip the code.
        pass

    gpt_model = loadConfig.MODEL
    gpt_time = loadConfig.MAX_TIME
    gpt_retries = loadConfig.MAX_RETRIES

    gpt_client = services.gpt_setup_client(gpt_key, gpt_time, gpt_retries)
    
    gpt_response = services.gpt_send(gpt_client, gpt_model, gpt_prompt, message)

    # TODO: return json
    pass