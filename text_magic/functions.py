from string import punctuation


PUNCTUATIONS = punctuation + "“”"


def clean_to_lower(text:str) -> str:
    return text.lower()

def clean_punctuation(text:str) -> str:
    output_string = ""
    for character in text:
        if character not in PUNCTUATIONS:
            output_string += character
    return output_string

def clean_strip(text:str) -> str:
    for _ in range(10):
        text = text.replace("  ", " ")
    return text.strip()

def pipeline(text:str) -> str:
    text = clean_to_lower(text)
    text = clean_punctuation(text)
    text = clean_strip(text)
    return text
