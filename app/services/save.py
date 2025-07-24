import json
import logging
from pathlib import Path

def update_save(payload):
    """
    Updates the conversation and image data in data/user/save.json.

    Args:
        payload (dict): A dictionary containing the following keys:
            - "conversation" (dict): A conversation object with:
                - "user" (str): User's message.
                - "gpt" (str): GPT's response.

    Returns:
        str: Success message ("Save success!") or error message with details.

    Raises:
        Exception: If saving the file fails due to IO or JSON errors.
    """
    try:
        conversation = payload.get("conversation")
        user_conversation = conversation.get("user")
        gpt_conversation = conversation.get("gpt")

        if not user_conversation or not gpt_conversation:
            raise ValueError("Conversation content is missing.")
    except Exception as e:
        logging.error(f"Can not load conversation.\nFile: {__file__}\nError code: {e}")
        raise Exception ("Can not load conversation.") from e

    try:
        path = Path(__file__).parent.parent.parent / 'data' / 'user' / 'save.json'
        with open(path, 'r', encoding = 'utf-8') as f:
            data = json.load(f)

        # load previous conversation history.
        # if emtpy -> create emtpy list
        # history : list
        # [{"user": <conversation>, "gpt": <conversation>} . . .]
        conversation_history = data.get("history", [])

        will_upload = {"user": user_conversation, "gpt": gpt_conversation}
        conversation_history.append(will_upload)
        data["history"] = conversation_history

        with open(path, 'w', encoding = 'utf-8') as f:
            json.dump(data, f, ensure_ascii = False, indent = 4)
        
        logging.info(f"Save success!\n\nUser : {user_conversation}\nGpt : {gpt_conversation}")
        return True
    except Exception as e:
        logging.error(f"Can not load data/user/save.json.\nFile: {__file__}\nError code: {e}")
        raise Exception ("Can not load data/user/save.json") from e