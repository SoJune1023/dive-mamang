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
    # TODO: return client
    pass

def gpt_send(client, prompt, message):
    try:
        response = client.responses.parse(
            model = "model",
            input = [
                {
                    "role": "system",
                    "content": prompt
                },
                {
                    "role": "user",
                    "content": message
                }
            ],
            text_format = ResponseFormat
        )

        # TODO: return result
    except Exception as e:
        raise Exception(f"Chat gpt did not response. Error code: {e}")