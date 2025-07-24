import json
import logging
from pathlib import Path
from flask import jsonify

def load_img_list():
    try:
        path = Path(__file__).parent.parent.parent / 'data' / 'character' / 'img' / 'imgList.json'
        with open(path, 'r', encoding = 'utf-8') as f:
            data = json.load(f)

        img_list = data['list']
        return img_list
    except Exception as e:
        logging.error(f"Cannot load data/character/img/imgList.json\nFile: {__file__}\nError code: {e}")
        return jsonify({"Cannot load data/character/img/imgList.json"}), 403

def load_default_img():
    try:
        path = Path(__file__).parent.parent.parent / 'data' / 'character' / 'img' / 'imgList.json'
        with open(path, 'r', encoding = 'utf-8') as f:
            data = json.load(f)
        
        default_img = data['default']
        return default_img
    except Exception as e:
        logging.error(f"Cannot load data/character/img/imgList.json\nFile: {__file__}\nError code: {e}")
        return jsonify({"Cannot load data/character/img/imgList.json"}), 403