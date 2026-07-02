import os
import base64

def connect(config):
    disconnect()
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
    os.system("nmcli --fields UUID,TYPE connection show --active | awk '$2 ~ /vpn|wireguard/ {print $1}' | xargs -I {} nmcli connection down uuid {}")
    os.system("nmcli connection delete vpngate")