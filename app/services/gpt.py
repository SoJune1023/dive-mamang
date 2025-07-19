from openai import OpenAI
from pydantic import BaseModel

class TextFormat(BaseModel):
    message: str
    context: str

class ResponseFormat(BaseModel):
    response_text: list[TextFormat]
    image: str

def gpt_setup_client():
    # TODO: set gpt client
    pass

def gpt_send():
    # TODO: send message to gpt
    pass