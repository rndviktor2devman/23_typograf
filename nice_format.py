import re

patterns = []


def text_format(text):
    for pattern, replacement in patterns:
        text = re.sub(pattern, replacement, text)
    return text