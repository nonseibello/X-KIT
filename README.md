# X-KIT Network Security Tool

Complete network security toolkit for host discovery, port scanning, packet analysis, and OS detection.

## Installation

### One-liner (Recommended)
```bash
wget -O install.sh https://raw.githubusercontent.com/nonseibello/X-KIT/main/install.sh && chmod +x install.sh && sudo ./install.sh
Manual
Download the executable from Releases

bash
tar -xzf xkit.tar.gz
sudo cp xkit /usr/local/bin/
sudo chmod +x /usr/local/bin/xkit
## Compatibility

### For older distributions (Ubuntu 20.04, Debian 11, CentOS 7, etc.)

If you get a `GLIBC` error when running X-KIT, install the legacy version:

```bash
wget -O install_legacy.sh https://raw.githubusercontent.com/nonseibello/X-KIT/main/install_legacy.sh
chmod +x install_legacy.sh
sudo ./install_legacy.sh
Features
Host discovery (4 modes: stealth, classic, verbose, aggressive)

Port scanner with service detection and OS fingerprinting

Packet sniffer with BPF filters

Automatic dependency management (nmap, tshark)

Multi-distro support (Ubuntu, Debian, Fedora, Arch, Mint, Kali)

Logging to file with -f flag

Usage
bash
sudo xkit -c    # Classic mode
sudo xkit -v    # Verbose mode
sudo xkit -s    # Stealth mode
sudo xkit -A    # Aggressive mode
sudo xkit -f    # Save results to file
sudo xkit -n    # Disable ASCII art
sudo xkit -h    # Show help
Requirements
Linux OS

Root privileges

Dependencies (nmap, tshark) installed automatically

License
Proprietary - All rights reserved
link to tar.gz file:
https://github.com/nonseibello/X-KIT/releases/download/v1.0/xkit.tar.gz
Author
alex
tiktok:
@real_cybersecurity12
creds to:
- Scapy Team - For the packet manipulation library
- Nmap Project - For advanced scanning capabilities
- PyShark Team - For Wireshark integration
And also , im going to soon add many more functionalities!
