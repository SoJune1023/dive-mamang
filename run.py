import logging

from app import create_app

logging.basicConfig(
    level = logging.INFO,
    format = "%(asctime)s [%(levelname)s] %(message)s",
    handlers = [
        logging.FileHandler("logs/logs.log", encoding = 'utf-8'),
        logging.StreamHandler()
    ]
)

app = create_app()

if __name__ == "__main__":
    app = create_app()
    if app is not None:
        try:
            app.run(debug = True, port = 5050)
        except Exception as e:
            logging.error(f"Something went wrong\nFile: {__file__}\nError code: {e}")
    else:
        logging.error("Flask app 생성 실패로 인해 실행 불가.")
