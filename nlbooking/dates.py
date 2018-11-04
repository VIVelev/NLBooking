from datetime import date, timedelta
from parsedatetime import Calendar

__all__ = [
    "str2date",
    "get_dates",
]


def str2date(a, verbose=False):
    struct, status = Calendar().parse(a)
    if status == 0:
        if verbose:
            print(f"Unable to recognize date in \"{a}\".")
        return date.today()

    return date(*struct[:3])

def get_dates(a, verbose=False):
    if verbose:
        print()
        print('-'*100)
        print("\tRunning `get_dates`...")
        print('-'*100)

    tokens = a.split(' ')
    if verbose:
        print("Tokens:", tokens, '\n')

    ########## Extract Check In String ##########
    ci_str = None
    if "from" in tokens and tokens.index("from")+1 < len(tokens):
        ci_str = tokens[tokens.index("from")+1]

    elif "for" in tokens and tokens.index("for")+1 < len(tokens):
        after_for = tokens[tokens.index("for")+1]
        if after_for == "a" and tokens.index("for")+2 < len(tokens):
            ci_str = "for a " + tokens[tokens.index("for")+2]
        else:
            ci_str = "for " + after_for

    else:
        pass

    ########## Extract Check Out String ##########
    co_str = None
    if "for" in tokens and tokens.index("for")+1 < len(tokens):
        after_for = tokens[tokens.index("for")+1]
        if after_for == "a" and tokens.index("for")+2 < len(tokens):
            co_str = "for a " + tokens[tokens.index("for")+2]
        else:
            co_str = "for " + after_for

    elif "till" in tokens and tokens.index("till")+1 < len(tokens):
        co_str = tokens[tokens.index("till")+1]

    elif "until" in tokens and tokens.index("until")+1 < len(tokens):
        co_str = tokens[tokens.index("until")+1]

    elif "to" in tokens and tokens.index("to")+1 < len(tokens):
        tmp = tokens[tokens.index("to")+1]
        if (tmp in ["tomorrow", "monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]
            or r"[0-9]" in tmp):
            co_str = tmp

    else:
        pass

    ##############################################

    if verbose:
        print("Check In String:", ci_str)
        print("Check Out String:", co_str)

    ###############################################

    if ci_str is None and co_str is None:
        return None
        
    elif ci_str is None:
        co = str2date(co_str, verbose=verbose) - timedelta(1, 0, 0)
        return f"None-{co.year}/{co.month}/{co.day}"

    elif co_str is None:
        ci = str2date(ci_str, verbose=verbose)
        return f"{ci.year}/{ci.month}/{ci.day}-None"

    else:
        ci = str2date(ci_str, verbose=verbose)
        co = ci + (str2date(co_str, verbose=verbose) - date.today()) - timedelta(1, 0, 0)
        return f"{ci.year}/{ci.month}/{ci.day}-{co.year}/{co.month}/{co.day}"
