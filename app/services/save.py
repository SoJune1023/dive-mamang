import json

def update_save(payload):
    """
    Updates the conversation and image data in data/user/save.json.

    Args:
        payload (dict): A dictionary containing the following keys:
            - "image" (str): The image URL.
            - "conversation" (dict): A conversation object with:
                - "user" (str): User's message.
                - "gpt" (str): GPT's response.

    Returns:
        str: Success message ("Save success!") or error message with details.

    Raises:
        Exception: If saving the file fails due to IO or JSON errors.
    """