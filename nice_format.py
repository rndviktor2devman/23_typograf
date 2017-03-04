import re

char_format = '\u00A0'

patterns = [
    # quotes
    (r'([\'"])(.*?)(\1)', r'«\2»'),
    # hyphen to dash
    (r'( - )', ' — '),
    # new lines
    (r'\r\n', r'\n'),
    # exceed spaces
    (r'[ ]{2,}', r' '),
    # tabs by spaces
    (r'\t', r' '),
    # exceed unix rows
    (r'\n{2,}', r'\n'),
]


def text_format(text):
    for pattern, replacement in patterns:
        text = re.sub(pattern, replacement, text)
    return text
