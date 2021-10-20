import requests
import sys

'''
The plan is still to meet and officially start on Monday 10/18 at 8PM. However, since it is the first week I figure a few extra days to get in the swing of things wouldn't hurt. While there us no due-date, project 2 begins on 10/25

Project 1 - The Scope!

Scenario: Congrats, your Penetration testing company Red Planet has landed an external assessment for Microsoft! Your point of contact has give you a few IP addresses for you to test. Like with any test you should always verify the scope given to you to make sure there wasn't a mistake.

Beginner Task: Write a script that will have the user input an IP address. The script should output the ownership and geolocation of the IP. The output should be presented in a way that is clean and organized in order to be added to your report.

Intermediate Task:  Have the script read multiple IP addresses from a text file and process them all at once.

Expert Task:Have the script read from a file containing both single IP addresses and CIDR notation, having it process it both types.

Here are your IP addresses to check:
131.253.12.5
131.91.4.55
192.224.113.15
199.60.28.111

For the Expert Task here are two networks in CIDR notation:
20.128.0.0/16
208.76.44.0/22


Please put all discussion for this project in project1-the-scope 


    https://ipgeolocation.io/
'''

def get_file_contents(filename):
    """ Given a filename,
        return the contents of that file
    """
    try:
        with open(filename, 'r') as f:
            # It's assumed our file contains a single line,
            # with our API key
            return f.read().strip()
    except FileNotFoundError:
        print("'%s' file not found" % filename)

API_KEY = get_file_contents('api_key.txt')

#print(API_KEY)

IP_ADDR = "131.253.12.5"

response = requests.get('https://api.ipgeolocation.io/ipgeo?apiKey='+API_KEY+'&ip='+IP_ADDR)

print(response.text)