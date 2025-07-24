import logging
from flask import Blueprint, request, jsonify

import app.utils as utils
import app.services as services
from app.loadConfig import Config

chat_bp = Blueprint('chat_bp', __name__)

@chat_bp.route('/onSend', methods = ['POST'])
def onSend():
    # Get payload.
    try:
        payload = request.get_json(force = True)
        """ payload : dict
        {
            "message"(str) : <user_message>,
            "user_note"(str) : <user_note>
        }
        """

        # message, user_note가 비어있는 경우 " "로 대체
        message = payload.get("message", " ")
        user_note = payload.get("user_note", " ")

        # load prompt from data/character/prompt.json
        prompt = utils.prompt_loader()
        # build prompt
        gpt_prompt = utils.prompt_builder(prompt, user_note)
    except Exception as e:
        logging.error(f"Could not get payload.\nFile: {__file__}\nError code: {e}")
        return jsonify({"error": "could not retrieve message or user_note"}), 403

    # Load previous conversation
    i = Config.MAX_PREVIOUS
    previous = []
    previous_conversation = utils.gpt_load_previous_conversation()

    # 읽기 편하게 previous_conversation을 변환
    if len(previous_conversation) > i:
        for text in previous_conversation:
            will_append = f"{i} message ago: \n'User': {text["user"]} 'System': {text["gpt"]}"
            previous.append(will_append)
            i += -1
    else:
        i = len(previous_conversation)
        for text in previous_conversation:
            will_append = f"{i} message ago: \n'User': {text["user"]} 'System': {text["gpt"]}"
            previous.append(will_append)
            i += -1

    # API_KEY가 올바른 값인지 검증
    gpt_key = Config.API_KEY
    if not gpt_key:
        return jsonify({"error": "API_KEY is missing"}), 403

    # 해당 config는 default value가 있기에 비어있을 경우가 없음.
    gpt_model = Config.MODEL
    gpt_time = Config.MAX_TIME
    gpt_retries = Config.MAX_RETRIES

    # gpt client 생성. -> type: OpenAI
    gpt_client = services.gpt_setup_client(gpt_key, gpt_time, gpt_retries)
    
    # gpt response 생성.
    gpt_response = services.gpt_send(gpt_client, gpt_model, gpt_prompt, message, previous)
    """ gpt_response : dict
    {
        response_text (List[TextFormat]):
        {
            message (str): 대화 내용
            context (str): 해당 메시지의 상황/맥락
        },
        image (str): 이미지 URL
    }
    """

    # Get gpt response
    response_text = gpt_response.get("response_text")
    if not response_text:
        return jsonify({"error": "Response is missing."}), 502

    # 만약 img_list에 gpt_response img가 없을 경우 default img를 가져옵니다.
    img_list = utils.load_img_list()
    defalut_img = utils.load_default_img
    response_image = gpt_response.get("image")
    if not response_image in img_list:
        response_image = defalut_img

    # Gpt response를 user가 읽기 쉬운 형태로 반환
    try:
        result_text = ""
        for text in response_text:
            result_text += '"' + text["message"] + '"'
            result_text += '*' + text["context"] + '*'
    except Exception as e:
        logging.error(f"Could not load response from chat-gpt.\nFile: {__file__}\nError code: {e}")
        return jsonify({"error": "Could not load response from chat-gpt"}), 502

    # upload conversation
    conversation = {"conversation": {"user": message, "gpt": result_text}}
    services.update_save(conversation) # update_save()내부에서 예외 처리 되어있음.

    # TODO: Front end로 송신 기능 추가.
    return jsonify({"text": result_text, "image": response_image}), 200