import sys
import sniffer
import discovery
import utils
import port_scanner
import nameforger

def stealth():
    """Modalità stealth del tool"""
    print(r"""
┌─┐┌┬┐┌─┐┌─┐┬ ┌┬┐┬ ┬┬ ┬  ┌┬┐┌─┐┌┬┐┌─┐
└─┐ │ ├┤ ├─┤│  │ ├─┤└┬┘  ││││ │ ││├┤ 
└─┘ ┴ └─┘┴ ┴┴─┘┴ ┴ ┴ ┴   ┴ ┴└─┘─┴┘└─┘
""")
    
    print("""
        1.port scanner
        2.packet sniffer
        3.host discovery
        4.nameforger
        5.exit
        """)
    chose = input("chose a mode:\n")
    
    if chose == '1':
        print("port scanner")
        port_scanner.port_scanner_stealth()  
    elif chose == '2':
        print("packet sniffer")
        sniffer.sniffer_noverbose()
    elif chose == '3':
        print("host discovery")
        discovery.stealth_discovery()
    elif chose == '4':
        print("nameforger")
        nameforger.nameforger()
    elif chose == '5':
        print("exiting")
        sys.exit(1)
    else:
        print("Invalid option.")
        return stealth()

def verbose():
    """Modalità verbose del tool"""
    print(r"""
             _                              _     
 _ _ ___ ___| |_ ___ ___ ___    _____ ___ _| |___ 
| | | -_|  _| . | . |_ -| -_|  |     | . | . | -_|
 \_/|___|_| |___|___|___|___|  |_|_|_|___|___|___|                                                
""")
    print("""
        1.port scanner
        2.packet sniffer
        3.host discovery
        4.nameforger
        5.exit
        """)
    chose = input("chose a mode:\n")
    
    if chose == '1':
        print("port scanner")
        port_scanner.port_scanner_verbose()
    elif chose == '2':
        sniffer.verbose_sniffer()
    elif chose == '3':
        print("Starting host discovery...")
        discovery.verbose_discovery()
    elif chose == '4':
        print("nameforger")
        nameforger.nameforger()
    elif chose == '5':
        print("exiting")
        sys.exit(1)
    else:
        print("Invalid option.")
        return verbose()

def classic():
    """Modalità classica del tool"""
    print(r"""
       _                                                    
      | |                                            |      
  __  | |  __,   ,   ,      __     _  _  _    __   __|   _  
 /    |/  /  |  / \_/ \_|  /      / |/ |/ |  /  \_/  |  |/  
 \___/|__/\_/|_/ \/  \/ |_/\___/    |  |  |_/\__/ \_/|_/|__/
""")
    
    print("""
        1.port scanner
        2.packet sniffer
        3.host discovery
        4.nameforger
        5.exit
        """)
    chose = input("chose a mode:\n")
    if chose == '1':
        print("port scanner")
        port_scanner.port_scanner_classic()
    elif chose == '2':
        print("packet sniffer")
        sniffer.sniffer_noverbose()
    elif chose == '3':
        print("host discovery")
        discovery.host_discovery()
    elif chose == '4':
        print("nameforger")
        nameforger.nameforger()
    elif chose == '5':
        sys.exit(1)
    else:
        print("Invalid option.")
        return classic()

def aggresive():
    """Modalità aggressiva del tool"""
    print(r"""
 .--.                               _                                 .-.      
: .; :                             :_;                                : :      
:    : .--.  .--. .--.  .--.  .--. .-..-..-. .--.   ,-.,-.,-. .--.  .-' : .--. 
: :: :' .; :' .; :: ..'' '_.'`._-.': :: `; :' '_.'  : ,. ,. :' .; :' .; :' '_.'
:_;:_;`._. ;`._. ;:_;  `.__.'`.__.':_;`.__.'`.__.'  :_;:_;:_;`.__.'`.__.'`.__.'
       .-. : .-. :                                                             
       `._.' `._.'                                                             
""")
    
    print("""
        1.port scanner
        2.packet sniffer
        3.host discovery
        4.nameforger
        5.exit
        """)
    chose = input("chose a mode:\n")
    if chose == '1':
        print("port scanner")
        port_scanner.port_scanner_aggressive()
    elif chose == '2':
        print("packet sniffer")
        sniffer.sniffer_noverbose()
    elif chose == '3':
        print("host discovery")
        discovery.aggresive_discovery()
    elif chose == '4':
        print("nameforger")
        nameforger.nameforger()
    elif chose == '5':
        print("exiting")
        sys.exit(1)
    else:
        print("Invalid option.")
        return aggresive()