import requests
import json

def get_who_in_space():
    response = requests.get("http://api.open-notify.org/astros.json")
    
    if response.status_code != 200:
        print "I failed with error code %i " % response.status_code

    data = response.json()
    return data

def display_who_in_space(data):
    output = ""
    output += "The number of people currently in space is : %i\n" % data["number"]
    
    max_name = max(len(member["name"]) for member in data["people"])
    max_craft = max(len(member["craft"]) for member in data["people"])
    
    output += "They are :\n"
    output += "|".join(["Name".ljust(max_name),"Craft"]) + "\n"
    output += "-" * max_name + "|" + "-" * (max_craft + 2) + "\n"
    
    for member in data["people"]:
        output += "|".join([member["name"].ljust(max_name), member["craft"]]) + "\n"

    print output
    return output

if __name__ == "__main__":
    display_who_in_space(get_who_in_space())
