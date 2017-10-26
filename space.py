#import libraries
import requests
from collections import Counter

#initiate dicitonary
data = {}

#get the response from the API endpoint.
response = requests.get('http://api.open-notify.org/astros.json')

#return the JSON formatted information to ur data dictionary
data = response.json()

#output data in a friendly way
print("\n Welcome to the Astronaut in Space tool. \n")
print("\t With this tool, you will receive information about all " + "the astronauts currently in space.\n")

astronauts = str(data["number"])
print("There are " + astronauts + " astronauts.")
number = 0

for astroData in data["people"]:
    if (astroData["craft"] == "ISS"):
        number+=1
        print("Astronaut " + str(number) + ": " + "\n\t" + astroData["name"])
