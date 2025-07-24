import json
import logging
from pathlib import Path

try:
    path = Path(__file__).parent.parent / 'data' / 'user' / 'config.json'
    with open(path, 'r', encoding = 'utf-8') as f:
        data = json.load(f)
except Exception as e:
    logging.error(f"Failed to load data/user/config.json.\nFile: {__file__}\nError code: {e}")

class Config:
    API_KEY = data.get("API_KEY", "none")
    logging.info(f"Success to load API_KEY.\nAPI_KEY = {API_KEY}")
    MODEL = data.get("MODEL")
    logging.info(f"Success to load MODEL.\nMODEL = {MODEL}")
    MAX_TIME = data.get("TIMEOUT", 120)
    logging.info(f"Success to load MAX_TIME.\nMODEMAX_TIMEL = {MAX_TIME}")
    MAX_RETRIES = data.get("MAX_RETRIES", 2)
    logging.info(f"Success to load MAX_RETRIES.\nMAX_RETRIES = {MAX_RETRIES}")
    pass
