# Natural Language Booking (NLBooking)


### How it works?
```bash
$ pipenv run python search.py [flags] [the spoken text]
```

#### Optional Flags
- `--voice` - activate voice search (`the spoken text` is not needed as an argument, speak directly)
- `--example` - shows an example output
- `--verbose` - shows verbose output

#### Example
```bash
$ pipenv run python search.py hello i want to go to barcelona and i want my hotel to have free wi-fi and a swimming pool and also i dont want to pay more the £100
{"dates": null, "locations": ["Barcelona"], "n_adults": null, "n_children": null, "price_limits": ["100"], "search_tags": ["free wi-fi", "swimming pool"]}
```

### Setup for Mac OSX
```bash
$ brew install pipenv
$ brew install portaudio
$ git clone https://github.com/VIVelev/NLBooking.git
$ cd ./NLBooking
$ bash ./setup.sh
```
