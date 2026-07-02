# VPNGate

A command-line client for SoftEther's VPN Gate.

Designed for Linux as there is no official client.

## Running

```bash
pip install requests colorama
git clone https://github.com/rubythecutie/VPNGate
cd VPNGate
python3 vpngate.py
```

## Command-line options

```
vpngate.py help - Display command-line options
vpngate.py connect <id> - Connect to a server
vpngate.py disconnect - Disconnect from VPN
vpngate.py list - List VPN Gate servers
```