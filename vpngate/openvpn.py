import os
import base64
import requests
from colorama import Fore, Back, Style

def connect(config):
    disconnect(verbose=False)
    decoded = base64.b64decode(config).decode('utf-8')

    with open("/tmp/vpngate.ovpn", "w") as w:
        w.write(decoded)
        w.close()

    os.system("nmcli connection import type openvpn file /tmp/vpngate.ovpn")
    os.system("nmcli connection modify vpngate +vpn.data \"password-flags=0\"")
    os.system("nmcli connection modify vpngate +vpn.secrets username=vpn")
    os.system("nmcli connection modify vpngate +vpn.secrets password=vpn")
    connection = os.system("nmcli connection up vpngate")
    
    if connection == 0:
        ipinfo = requests.get("https://ipapi.co/json").json()
        print(f"{Back.GREEN}{Fore.WHITE}{Style.BRIGHT}Successfully connected to {ipinfo['country_name']}.{Style.RESET_ALL}")
    else:
        print(f"{Back.RED}{Fore.WHITE}{Style.BRIGHT}The VPN failed to connect. {Style.NORMAL}Please try again.{Style.RESET_ALL}")

def disconnect(verbose=True):
    os.system("nmcli --fields UUID,TYPE connection show --active | awk '$2 ~ /vpn|wireguard/ {print $1}' | xargs -I {} nmcli connection down uuid {}")
    connection = os.system("nmcli connection delete vpngate")
    if verbose == True:
        if connection == 0:
            print(f"{Back.GREEN}{Fore.WHITE}{Style.BRIGHT}Disconnected.{Style.RESET_ALL}")
        else:
            print(f"{Back.GREEN}{Fore.WHITE}{Style.BRIGHT}Failed to disconnectcl.{Style.RESET_ALL}")