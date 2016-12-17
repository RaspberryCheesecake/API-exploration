import requests
import json

response = requests.get("http://api.open-notify.org/astros.json")

if response.status_code != 200:
    print response.status_code

data = response.json()

print "The number of people currently in space is : %i " % data["number"]

max_name = max(len(member["name"]) for member in data["people"])
max_craft = max(len(member["craft"]) for member in data["people"])

print "They are :\n"
print "|".join(["Name".ljust(max_name),"Craft"])
print "-" * max_name + "|" + "-" * (max_craft + 2)

for member in data["people"]:
    print "|".join([member["name"].ljust(max_name), member["craft"]])
