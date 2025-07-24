import logging
from flask import Flask

from .loadConfig import Config
from .services import gpt_send, gpt_setup_client, load_save_for_gpt, update_save
from .utils import prompt_builder, prompt_loader
from .routes import chat_bp, config_bp, userNote_bp

def create_app():
    try:
        app = Flask(__name__)
        logging.info("Flask app create 완료.")
    except Exception as e:
        logging.error(f"Failed to create Flask app\nFile: {__file__}\nError code: {e}")

    try:
        app.config.from_object(Config)
        logging.info("loadConfig.py 불러오기 완료")
    except Exception as e:
        logging.error(f"Failed to load loadConfig.py.\nFile: {__file__}\nError code: {e}")
    
    try:
        success = []
        app.register_blueprint(chat_bp)
        success.append('chat_bp')
        app.register_blueprint(config_bp)
        success.append('config_bp')
        app.register_blueprint(userNote_bp)
        success.append('userNote_bp')
        
        logging.info(f"Register blueprint success.\nLoad 된 blue print list: {[text for text in success]}")

        return app
    except Exception as e:
        logging.error(f"Failed to load blue print.\nFile: {__file__}\nLoad 된 blue print: {[text for text in success]}")