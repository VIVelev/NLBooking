from .ner import get_named_entities

__all__ = [
    "get_price_limits",
]

def get_price_limits(a, verbose=False):
    if verbose:
        print()
        print('-'*100)
        print("\tRunning `get_price_limits`...")
        print('-'*100)

    return [x[0] for x in get_named_entities(a) if x[1] == "MONEY"]
