from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

__all__ = [
    "clean",
    "ner_preprocessing",
]


def clean(a):
    noise = stopwords.words("english")   
    new = []

    for x in word_tokenize(a):
        if x not in noise:
            new.append(x)
            
    return new

def ner_preprocessing(a):
    tokens = word_tokenize(a)
    prepositions = ["visit", "to", "in", "near", "by", "at", "for"]
    
    for prep in prepositions:
        idxs = [i for i, x in enumerate(tokens) if x == prep]
        for i in idxs:
            if i+1 < len(tokens) and tokens[i+1] not in prepositions:
                tokens[i+1] = tokens[i+1][0].upper() + tokens[i+1][1:]

    return ' '.join(tokens)
