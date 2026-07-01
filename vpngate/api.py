import requests

def servers():
    servers = {}
    data = requests.get("http://www.vpngate.net/api/iphone/").text.split("\n")[2:-2]

    for i in data:
        temp = i.split(",")
        servers[temp[0]] = {"ip": temp[1], "country": temp[6], "openvpn": temp[-1]}

    return servers