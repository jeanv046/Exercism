import re
from collections import Counter
def count_words(phrase: str) -> Counter:
    """Count the number of words in a phrase."""
    phrase = re.sub(r"(\' | \')", " ", phrase.lower())
    phrase = re.sub(r"(^(\')+|(\')+$)", "", phrase)
    return Counter(item for item in re.split("[^a-zA-Z0-9']", phrase) if item)