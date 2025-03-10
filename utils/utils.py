import re

def slugify(text: str):
    return re.sub(r'[\W_]+', '-', text)