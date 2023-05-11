import re

def remove_proper_names(text: str) -> str:
    pattern = r'[\"\'«\(\[\{\\].*?[\"\'»\)\]\}\\]'
    return re.sub(pattern, '', text)