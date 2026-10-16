


# X-KIT

Network security toolkit for Linux: port scanning, host discovery, packet sniffing, and wordlist generation.

## ⚠️ LEGAL DISCLAIMER — READ BEFORE USE

**X-KIT is provided strictly for authorized security testing, educational purposes, and use on networks and systems you own or have explicit written permission to test.**

By downloading, installing, running, or otherwise using this software, you agree to the following:

### 1. Authorized Use Only

You may use X-KIT **only** on:
- Systems and networks you own personally
- Systems and networks where you have **prior written authorization** from the owner
- Isolated lab environments specifically designated for security testing
- CTF (Capture The Flag) competitions where the rules permit such tools

### 2. Prohibited Use

You may **NOT** use X-KIT to:
- Scan, probe, attack, or access any system or network without explicit written permission
- Intercept, capture, decrypt, or analyze network traffic you are not authorized to access
- Perform ARP spoofing, man-in-the-middle attacks, or packet injection on any network you do not own
- Harvest credentials, personal data, or any information belonging to third parties
- Bypass security controls, authentication mechanisms, or access restrictions
- Violate any local, national, or international law

### 3. Legal Consequences

Unauthorized use of this software may constitute a **criminal offense** in most jurisdictions, including but not limited to:

- **Italy**: Art. 615-ter, 615-quater, 615-quinquies, 617-ter, 617-quater, 635-bis, 635-ter, 635-quater of the Penal Code (Codice Penale)
- **European Union**: Directive 2013/40/EU on attacks against information systems
- **United States**: Computer Fraud and Abuse Act (CFAA), 18 U.S.C. § 1030
- **United Kingdom**: Computer Misuse Act 1990
- **Germany**: StGB § 202a, § 202b, § 202c, § 303a, § 303b
- **France**: Articles 323-1 to 323-8 of the Code Pénal

Penalties include imprisonment, criminal fines, civil liability, and permanent criminal record.

### 4. No Warranty

This software is provided "AS IS", without warranty of any kind, express or implied, including but not limited to the warranties of merchantability, fitness for a particular purpose, and noninfringement.

The author makes **no guarantee** that:
- The software is accurate, reliable, or error-free
- The software will detect all hosts, ports, or services
- The software will not cause network disruption, data loss, or service interruption
- Any output produced by the software is correct or complete

### 5. Limitation of Liability

**IN NO EVENT SHALL THE AUTHOR, CONTRIBUTORS, OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES, OR OTHER LIABILITY**, whether in an action of contract, tort, or otherwise, arising from, out of, or in connection with the software or the use or other dealings in the software.

This includes, without limitation:
- Direct, indirect, incidental, special, consequential, or punitive damages
- Loss of profits, revenue, data, or use
- Business interruption or network downtime
- Legal fees, fines, or penalties incurred by the user
- Any harm caused to third parties by the user

### 6. User Responsibility

**The user assumes full and sole responsibility** for:
- Ensuring they have legal authorization to use this tool in their jurisdiction and context
- Any actions taken using this software
- Any consequences, legal or otherwise, resulting from such actions
- Complying with all applicable local, state, national, and international laws
- Obtaining any required permissions, licenses, or authorizations

### 7. No Endorsement

The author does not endorse, encourage, or condone the use of this software for any illegal, unethical, or unauthorized purpose. The existence of this software does not constitute permission to use it against any system or network.

### 8. Indemnification

You agree to indemnify, defend, and hold harmless the author and any contributors from and against any and all claims, liabilities, damages, losses, or expenses (including reasonable legal fees) arising out of or in any way connected with your use of this software.

---

**If you do not agree with any part of this disclaimer, do not download, install, or use X-KIT.**

---

## Features

- Host Discovery (4 modes: stealth, classic, verbose, aggressive)
- Port Scanner with service detection and OS fingerprinting
- Packet Sniffer with BPF filter support
- MITM / ARP spoof mode (advanced users only — see disclaimer)
- Nameforger wordlist generator
- JSON export with `--json <file>`
- Logging to file with `-f`
- Multi-distro support (Ubuntu, Debian, Fedora, Arch, Mint, Kali)
  
installation:
  ### One-liner (Recommended)
```bash
wget -O install.sh https://raw.githubusercontent.com/nonseibello/X-KIT/main/install.sh && chmod +x install.sh && sudo ./install.sh
Manual
Download the executable from Releases

bash
tar -xzf xkit.tar.gz
sudo cp xkit /usr/local/bin/
sudo chmod +x /usr/local/bin/xkit
