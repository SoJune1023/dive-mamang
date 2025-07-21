import json
import logging
from pathlib import Path

try:
    path = Path(__file__).parent.parent / 'data' / 'user' / 'config.json'
    with open(path, 'r', encoding = 'utf-8') as f:
        data = json.load(f)
except Exception as e:
    #TODO: except시 error raises.
    #TODO: log 남기기.
    pass

class Config:
    # TODO: app/services/gpt.py의 gpt_setup_client()에 필요한 함수인 key, time, retires 불러오기.
    "API_KEY" = data.get("API_KEY", "none")
    "TIME" = data.get("TIMEOUT", 120)
    "RETIRES" = data.get("")
    # TODO: 위에서 불러온 값을 class를 활용하여 저장하기.
    # TODO: log 남기기.
    pass
