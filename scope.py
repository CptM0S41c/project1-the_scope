import requests
import sys
import re
import json
import ipaddress



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
                #we clean the line
                line_strip = line.strip()
                #we create object ipaddress
                net = ipaddress.ip_network(line_strip)
                if net.num_addresses == 1:
                    #print("We got ip address ! "+str(line))
                    list_IP.append(line_strip)             
                else:
                    for addr in net:
                        list_IP.append(str(addr))
    except FileNotFoundError:
        print("'%s' file not found" % filename)
    finally:
        #print(list_IP)
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

def print_result(ret_from_api_json):

    for result in ret_from_api_json:
        y = json.loads(result)
        #print(y["ip"])
        print('the ip address '+y["ip"]+" belong to the organization "+y["organization"])


#end of method, start on how the script behave
ip = []
#print(len(sys.argv))
if len(sys.argv) > 1 :
    print("beginner task!")
    print(sys.argv[1])
    ip.append(sys.argv[1])
    geoIP_return = send_IP_address(ip)
    print(geoIP_return)
else:
    print("intermediate task")
    ip = read_ip_file('ips.txt')
    print('we have '+str(len(ip))+' ip address to check')
    if len(ip)> 20:
        downsize_array_of_ip = ip[0:20]
        geoIP_return = send_IP_address(downsize_array_of_ip)
        print_result(geoIP_return)
    else:
        print("expert task")
        geoIP_return = send_IP_address(ip)
        print_result(geoIP_return)