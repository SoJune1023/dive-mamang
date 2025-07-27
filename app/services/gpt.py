import logging
from openai import OpenAI
from pydantic import BaseModel

class TextFormat(BaseModel):
    message: str
    context: str

class ResponseFormat(BaseModel):
    response_text: list[TextFormat]
    image: str


"""
위에서 정의한 두 class에 의하여 response : dict는 다음 형식을 따르게 됩니다.
{
    response_text: [
    {
        message: <message>
        context: <context>
    }, {
        message: <message>
        contextL <constext>
    }, . . .
    ],
    image: <image_URL>
}
"""

def gpt_setup_client(key: str, time: float, retries: int) -> OpenAI:
    # Gpt의 client를 set합니다.
    client = OpenAI(
        api_key = key,
        timeout = time,
        max_retries = retries
    )
    return client

def gpt_send(client, model, prompt, message, previous):
    """
    Chat-GPT에게 message를 보내고, 응답을 구조화된 형태로 받습니다.

    Args:
        client (OpenAI): chat-gpt의 client 인스턴스.
        model (str) : 사용할 chat-gpt의 model.
        prompt (str) : chat-gpt가 자신을 정의하는 prompt입니다.
        message (str) : user가 chat-gpt에게 보낼 메시지.
        previous (list) : 이전 대화들 ex) [{"user": <conversation>, "gpt": <conversation>}, . . .] 왼쪽에서 오른쪽 -> 오래전에서 최신

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
                {"role": "system", "content":
                    prompt
                    + "\n[ Previous conversation ]\n"
                    + [text for text in previous]},
                {"role": "user", "content": message}
            ],
            text_format = ResponseFormat
        )
        return response.output_parsed
    except Exception as e:
        logging.error(f"Failed to get response from chat-gpt\nFile: {__file__}\nError code: {e}")
        raise RuntimeError("Failed to get response from chat-gpt") from e