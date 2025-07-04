import subprocess
import os
import time


def run_httpx(input_file, output_path):
    print("\n[+] Running HTTPX for live hosts")
    
    if not os.path.exists(input_file):
        print(f"[!] Input file not found: {input_file}")
        return
    
    created_time = time.strftime("%Y-%m-%d_%H-%M")
    httpx_dir = f"{output_path}/{created_time}"
    os.makedirs(httpx_dir, exist_ok=True)

    output_file = f"{httpx_dir}/httpx_live_hosts.txt"
    cmd = f"httpx -l {input_file} -silent -o {output_file}"

    subprocess.run(cmd, shell=True)
    print(f"\n[+] HTTPX finished successfully. Results saved in: {output_file}")
