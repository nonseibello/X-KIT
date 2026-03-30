# X-KIT Network Security Tool

Complete network security toolkit for host discovery, port scanning, packet analysis, and OS detection.

## Installation

### One-liner (Recommended)
```bash
wget -O install.sh https://raw.githubusercontent.com/nonseibello/X-KIT/main/install.sh && chmod +x install.sh && sudo ./install.sh
Manual
Download the tar.gz executable from Releases

bash
tar -xzf xkit.tar.gz
sudo cp xkit /usr/local/bin/
sudo chmod +x /usr/local/bin/xkit
## Legacy Version

If you get a gblic error , use this installer instead!

```bash
cd /tmp
wget -O install_legacy.sh https://raw.githubusercontent.com/nonseibello/X-KIT/main/install_legacy.sh
chmod +x install_legacy.sh
sudo bash install_legacy.sh
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
# LEGAL DISCLAIMER – READ CAREFULLY

## 1. Purpose and Authorized Use
This software (hereinafter "the Software") is provided **SOLELY** for:
- Security research and educational purposes in **controlled laboratory environments**
- Testing on **networks and devices exclusively owned by the user**
- Authorized penetration testing with **explicit written permission** from the network owner

## 2. Prohibited Use – EXPRESSLY FORBIDDEN
Any use of the Software on networks, systems, or devices that you do not **legally own or have explicit written authorization to test** is STRICTLY PROHIBITED.

Without limiting the generality of the foregoing, the following are EXPRESSLY FORBIDDEN:
- Packet sniffing or traffic interception on third-party networks
- Port scanning or host discovery without explicit authorization
- Any activity that may violate applicable laws including but not limited to:
  - Unauthorized access to computer systems
  - Interception of electronic communications
  - Interference with network services

## 3. NO WARRANTIES – "AS IS" CLAUSE
THE SOFTWARE IS PROVIDED **"AS IS"** AND **"AS AVAILABLE"**, WITHOUT ANY WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO:

- WARRANTIES OF MERCHANTABILITY
- WARRANTIES OF FITNESS FOR A PARTICULAR PURPOSE
- WARRANTIES OF NON-INFRINGEMENT
- WARRANTIES OF TITLE OR QUIET ENJOYMENT
- WARRANTIES OF UNINTERRUPTED OR ERROR-FREE OPERATION 

NO ORAL OR WRITTEN INFORMATION OR ADVICE GIVEN BY THE AUTHOR SHALL CREATE ANY WARRANTY.

## 4. COMPLETE DISCLAIMER OF LIABILITY
TO THE MAXIMUM EXTENT PERMITTED BY APPLICABLE LAW, **IN NO EVENT SHALL THE AUTHOR, CONTRIBUTORS, OR COPYRIGHT HOLDERS BE LIABLE FOR:**

- ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, PUNITIVE, OR CONSEQUENTIAL DAMAGES
- LOSS OF PROFITS, REVENUE, DATA, OR GOODWILL
- BUSINESS INTERRUPTION OR PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES
- PERSONAL INJURY OR PROPERTY DAMAGE
- UNAUTHORIZED ACCESS TO OR ALTERATION OF YOUR TRANSMISSIONS OR DATA

**THIS LIABILITY DISCLAIMER APPLIES REGARDLESS OF THE LEGAL THEORY** (contract, tort, negligence, strict liability, or otherwise), EVEN IF THE AUTHOR HAS BEEN ADVISED OF THE POSSIBILITY OF SUCH DAMAGES.

## 5. User Responsibility and Indemnification
BY DOWNLOADING, INSTALLING, OR USING THE SOFTWARE, YOU:

- **ACKNOWLEDGE** that you have read, understood, and agreed to this disclaimer
- **ASSUME ALL RISKS** associated with the use of the Software
- **AGREE TO INDEMNIFY, DEFEND, AND HOLD HARMLESS** the author from any claims, damages, losses, liabilities, costs, and expenses (including reasonable attorneys' fees) arising from your use of the Software or violation of this disclaimer 

## 6. Compliance with Laws
The author **DOES NOT AUTHORIZE, ENCOURAGE, OR TOLERATE** any illegal use of this Software. It is **SOLELY YOUR RESPONSIBILITY** to:
- Ensure compliance with all applicable local, state, national, and international laws
- Obtain all necessary authorizations before using the Software
- Understand the legal consequences of unauthorized network activities in your jurisdiction

**NOTICE:** In many jurisdictions, unauthorized interception of communications, port scanning, and host discovery without permission may constitute criminal offenses punishable by imprisonment and/or fines .

## 7. Export Control
The Software may be subject to export control laws. You agree to comply with all applicable export and re-export restrictions and not to transfer the Software to prohibited countries or entities.

## 8. Severability
If any provision of this disclaimer is found to be unenforceable or invalid under applicable law, such provision shall be limited or eliminated to the minimum extent necessary, and the remaining provisions shall remain in full force and effect.

## 9. Governing Law
This disclaimer shall be governed by and construed in accordance with the laws of [YOUR JURISDICTION], without regard to its conflict of laws principles.

## 10. Acknowledgment of Understanding
**BY USING THE SOFTWARE, YOU ACKNOWLEDGE THAT YOU HAVE READ THIS DISCLAIMER, UNDERSTAND ITS TERMS, AND AGREE TO BE BOUND BY THEM. IF YOU DO NOT AGREE, DO NOT DOWNLOAD, INSTALL, OR USE THE SOFTWARE.**
