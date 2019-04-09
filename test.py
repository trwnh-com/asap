from pyld import jsonld as jld
import json
import requests
import pprint

url = "https://mastodon.social/@trwnh.json"
response = requests.get(url)
test = response.json()

pp = pprint.PrettyPrinter(indent=2)
pp.pprint(test)

# print("Ⴟ")