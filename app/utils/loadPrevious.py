import json
import logging
from pathlib import Path

from app.loadConfig import Config

def load_previous_conversation():
    path = Path(__file__).parent.parent.parent / 'data' / 'user' / 'save.json'
    with open(path, 'r', encoding = 'utf-8') as f:
        data = json.load(f)
    
    previous_conversation = data['history']
    
    # TODO: 과거 대화를 얼마나 가져올지 app.loadConfig 파일에서 불러온 후 if 문을 통한 compare.
    previous_conversation = previous_conversation[-10:]

    # TODO: return result