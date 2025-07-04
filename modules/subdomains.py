import subprocess
import time
import os

def run_subfinder(domain, output_path):
    print(f"\n[+] Running Subfinder on {domain}")
    
    created_time = time.strftime("%Y-%m-%d_%H-%M")
    subf_dir = f"{output_path}/{created_time}"
    os.makedirs(subf_dir, exist_ok=True)

    output_file = f"{subf_dir}/subdomains.txt"
    cmd = f"subfinder -d {domain} -silent -o {output_file}"
    
    subprocess.run(cmd, shell=True)
    print(f"\n[+] Subfinder finished successfully. Results saved to: {output_file}")
    
    return output_file

