import subprocess
import time
import os
from urllib.parse import urlparse

def run_feroxbuster(url, wordlist, output_path):
    print(f"\n[+] Running Feroxbuster on {url}")
    
    # Timestamped output directory
    created_time = time.strftime("%Y-%m-%d_%H-%M")
    ferox_dir = f"{output_path}/{created_time}"
    os.makedirs(ferox_dir, exist_ok=True)  # ✅ Fixed

    # Clean filename from URL
    parsed = urlparse(url)
    filename = parsed.netloc.replace('.', '_')

    output_file = f"{ferox_dir}/ferox_{filename}.txt"
    cmd = f"feroxbuster -u {url} -w {wordlist} -x php,html,txt,json -o {output_file} -q"
    subprocess.run(cmd, shell=True)
    
    print(f"\n[+] Feroxbuster finished successfully. Results saved in: {output_file}")
