import sys
import vpngate.api
import vpngate.openvpn

if len(sys.argv) > 1:
    if sys.argv[1] == "list":
        servers = vpngate.api.servers()
        for server, details in servers.items():
            print(server.ljust(15), details["country"].ljust(2))
    elif sys.argv[1] == "connect":
        if len(sys.argv) < 3:
            print("Server not specified")
            sys.exit(1)

        servers = vpngate.api.servers()
        vpngate.openvpn.connect(servers[sys.argv[2]]["openvpn"])
    elif sys.argv[1] == "disconnect":
        vpngate.openvpn.disconnect()
else:
    print("No arguments specified.")