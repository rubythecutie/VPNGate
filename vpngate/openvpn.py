import os
import base64

def connect(config):
    decoded = base64.b64decode(config).decode('utf-8')

    with open("/tmp/vpngate.ovpn", "w") as w:
        w.write(decoded)
        w.close()

    os.system("nmcli connection import type openvpn file /tmp/vpngate.ovpn")
    os.system("nmcli connection modify vpngate +vpn.data \"password-flags=0\"")
    os.system("nmcli connection modify vpngate +vpn.secrets username=vpn")
    os.system("nmcli connection modify vpngate +vpn.secrets password=vpn")
    os.system("nmcli connection up vpngate")

def disconnect():
    os.system("nmcli connection down vpngate")
    os.system("nmcli connection delete vpngate")