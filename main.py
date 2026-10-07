import os
# At the very top of main.py, add:
import warnings
warnings.filterwarnings("ignore")

import sys
import subprocess
import platform

# PRIMA: gestisci -i PRIMA di qualsiasi import di scapy/pyshark
if "-i" in sys.argv:
    dependencies = input("install dependencies?(y/n)")
    if dependencies == "y" or dependencies == "Y":
        print("Installing dependencies...")
        
        # Try multiple methods to install pip packages
        install_methods = [
            [sys.executable, "-m", "pip", "install", "--user", "pyshark", "scapy", "python-nmap"],
            ["pip3", "install", "--user", "pyshark", "scapy", "python-nmap"],
            ["pip", "install", "--user", "pyshark", "scapy", "python-nmap"],
            [sys.executable, "-m", "pip", "install", "pyshark", "scapy", "python-nmap"]
        ]
        
        installed = False
        for method in install_methods:
            try:
                subprocess.run(method, check=True, capture_output=True)
                installed = True
                break
            except (subprocess.CalledProcessError, FileNotFoundError):
                continue
        
        if installed:
            print("Dependencies installed successfully!")
            print("Please run the tool again without -i flag.")
            sys.exit(0)
        else:
            print("Failed to install dependencies automatically.")
            print("\nPlease install manually:")
            print("  pip install --user pyshark scapy python-nmap")
            print("\nOr using your package manager:")
            print("  Ubuntu/Debian: sudo apt install python3-pyshark python3-scapy python3-nmap")
            print("  Fedora: sudo dnf install python3-pyshark python3-scapy python3-nmap")
            print("  Arch: sudo pacman -S python-pyshark python-scapy python-nmap")
            sys.exit(1)
    else:
        print("exiting...")
        sys.exit(1)

# DOPO: ora importa i moduli (le dipendenze sono già installate)
import datetime
import time
import logging
from concurrent.futures import ThreadPoolExecutor
import ipaddress
import asyncio

# Import con try/except per sicurezza
try:
    import pyshark
    import scapy
    import nmap
    from scapy.all import ARP, Ether, srp, IP, ICMP, sr1, TCP, conf
    from scapy.all import get_if_list, sniff
except ModuleNotFoundError as e:
    print(f"✗ Missing dependencies: {e}")
    print("\nPlease install required packages:")
    print("  pip install --user pyshark scapy python-nmap")
    print("\nOr run with -i flag to auto-install:")
    print("  ./xkit -i")
    sys.exit(1)

# Import dei tuoi moduli
import utils
import modes
import discovery
import sniffer
import port_scanner
import patch
import deps

# ... resto del codice uguale ...
# Applica patch per Python 3.14+
patch.apply_patches()

# Verifica e installa dipendenze
deps.check_and_install_dependencies()
deps.check_system_dependencies()

# Importa i moduli necessari
deps.import_modules()

# Verifica root
utils.check_root()

# Inizializza logging
utils.init_logging()

