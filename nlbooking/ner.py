import spacy
nlp = spacy.load("en_core_web_sm")

from .preprocessing import ner_preprocessing

__all__ = [
    "get_named_entities",
]


def get_named_entities(a):
    doc = nlp(ner_preprocessing(a))
    return [(x.text, x.label_) for x in doc.ents]
