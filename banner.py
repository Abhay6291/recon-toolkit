# banner.py

import random

# ANSI color codes
RED = "\033[91m"
GREEN = "\033[92m"
CYAN = "\033[96m"
RESET = "\033[0m"

# Recon tips list
TIPS = [
    "Subfinder + HTTPX = Clean live subdomains",
    "Try /robots.txt and /sitemap.xml in FFUF",
    "Waybackurls might expose admin panels 👀",
    "Feroxbuster is recursive by default 🔁",
    "Use different wordlists for APIs and JS files",
    "Nmap -A gives you OS, services & versions 🎯",
    "Run tools on multiple targets with a loop 🌀",
    "Check URLs with parameters for LFI or RCE ⚙️",
    "Use -mc 200 with FFUF to filter valid pages ✅",
    "Combine output files for mega wordlists 📁"
]

def show_banner():
    print(CYAN + r'''


   ___                                             _  __     _      _
  | _ \    ___     __      ___    _ _       o O O | |/ /    (_)    | |_
  |   /   / -_)   / _|    / _ \  | ' \     o      | ' <     | |    |  _|
  |_|_\   \___|   \__|_   \___/  |_||_|   TS__[O] |_|\_\   _|_|_   _\__|
_|"""""|_|"""""|_|"""""|_|"""""|_|"""""| {======|_|"""""|_|"""""|_|"""""|
"`-0-0-'"`-0-0-'"`-0-0-'"`-0-0-'"`-0-0-'./o--000'"`-0-0-'"`-0-0-'"`-0-0-'
                --- Automated Recon Toolkit ---

    ''' + RESET)
    print(GREEN + f"Tip: {random.choice(TIPS)}\n" + RESET)
