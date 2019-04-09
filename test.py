from pyld import jsonld as jld
import json
import requests
import pprint

url = "https://mastodon.social/@trwnh.json"
response = requests.get(url)
test = response.json()

test["name"] = "infinite love Ⴟ"

pp = pprint.PrettyPrinter(indent=2)
pp.pprint(test)

# print("Ⴟ")