import sys
import json

from nlbooking import (
    transcribe,
    get_dates,
    get_locations,
    get_n_adults,
    get_n_children,
    get_price_limits,
    get_search_tags,
)


if __name__ == "__main__":

    if "--voice" in sys.argv or "-V" in sys.argv:
        search_string = transcribe()
    elif "--example" in sys.argv or "-E" in sys.argv:
        search_string = "hello i want to go to barcelona and i want my hotel to \
        have free wi-fi and a swimming pool and also i dont want to pay more the £100"
    else:
        search_string = ' '.join(sys.argv[1:])

    verbose = False
    if "--verbose" in sys.argv or "-v" in sys.argv:
        verbose = True

    data = json.dumps({
        "dates": get_dates(search_string, verbose=verbose),
        "locations": get_locations(search_string, verbose=verbose),
        "n_adults": get_n_adults(search_string, verbose=verbose),
        "n_children": get_n_children(search_string, verbose=verbose),
        "price_limits": get_price_limits(search_string, verbose=verbose),
        "search_tags": get_search_tags(search_string, verbose=verbose),
    })

    if verbose:
        print()
    print(data)


########## AI SEARCHES FOR ##########
# Dates (Check In Date - Check Out Date)
# City / Country (Location)
# Number of Adults
# Number of Children
# Price Limits
# Search Tags
#####################################
