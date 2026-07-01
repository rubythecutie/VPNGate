import sys
import vpngate.api

if len(sys.argv) > 1:
    if sys.argv[1] == "list":
        servers = vpngate.api.servers()
        for server, details in servers.items():
            print(server.ljust(15), details["country"].ljust(2))
    if sys.argv[1] == "connect":
        if len(sys.argv) < 3:
            print("Server not specified")
            sys.exit(1)

        servers = vpngate.api.servers()
        print(servers[sys.argv[2]]["openvpn"])
else:
    print("No arguments specified.")