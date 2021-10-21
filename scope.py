import requests
import sys
import pprint
import json

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


def read_ip_file(filename):
    """ Given a filename,
        return the contents of that file
    """
    try:
        with open(filename, 'r') as f:
            for line in f:
                line_strip = line.strip()
                list_IP.append(line_strip)
    except FileNotFoundError:
        print("'%s' file not found" % filename)
    finally:
        f.close()



url_geoip = "https://api.ipgeolocation.io/"
#url_command

API_KEY = get_api_key('api_key.txt')
list_IP = []
read_ip_file('ips.txt')
#print(list_IP)
#IP_ADDR = sys.argv[1]

bulk_ip_response = requests.post('https://api.ipgeolocation.io/ipgeo-bulk?apiKey='+API_KEY, 'Content-type : application/json', {"ips":list_IP})
print(bulk_ip_response.text)
#response = requests.get('https://api.ipgeolocation.io/ipgeo?apiKey='+API_KEY+'&ip='+IP_ADDR)

#pprint.pprint(response.text)