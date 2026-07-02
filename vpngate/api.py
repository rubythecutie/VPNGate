import base64
import requests
import json
from pathlib import Path

def get_port(config):
    config = base64.b64decode(config).decode('utf-8').split("\n")
    
    for line in config:
            if line.split(" ")[0] == "remote":
                    port = line.split(" ")[2]

    return port

def get_protocol(config):
    config = base64.b64decode(config).decode('utf-8').split("\n")
    
    for line in config:
            if line.split(" ")[0] == "proto":
                    protocol = line.split(" ")[1]

    return protocol

def servers():
    if Path("/tmp/vpngate.json").exists():
        with open("/tmp/vpngate.json", "r") as w:
            content = json.loads(w.read())
            w.close()
    else:
        with open("/tmp/vpngate.json", "w") as x:
            content = fetch_servers()
            x.write(json.dumps(content))
    return content


def fetch_servers():
    servers = {}
    data = requests.get("http://www.vpngate.net/api/iphone/").text.split("\n")[2:-2]

    for i in data:
        temp = i.split(",")
        servers[temp[0]] = {
            "ip": temp[1].strip(),
            "country": temp[6].strip(),
            "openvpn": temp[-1].strip(),
            "port": get_port(temp[-1]).strip(),
            "protocol": get_protocol(temp[-1]).strip()
        }

    return servers