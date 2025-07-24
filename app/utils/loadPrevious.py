import json
import logging
from pathlib import Path
from flask import jsonify

from app.loadConfig import Config

def gpt_load_previous_conversation():
    try:
        path = Path(__file__).parent.parent.parent / 'data' / 'user' / 'save.json'
        with open(path, 'r', encoding = 'utf-8') as f:
            data = json.load(f)
        
        previous_conversation = data['history']
        # previous_conversation = [{"user": <conversation>, "gpt": <conversation>} . . .]
        
        # 과거 대화를 얼마나 가져올지 app/loadConfig.py에서 불러온 후 if 문을 통한 compare.
        max_previous = Config.MAX_PREVIOUS
        if len(previous_conversation) > max_previous:
            # 최대 conversation history에 맞춤
            previous_conversation[-max_previous:]
        
        return previous_conversation
    except Exception as e:
        logging.error(f"Failed to load previous conversation.\nFile: {__file__}\nError code: {e}")
        return jsonify({"error": "Failed to load previous conversation."}), 403

def user_load_previous_conversation():
    try:
        path = Path(__file__).parent.parent.parent / 'data' / 'user' / 'save.json'
        with open(path, 'r', encoding = 'utf-8') as f:
            data = json.load(f)
        
        previous_conversation = data['history']
        # previous_conversation = [{"user": <conversation>, "gpt": <conversation>} . . .]

        return previous_conversation
    except Exception as e:
        logging.error(f"Failed to load previous conversation.\nFile: {__file__}\nError code: {e}")
        return jsonify({"error": "Failed to load previous conversation."}), 403