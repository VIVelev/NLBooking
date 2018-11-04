import numpy as np

from nltk.chunk import RegexpParser
from nltk.tokenize import word_tokenize
from nltk.tag import pos_tag

__all__ = [
    "extract_tags",
    "get_search_tags",
]


def extract_tags(data):
    idxs = np.unique([x[0] for x in data.treepositions() if len(x) > 1])
    raw_data = [list(data[int(i)]) for i in idxs]

    tags = []
    for phrase in raw_data:
        res = ''
        for word in phrase:
            if ("NN" in word[1] and word[0] not in ["week", "tomorrow"]
                or "JJ" in word[1]
                or word[1] == "IN" and word[0] in ["near", "by", "next"]):

                res += word[0] + ' '

            else:
                pass

        if len(res) > 0:
            tags.append(res[:-1])

    return tags

def get_search_tags(a, verbose=False):
    if verbose:
        print()
        print('-'*100)
        print("\tRunning `get_search_tags`...")
        print('-'*100)

    search_tag_parser = RegexpParser("STAG: {\
        (<RB>|<RBR>|<RBS>|<VB>|<VB[A-Z]>|<IN>|<CC>)\
        (<JJ>|<JJR>|<JJS>|<DT>)\
        (<NN>|<NNS>|<NNP>|<NNPS>)+\
        }")

    pos_tags = pos_tag(word_tokenize(a))
    if verbose:
        print("Part of Speech Tags:", pos_tags, '\n')

    data = search_tag_parser.parse(pos_tags)
    if verbose:
        print("Matched Search Tags:", data)

    return extract_tags(data)
