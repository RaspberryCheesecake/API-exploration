import requests
import json

response = requests.get("http://api.open-notify.org/astros.json")

if response.status_code != 200:
    print response.status_code

data = response.json()

print type(data)

print "The number of people currently in space is: %i " % data["number"]
print "They are:"
print "Name           |          Craft"
print "__________________________________"

for member in data["people"]:
    print " %s  | % s " % (member["name"], member["craft"])
