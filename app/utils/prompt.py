import json
import logging

def prompt_loader():
    # TODO: load prompt from json
    pass

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