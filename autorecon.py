# main.py

import os
import time
from modules import subdomains, probing, ports, waybackurl, ferox, fuff
from banner import show_banner

def main():
    print("\nChoose a tool:")
    print("1. Subfinder (Subdomain Enumeration)")
    print("2. HTTPX (Live Host Discovery)")
    print("3. Nmap (Port Scanning)")
    print("4. FFUF (Directory and parameter fuzzing/brute-forcing)")
    print("5. Waybackurls (Historical URLs)")
    print("6. Feroxbuster (Content Discovery)")
    print("7. Run All")

    choice = input("\nEnter Choice (1/2/3/4/5/6/7): ").strip()

    base_path = "output"
    domain = ""

    # Ask for domain only if needed
    if choice in ['1', '3', '5', '7']:
        domain = input("Enter target domain: ").strip()
        base_path = f"output/{domain}"
        os.makedirs(base_path, exist_ok=True)

    # Subfinder
    if choice in ['1', '7']:
        subdomains_file = subdomains.run_subfinder(domain, base_path)

    # HTTPX
    if choice == '2':
        print("Hint: The file is usually located at: output/<domain>/<timestamp>/subdomains.txt")
        input_file = input("Enter path to input file for HTTPX: ").strip()
        probing.run_httpx(input_file, base_path)
    elif choice == '7':
        probing.run_httpx(subdomains_file, base_path)

    # Nmap
    if choice in ['3', '7']:
        print("\nChoose a Scan Type:")
        print("1. Fast Scan (nmap -F)")
        print("2. Specific Ports (nmap -p)")
        print("3. All Ports (nmap -p 1-65535)")
        print("4. Top Ports (nmap --top-ports)")
        print("5. Aggressive Scan (nmap -A)")
        scan_type = input("Enter scan type (1/2/3/4/5): ").strip()
        ports.run_nmap(domain, base_path, scan_type)

    # FFUF
    if choice in ['4', '7']:
        print("\nChoose FFUF input method:")
        print("1. Use live.txt (Multiple URLs)")
        print("2. Enter single URL manually")
        url_input = input("Enter input method (1/2): ").strip()

        if url_input == "1":
            try:
                with open(f"{base_path}/live.txt") as f:
                    for url in f:
                        fuff.run_ffuf(url.strip(), "/usr/share/wordlists/dirb/common.txt", base_path)
            except FileNotFoundError:
                print("[-] live.txt not found. Run HTTPX first or check your path.")
        elif url_input == "2":
            single_url = input("Enter the URL (e.g. https://example.com): ").strip()
            fuff.run_ffuf(single_url, "/usr/share/wordlists/dirb/common.txt", base_path)
        else:
            print("[-] Invalid FFUF input option.")

    # Waybackurls
    if choice in ['5', '7']:
        waybackurl.run_wayback(domain, f"{base_path}/wayback.txt")

    # Feroxbuster
    if choice in ['6', '7']:
        print("\nChoose Feroxbuster input method:")
        print("1. Use live.txt (Multiple URLs)")
        print("2. Enter single URL manually")
        url_input = input("Enter input method (1/2): ").strip()

        if url_input == "1":
            try:
                with open(f"{base_path}/live.txt") as f:
                    for url in f:
                        ferox.run_feroxbuster(url.strip(), "/usr/share/wordlists/dirb/common.txt", base_path)
            except FileNotFoundError:
                print("[-] live.txt not found. Run HTTPX first or check your path.")
        elif url_input == "2":
            single_url = input("Enter the URL (e.g. https://example.com): ").strip()
            ferox.run_feroxbuster(single_url, "/usr/share/wordlists/dirb/common.txt", base_path)
        else:
            print("[-] Invalid Feroxbuster input option.")

    if choice == '7':
        print("\n[+] Completed full recon workflow.")

if __name__ == "__main__":
    try:
        show_banner()
        main()
    except KeyboardInterrupt:
        exit(0)