# ASCII Art e slogan
slogan = r"""
                                   _     _                                                         _                          _     _                                         _           _      
                              _   | |   (_)                                                       | |                    _   | |   (_)                                       | |         ( )_    
  ____ _   _ ____  ____ _   _| |_ | | _  _ ____   ____    _   _  ___  _   _    ____   ____ ____ _ | |        ____   ___ | |_ | | _  _ ____   ____    _   _  ___  _   _     _ | | ___  ___|/| |_  
 / _  ) | | / _  )/ ___) | | |  _)| || \| |  _ \ / _  |  | | | |/ _ \| | | |  |  _ \ / _  ) _  ) || |       |  _ \ / _ \|  _)| || \| |  _ \ / _  |  | | | |/ _ \| | | |   / || |/ _ \|  _ \|  _) 
( (/ / \ V ( (/ /| |   | |_| | |__| | | | | | | ( ( | |  | |_| | |_| | |_| |  | | | ( (/ ( (/ ( (_| |   _   | | | | |_| | |__| | | | | | | ( ( | |  | |_| | |_| | |_| |  ( (_| | |_| | | | | |__ 
 \____) \_/ \____)_|    \__  |\___)_| |_|_|_| |_|\_|| |   \__  |\___/ \____|  |_| |_|\____)____)____|  ( )  |_| |_|\___/ \___)_| |_|_|_| |_|\_|| |   \__  |\___/ \____|   \____|\___/|_| |_|\___)
                       (____/                   (_____|  (____/                                        |/                                  (_____|  (____/                                       
"""
ascii = r"""                                                                                                                                                                                      
XXXXXXX       XXXXXXX                 KKKKKKKKK    KKKKKKKIIIIIIIIITTTTTTTTTTTTTTTTTTTTTTT
X:::::X       X:::::X                 K:::::::K    K:::::KI::::::::IT:::::::::::::::::::::T
X:::::X       X:::::X                 K:::::::K    K:::::KI::::::::IT:::::::::::::::::::::T
X::::::X     X::::::X                 K:::::::K   K::::::KII::::::IIT:::::TT:::::::TT:::::T
XXX:::::X   X:::::XXX                 KK::::::K  K:::::KKK  I::::I  TTTTTT  T:::::T  TTTTTT
   X:::::X X:::::X                      K:::::K K:::::K     I::::I          T:::::T        
    X:::::X:::::X                       K::::::K:::::K      I::::I          T:::::T        
     X:::::::::X      ---------------   K:::::::::::K       I::::I          T:::::T        
     X:::::::::X      -:::::::::::::-   K:::::::::::K       I::::I          T:::::T        
    X:::::X:::::X     ---------------   K::::::K:::::K      I::::I          T:::::T        
   X:::::X X:::::X                      K:::::K K:::::K     I::::I          T:::::T        
XXX:::::X   X:::::XXX                 KK::::::K  K:::::KKK  I::::I          T:::::T        
X::::::X     X::::::X                 K:::::::K   K::::::KII::::::II      TT:::::::TT      
X:::::X       X:::::X                 K:::::::K    K:::::KI::::::::I      T:::::::::T      
X:::::X       X:::::X                 K:::::::K    K:::::KI::::::::I      T:::::::::T      
XXXXXXX       XXXXXXX                 KKKKKKKKK    KKKKKKKIIIIIIIIII      TTTTTTTTTTT                                                                                                                                                                                                                                                                                        
"""

if "-n" not in sys.argv:
    print(ascii)
    time.sleep(0.2)
    print(slogan)
else:
    print("welcome to X-KIT")
    print("everything you need,nothing you don't.")

# Help
if "--help" in sys.argv or "-h" in sys.argv:
    print("help list")
    print("""
        1. -v = verbose output
        2. -s = stealthy mode 
        3. -f = append all results to file
        4. -n = no ascii output
        5. -A = for aggresive mode
        6. -c = for classic mode
        """)
    sys.exit(1)

# Modalità di esecuzione
if "-v" in sys.argv:
    modes.verbose()
elif "-A" in sys.argv:
    modes.aggresive()
elif "-s" in sys.argv:
    modes.stealth()
elif "-c" in sys.argv:
    modes.classic()
elif "-n" in sys.argv:
    pass
elif "-f" in sys.argv:
    print("saving results in : results.txt")
    print("Welcome to THE tool")

# Now import everything (only if we're actually running the tool)
import datetime
import time
import logging
from concurrent.futures import ThreadPoolExecutor
import ipaddress
import asyncio

# Import with error handling
try:
    import pyshark
    import scapy
    import nmap
    from scapy.all import ARP, Ether, srp, IP, ICMP, sr1, TCP, conf
    from scapy.all import get_if_list, sniff
except Exception as e:
    print(f"Warning: Some features may be limited: {e}")
    # Set dummy values so code doesn't crash
    pyshark = None
    scapy = None
    nmap = None
# Validazione flag
valid_flags = ["-v", "-s", "-c", "-A", "-n", "-f"]
if len(sys.argv) > 1:
    if not any(flag in sys.argv for flag in valid_flags):
        print("invalid option , append -h or --help for a list of commands")
        sys.exit(1)
else:
    print("use --help or -h for a list of cmds")