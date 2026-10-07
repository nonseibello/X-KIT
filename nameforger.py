import sys
import utils

def nameforger():
    """Name generator tool per wordlist"""
    
    print(f"\n{utils.CYAN}╔═════════════════════════════════════╗{utils.RESET}")
    print(f"{utils.CYAN}║  n a m e f o r g e r                ║{utils.RESET}")
    print(f"{utils.CYAN}║  ──────────────────────────────     ║{utils.RESET}")
    print(f"{utils.CYAN}║  [>] name generator tool            ║{utils.RESET}")
    print(f"{utils.CYAN}║  [>] v1.0                           ║{utils.RESET}")
    print(f"{utils.CYAN}╚═════════════════════════════════════╝{utils.RESET}\n")
    
    name = input("Enter target name: ").strip()
    
    # Validazione
    if not name:
        print(f"{utils.RED}[!] Name cannot be empty{utils.RESET}")
        return
    
    if name.isdigit():
        print(f"{utils.RED}[!] No integers, they are useless{utils.RESET}")
        return
    
    filename = input("Name of the file where to append the combinations: ").strip()
    if not filename:
        filename = "wordlist.txt"
    
    # Avviso
    print(f"\n{utils.YELLOW}[!] WARNING: This will generate approximately 9,000,000 lines{utils.RESET}")
    print(f"{utils.YELLOW}[!] The file could be several hundred MB{utils.RESET}")
    print(f"{utils.YELLOW}[!] It may take a few minutes{utils.RESET}\n")
    
    confirm = input("Continue? (y/n): ").strip().lower()
    if confirm != 'y':
        print("Aborted.")
        return
    
    def func(f, current_name):
        var = 0
        while True:
            var += 1
            f.write(f"{current_name}{var}\n")
            if var == 999999:
                var = 0
                break
        while True:
            var += 1
            f.write(f"{current_name}-{var}\n")
            if var == 999999:
                var = 0
                break
        while True:
            var += 1
            f.write(f"{current_name}.{var}\n")
            if var == 999999:
                break
    
    try:
        with open(filename, "w", encoding="utf-8") as f:
            print(f"\n{utils.GREEN}[*] Generating first million combinations...{utils.RESET}")
            f.write(name + "\n")
            func(f, name)
            utils.log(f"Nameforger: generated combinations for '{name}' (lowercase)")
            
            print(f"{utils.GREEN}[*] Generating second million combinations...{utils.RESET}")
            name_cap = name.capitalize()
            f.write(name_cap + "\n")
            func(f, name_cap)
            utils.log(f"Nameforger: generated combinations for '{name_cap}' (capitalized)")
            
            print(f"{utils.GREEN}[*] Generating last million combinations...{utils.RESET}")
            name_up = name.upper()
            f.write(name_up + "\n")
            func(f, name_up)
            utils.log(f"Nameforger: generated combinations for '{name_up}' (uppercase)")
            
            print(f"\n{utils.GREEN}[+] Done → {filename} is ready{utils.RESET}")
            utils.log(f"Nameforger: wordlist saved to {filename}")
    except Exception as e:
        print(f"{utils.RED}[!] Error: {e}{utils.RESET}")


def nameforger_cli():
    """Versione CLI per chi usa argomenti da terminale"""
    if len(sys.argv) < 2:
        print("please give an argument, append -h or --help for help")
        sys.exit(1)
    
    if sys.argv[1] in ('-h', '--help'):
        print("""Usage:  nameforger <name>

  <name>     Target name to forge combinations from

  Flags:
    -h , --help    Show this message
   """)
        sys.exit(0)
    
    if len(sys.argv) != 2:
        print("only one name at a time")
        sys.exit(1)
    
    name = sys.argv[1]
    
    if name.isdigit():
        print("no integers, they are useless")
        sys.exit(1)
    
    filename = input("name of the file where to append the combinations: ")
    
    print(f"\n{utils.YELLOW}[!] WARNING: This will generate approximately 9,000,000 lines{utils.RESET}")
    confirm = input("Continue? (y/n): ").strip().lower()
    if confirm != 'y':
        print("Aborted.")
        return
    
    def func(f, current_name):
        var = 0
        while True:
            var += 1
            f.write(f"{current_name}{var}\n")
            if var == 999999:
                var = 0
                break
        while True:
            var += 1
            f.write(f"{current_name}-{var}\n")
            if var == 999999:
                var = 0
                break
        while True:
            var += 1
            f.write(f"{current_name}.{var}\n")
            if var == 999999:
                break
    
    with open(filename, "w", encoding="utf-8") as f:
        print("generating first million combinations...")
        f.write(name + "\n")
        func(f, name)
        
        print("generating second million combinations...")
        name_cap = name.capitalize()
        f.write(name_cap + "\n")
        func(f, name_cap)
        
        print("generating last million combinations...")
        name_up = name.upper()
        f.write(name_up + "\n")
        func(f, name_up)
        
        print(f"done → {filename} is ready")


if __name__ == "__main__":
    nameforger_cli()