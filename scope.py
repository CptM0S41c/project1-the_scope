import requests
import sys
import pprint
import json



# method to read and store api key
def get_api_key(filename):
    """ Given a filename,
        return the contents of that file. Put your api key in a file.
    """
    try:
        with open(filename, 'r') as f:
            # It's assumed our file contains a single line,
            # with our API key
            return f.read().strip()
    except FileNotFoundError:
        print("'%s' file not found" % filename)

#method to read ip address and return an  array.
def read_ip_file(filename):
    """ Given a filename,
        return the contents of that file. put ip address at each line
    """
    list_IP = []
    try:
        with open(filename, 'r') as f:
            for line in f:
                line_strip = line.strip()
                list_IP.append(line_strip)
    except FileNotFoundError:
        print("'%s' file not found" % filename)
    finally:
        print(list_IP)
        return list_IP
        f.close()

#method to send ip adress to ipgeolocation api
def send_IP_address(ip_address):
    """
        need ip address input(array or single no problem). and return Json object.
    """
    ret_IP_address = []
    API_KEY = get_api_key('api_key.txt')
    url_geoip = "https://api.ipgeolocation.io/"
    url_command = 'ipgeo?apiKey='+API_KEY+'&ip='
    print("value of the array ip_address:"+str(len(ip_address)))
    if len(ip_address) > 1 :
        for ip in ip_address:
            #print(url_geoip+url_command+ip)
            response = requests.get(url_geoip+url_command+ip)
            #print(response.text)
            ret_IP_address.append(response.text)
    else:
        response = requests.get(url_geoip+url_command+ip_address[0]) 
        #print(response.text)
        ret_IP_address.append(response.text)
    return ret_IP_address


#end of method, start on how the script behave
ip = []
print(len(sys.argv))
if len(sys.argv) > 1 :
    print(sys.argv[1])
    ip.append(sys.argv[1])
    geoIP_return = send_IP_address(ip)
    print(geoIP_return)
else:
    ip = read_ip_file('ips.txt')
    geoIP_return = send_IP_address(ip)  