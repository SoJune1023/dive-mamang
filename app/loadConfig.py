import json
import logging
from pathlib import Path

try:
    path = Path(__file__).parent.parent / 'data' / 'user' / 'config.json'
    with open(path, 'r', encoding = 'utf-8') as f:
        data = json.load(f)

    logging.info("Success to open config file!")
except Exception as e:
    logging.error(f"Failed to open data/user/config.json.\nFile: {__file__}\nError code: {e}")

class Config:
    API_KEY = data.get("API_KEY", "none")
    MODEL = data.get("MODEL", "gpt-4o")
    MAX_TIME = data.get("TIMEOUT", 120)
    MAX_RETRIES = data.get("MAX_RETRIES", 2)
    MAX_PREVIOUS = data.get("MAX_PREVIOUS", 7)