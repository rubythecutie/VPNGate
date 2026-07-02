import base64
import requests
import json
from pathlib import Path
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

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

def try_default_api():
    servers = {}
    try:
        data = requests.get("http://www.vpngate.net/api/iphone/", verify=False).text.split("\n")[2:-2]

        for i in data:
            temp = i.split(",")
            servers[temp[0]] = {
                "ip": temp[1].strip(),
                "country": temp[6].strip(),
                "openvpn": temp[-1].strip(),
                "port": get_port(temp[-1]).strip(),
                "protocol": get_protocol(temp[-1]).strip()
            }
        
        print("Success")
    except:
        print("Failed")
    
    return servers

def try_github_mirrors():
    server_data = {}
    mirrors = [
        "https://raw.githubusercontent.com/fdciabdul/Vpngate-Scraper-API/refs/heads/main/json/data.json",
        "https://raw.githubusercontent.com/bagussatoto/Vpngate-Scraper-API/refs/heads/main/json/data.json"
    ]

    for i in mirrors:
        print(f"Trying {i}...", end=" ")
        try:
            data = requests.get(i, verify=False)
            data = json.loads(data.text)[0]["servers"]
            for j in data:
                server_data[j["hostname"]] = {
                    "ip": j["ip"].strip(),
                    "country": j["countryshort"].strip(),
                    "openvpn": j["openvpn_configdata_base64"].strip(),
                    "port": get_port(j["openvpn_configdata_base64"]).strip(),
                    "protocol": get_protocol(j["openvpn_configdata_base64"]).strip()
                }

            print("Success")
            return server_data
        except:
            print("Failed")

def fetch_servers():
    print("Trying default API...", end=" ")
    server_data = try_default_api()
    if server_data == {}:
        server_data = try_github_mirrors()
    else:
        return {}
    return server_data