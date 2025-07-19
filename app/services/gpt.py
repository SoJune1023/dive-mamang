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

def gpt_send(client, model, prompt, message):
    """
    Chat-GPT에게 message를 보내고, 응답을 구조화된 형태로 받습니다.

    Args:
        client (OpenAI): chat-gpt의 client 인스턴스.
        model (str) : 사용할 chat-gpt의 model.
        prompt (str) : chat-gpt가 자신을 정의하는 prompt입니다.
        message (str) : user가 chat-gpt에게 보낼 메시지.

    Returns:
        response.output_parsed: 다음 구조를 따릅니다:
            - response_text (List[TextFormat]):
                - message (str): 대화 내용
                - context (str): 해당 메시지의 상황/맥락
            - image (str): 이미지 URL

    Raises:
        RuntimeError: chat-gpt의 응답 받기에 실패한 경우.
    """
    try:
        response = client.responses.parse(
            model = model,
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
        return response.output_parsed
    except Exception as e:
        raise RuntimeError("Failed to get response from chat-gpt") from e