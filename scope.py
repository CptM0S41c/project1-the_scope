import requests
import sys
import pprint

url_geoip = "https://api.ipgeolocation.io/"

def get_api_key(filename):
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


url_geoip = "https://api.ipgeolocation.io/"
API_KEY = get_api_key('api_key.txt')

#print(API_KEY)

IP_ADDR = sys.argv[1]

response = requests.get('https://api.ipgeolocation.io/ipgeo?apiKey='+API_KEY+'&ip='+IP_ADDR)

pprint.pprint(response.text)