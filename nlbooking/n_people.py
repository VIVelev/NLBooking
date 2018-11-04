__all__ = [
    "get_n_adults",
    "get_n_children",
]


def get_n_adults(a, verbose=False):
    if verbose:
        print()
        print('-'*100)
        print("\tRunning `get_n_adults`...")
        print('-'*100)

    tokens = a.split(' ')

    if "adults" in tokens:
        idx = tokens.index("adults")
    elif "adult" in tokens:
        idx = tokens.index("adult")
    else:
        idx = None
    
    if idx is None:
        return None
    else:
        return tokens[idx-1]

def get_n_children(a, verbose=False):
    if verbose:
        print()
        print('-'*100)
        print("\tRunning `get_n_children`...")
        print('-'*100)

    tokens = a.split(' ')

    if "children" in tokens:
        idx = tokens.index("children")
    elif "child" in tokens:
        idx = tokens.index("child")
    elif "kids" in tokens:
        idx = tokens.index("kids")
    elif "kid" in tokens:
        idx = tokens.index("kid")
    else:
        idx = None

    if idx is None:
        return None
    else:
        return tokens[idx-1]
