import json
import re


def escape_js_message(message: str) -> str:
    """
    Escape a message for use in JavaScript code.

    Args:
        message (str): The message to escape.

    Returns:
        str: The escaped message.
    """
    return json.dumps(message)


def beautify_plan_message(message:str) -> str:
    """
    Add a newline between each numbered step in the plan message if it does not already exist.

    Args:
        message (str): The plan message.

    Returns:
        str: The plan message with newlines added between each numbered step.
    """
    # Add a newline before each numbered step that is not already preceded by a newline
    plan_with_newlines = re.sub(r'(?<!\n)( \d+\.)', r'\n\1', message)
    return plan_with_newlines
