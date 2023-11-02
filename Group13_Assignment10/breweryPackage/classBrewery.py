# classBrewery.py 

# Name: Brianna Cruz and Abby Buysse
# email: cruzbm@mail.uc.edu and buyssead@mail.uc.edu
# Assignment Title: Assignment 10
# Due Date: 20231109
# Course: IS 4010
# Semester/Year: Fall 2023
# Brief Description: This project demonstrates we can use an API to get data 
# Citations: N/A
# Anything else that's relevant: N/A

import requests 
import json 

class Brewery: 
    # this pulls a list of breweries from an open API
    response = requests.get('https://api.openbrewerydb.org/v1/breweries')
    json_string = response.content
    parsed_json = json.loads(json_string) # Now we have a python dictionary
    
    # creating a variable to use in our for loop that lets us know what dictionary 
    # from the list of dictionaries to print
    number = 0
    
    # fancy print statement that lets us know what this data is 
    print("A list of all the brewery names in the database:")
    
    # a loop that prints the name from all 50 dictionaries from the list from the API 
    for breweries in range(0,50):
        print(parsed_json[number]['name'])
        number = number + 1
    