import logging
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
        logging.info(f'"user": {message}')

        user_note = payload.get("user_note", "")

        prompt = utils.prompt_loader()
        gpt_prompt = utils.prompt_builder(prompt + user_note)
    except Exception as e:
        logging.error(f"Could not get payload. Error code: {e}")
        return jsonify({"error": "could not retrieve message or user_note"}), 403

    # API_KEY가 올바른 값인지 검증
    gpt_key = loadConfig.API_KEY
    if not gpt_key:
        return jsonify({"error": "API_KEY is missing"}), 403

    gpt_model = loadConfig.MODEL
    gpt_time = loadConfig.MAX_TIME
    gpt_retries = loadConfig.MAX_RETRIES

    gpt_client = services.gpt_setup_client(gpt_key, gpt_time, gpt_retries)
    
    gpt_response = services.gpt_send(gpt_client, gpt_model, gpt_prompt, message)
    """ gpt_response : dict
    - response_text (List[TextFormat]):
        - message (str): 대화 내용
        - context (str): 해당 메시지의 상황/맥락
    - image (str): 이미지 URL
    """

    response_text = gpt_response.get("response_text")
    response_image = gpt_response.get("image", "<default_image_URL>")

    if not response_text:
        return jsonify({"error": "Response is missing."}), 502

    try:
        result_text = ""
        for text in response_text:
            result_text += '"' + text["message"] + '"'
            result_text += '*' + text["context"] + '*'

        logging.info(f'"CPU": {result_text}')
        return jsonify({"text": result_text, "image": response_image}), 200
    except Exception as e:
        logging.error(f"could not load response from chat-gpt. Error code: {e}")
        return jsonify({"error": "Could not load response from chat-gpt"}), 502