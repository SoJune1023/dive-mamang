import json
import logging
from pathlib import Path

def prompt_loader() -> str:
    """
    data/prompt/prompt.json에서 character의 prompt를 load하여 프롬프트로 가공
    
    Returns:
        prompt(str)

    Raises:
        Exception: prompt load 실패

    """
    try:
        path = Path(__file__).parent.parent.parent / 'data' / 'prompt' / 'prompt.json'
        with open(path, 'r', encoding = 'utf-8') as f:
            data = json.load(f)

        character_info = data["Character"]
        character_other = data["Others"]

        prompt = (
            "[ 캐릭터 정보 ]\n"
            + "\n".join(f"- {key}: {", ".join(value)}" for key, value in character_info.items())
            + "\n\n"
            + "[ 기타 ]\n"
            + "\n".join(f"- {value}" for value in character_other)
        )
        return prompt
    except Exception as e:
        logging.error(f"Could not load 'data / prompt / prompt.json.' Error code: {e}")
        raise Exception("Could not load 'data / prompt / prompt.json.'") from e

def prompt_builder(prompt: str, user_note: str) -> str:
    """
    prompt와 user_note를 받아 chat-gpt에게 보낼 하나의 프롬프트로 가공

    Args:
        prompt(str): data/prompt/prompt.json에 저장 된 prompt의 가공 결과
        user_note(str): 실시간으로 반영 되는 user_note

    Returns:
        "[ PROMPT ]
        {prompt}
        [ USER_NOTE ]
        {user_note}

    Raises:
        Exception: prompt building에 실패 한 경우
    
    """
    try:
        result = "[ PROMPT ]\n"
        +  prompt
        + "\n[ USER_NOTE ]\n"
        + user_note
        return result
    except Exception as e:
        raise Exception("Failed to build prompt") from e