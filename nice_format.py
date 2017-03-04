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
    # phone numbers
    (r'\b[\+\(]?(\d)[-\s+\(]?(\d{2,3})[-\s+\)]?\s?'
        r'(\d{2,3})[-\s]?(\d{1,3})[-\s]?(\d+)\b', r'\1(\2)\3–\4–\5'),
    # numbers followed by words
    (r'[^0-9]([а-яА-Яa-zA-Z.]+)\s?(\d+)', r' \1{}\2'.format(char_format)),
    # words followed by numbers
    (r'(\d+[.,]?\d+)\s?([€$\w]+)', r'\1{}\2'.format(char_format)),
]


def text_format(text):
    for pattern, replacement in patterns:
        text = re.sub(pattern, replacement, text)
    return text
