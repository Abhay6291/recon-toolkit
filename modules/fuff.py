import subprocess
import time
import os
from urllib.parse import urlparse

def run_ffuf(url, wordlist, base_path):
    print(f"\n[+] Running ffuf on {url}")
    
    created_time = time.strftime("%Y-%m-%d_%H-%M")
    ffuf_dir = f"{base_path}/{created_time}"
    os.makedirs(ffuf_dir, exist_ok=True)

    parsed = urlparse(url)
    safe_filename = parsed.netloc.replace('.', '_').replace('/', '_')
    output_file = f"{ffuf_dir}/ffuf_{safe_filename}.json"

    cmd = f"ffuf -w {wordlist} -u {url} -o {output_file} -of json"
    subprocess.run(cmd, shell=True)
    
    print(f"\n[+] Fuzzing finished successfully. Results saved in: {output_file}")
