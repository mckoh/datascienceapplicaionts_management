from string import punctuation
from nltk.corpus import stopwords


PUNCTUATIONS = punctuation + "“”"


def clean_to_lower(text:str) -> str:
    """Changes all words in a text to lower case.

    :param text: The input text to be cleaned
    :type text: str
    :return: Cleaned output text
    :rtype: str
    """
    return text.lower()


def clean_punctuation(text:str) -> str:
    """Removes punctuation from a text."""
    output_string = ""
    for character in text:
        if character not in PUNCTUATIONS:
            output_string += character
    return output_string


def clean_strip(text:str) -> str:
    "Removes trailing whitespaces and double white spaces from the text."
    for _ in range(10):
        text = text.replace("  ", " ")
    return text.strip()


def clean_stopwords(text:str, language:str="english"):
    """Removes stopwords from a text.

    :param text: Input text to be cleaned
    :type text: str
    :param language: The stopword language to be used
    :type language: str
    :return: Cleaned text
    :rtype: str
    """
    words = text.split(" ")
    clean_text = []
    for word in words:
        if word not in stopwords.words(language):
            clean_text.append(word)
    return " ".join(clean_text)


def pipeline(text:str, **kwargs) -> str:
    text = clean_to_lower(text)
    text = clean_punctuation(text)
    text = clean_strip(text)
    text = clean_stopwords(text, **kwargs)
    return text
