import subprocess
import time
import os

def run_wayback(domain, output_path):
    print(f"\n[+] Running waybackurls on {domain}")
    
    created_time = time.strftime("%Y-%m-%d_%H-%M")
    wayback_dir = f"{output_path}/{created_time}"
    os.makedirs(wayback_dir, exist_ok=True)

    output_file = f"{wayback_dir}/wayback_{domain.replace('.', '_')}.txt"
    cmd = f"echo {domain} | waybackurls > {output_file}"
    
    subprocess.run(cmd, shell=True)
    print(f"\n[+] Waybackurls finished successfully. Results saved in: {output_file}")
