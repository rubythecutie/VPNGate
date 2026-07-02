#!/usr/bin/python3

import sys
import vpngate.api
import vpngate.openvpn
from colorama import Fore, Back, Style

if len(sys.argv) > 1 and not sys.argv[1] == "help":
    if sys.argv[1] == "list":
        servers = vpngate.api.servers()
        for server, details in servers.items():
            print(server.ljust(15), details["country"].ljust(2), details["port"].ljust(6), details["protocol"].ljust(4))
    elif sys.argv[1] == "connect":
        if len(sys.argv) < 3:
            print("Server not specified")
            sys.exit(1)

        print(f"{Back.GREEN}{Style.BRIGHT}Connecting to {sys.argv[2]}...{Style.RESET_ALL}")
        servers = vpngate.api.servers()
        vpngate.openvpn.connect(servers[sys.argv[2]]["openvpn"])
    elif sys.argv[1] == "disconnect":
        print(f"{Back.GREEN}{Style.BRIGHT}Disconnecting from VPN...{Style.RESET_ALL}")
        vpngate.openvpn.disconnect()
elif len(sys.argv) == 1 or sys.argv[1] == "help":
    print(f"{Style.BRIGHT}VPNGate - A command-line client for SoftEther's VPN Gate{Style.RESET_ALL}\n")
    print(f"{sys.argv[0]} help - Display command-line options")
    print(f"{sys.argv[0]} connect <id> - Connect to a server")
    print(f"{sys.argv[0]} disconnect - Disconnect from VPN")
    print(f"{sys.argv[0]} list - List VPN Gate servers")
    