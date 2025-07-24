import logging
from flask import Blueprint, request, jsonify

import app.utils as utils
import app.services as services
import app.loadConfig as loadConfig

chat_bp = Blueprint('chat_bp', __name__)

@chat_bp.route('/onSend', methods = ['POST'])
def onSend():
    try:
        # TODO: load previous conversaions.
        # previous_conversaion = load_previous_conversaion()
        # app/utils/loadPrevious
        pass
    except Exception as e:
        logging.error(f"Failed to load previous conversations.\nFile: {__file__}\nError code: {e}")
        return jsonify({"error": "Failed to load previous conversations."}), 403
    
    try:
        payload = request.get_json(force = True)
        """ payload : dict
        {
            "message"(str) : <user_message>,
            "user_note"(str) : <user_note>
        }
        """

        message = payload.get("message", " ")
        user_note = payload.get("user_note", " ")

        prompt = utils.prompt_loader()
        gpt_prompt = utils.prompt_builder(prompt, user_note)
    except Exception as e:
        logging.error(f"Could not get payload.\nFile: {__file__}\nError code: {e}")
        return jsonify({"error": "could not retrieve message or user_note"}), 403

    # API_KEY가 올바른 값인지 검증
    gpt_key = loadConfig.API_KEY
    if not gpt_key:
        return jsonify({"error": "API_KEY is missing"}), 403

    # 해당 config는 default value가 있기에 비어있을 경우가 없음.
    gpt_model = loadConfig.MODEL
    gpt_time = loadConfig.MAX_TIME
    gpt_retries = loadConfig.MAX_RETRIES

    # gpt client 생성. -> type: OpenAI
    gpt_client = services.gpt_setup_client(gpt_key, gpt_time, gpt_retries)
    
    # gpt response 생성.
    gpt_response = services.gpt_send(gpt_client, gpt_model, gpt_prompt, message)
    """ gpt_response : dict
    - response_text (List[TextFormat]):
        - message (str): 대화 내용
        - context (str): 해당 메시지의 상황/맥락
    - image (str): 이미지 URL
    """

    response_text = gpt_response.get("response_text")
    # TODO: Compare with image list and if not match -> load default image url
    response_image = gpt_response.get("image", "<default_image_URL>")

    if not response_text:
        return jsonify({"error": "Response is missing."}), 502

    try:
        result_text = ""
        for text in response_text:
            result_text += '"' + text["message"] + '"'
            result_text += '*' + text["context"] + '*'
    except Exception as e:
        logging.error(f"Could not load response from chat-gpt.\nFile: {__file__}\nError code: {e}")
        return jsonify({"error": "Could not load response from chat-gpt"}), 502

    conversation = {"conversation": {"user": message, "gpt": result_text}}
    services.update_save(conversation) # update_save()내부에서 예외 처리 되어있음.

    # TODO: Front end로 송신 기능 추가.
    return jsonify({"text": result_text, "image": response_image}), 200