import json

# def text_to_json(text_input):
#     """
#     Converts ChatGPT text response to JSON format.

#     Args:
#         text_input (str): Raw text output from ChatGPT.  
#             Example:
#             Here is your JSON!
#             {
#                 "image": <image_URL>,
#                 "conversation": "Today's wether . . ."
#             }

#     Returns:
#         dict: Parsed JSON object with keys:
#             - "image" (str): Image URL
#             - "conversation" (str): ChatGPT response message

#     Raises:
#         ValueError: If the text does not contain valid JSON.
#         json.JSONDecodeError: If JSON parsing fails.
#     """
#     pass

def json_to_text(json_input):
    """
    Converts user json response to text format.

    Args:
        json_input (dict): Raw json output from user.  
            Example:
            {
                "message" : "Good bye.",
                "data" : {
                    "images" : <image_URL>,
                    "previous" : {
                        "prev_1" : {
                            "user" : "How's the . . ."
                            "gpt" : "It's . . ."
                        },
                        ...
                        "prev_10" : {
                            "user" : "How's the . . ."
                            "gpt" : "It's . . ."
                        }
                    }
                }
            }

    Returns:
        str: gpt-readable string representing the contents of the JSON.

    Raises:
        KeyError: If required fields are missing from the input dictionary.
    """
    pass