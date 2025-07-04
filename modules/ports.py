import subprocess
import time
import os

def run_nmap(domain, output_path, scan_type):
    print(f"\n[+] Running nmap on {domain}")
    created_time = time.strftime("%Y-%m-%d_%H-%M")
    nmap_dir = f"{output_path}/{created_time}"
    os.makedirs(nmap_dir, exist_ok=True)  
    
    if scan_type == "1":
        cmd = f"nmap -F -oN {nmap_dir}/nmap_fast.txt {domain}"

    elif scan_type == "2":
        ports = input("Enter specific ports (e.g., 80,443 or 22-100): ").strip() 
        cmd = f"nmap -p {ports} {domain} -oN {nmap_dir}/nmap_specific_ports.txt"

    elif scan_type == "3":
        cmd = f"nmap -p 1-65535 {domain} -oN {nmap_dir}/nmap_all_ports.txt"

    elif scan_type == "4":
        cmd = f"nmap --top-ports 100 {domain} -oN {nmap_dir}/nmap_top_ports.txt" 

    elif scan_type == "5":
        cmd = f"nmap -A {domain} -oN {nmap_dir}/nmap_aggressive_scan.txt"

    else:
        print("Invalid scan type selected.")
        return

    subprocess.run(cmd, shell=True)
    print(f"\n[+] Nmap scan finished successfully. Results saved in: {nmap_dir}")
