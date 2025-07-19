from flask import Blueprint, request, jsonify

import utils

chat_bp = Blueprint('chat_bp', __name__)

@chat_bp.routes('/onSend', methods = ['POST'])
def onSend():
    # TODO: chat-GPT 에게 보낼 text 파일을 user에게 받은 json에서 가공
    try:
        payload = request.get_json(force = True)

    except Exception as e:
        pass
    # TODO: chat-GPT 세션 작성
    # TODO: chat-GPT 에게 받은 text 파일을 json으로 가공
    # TODO: return json
    pass