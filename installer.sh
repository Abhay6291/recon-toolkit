#!/bin/bash

echo "=============================================="
echo "      Automated Recon Toolkit Installer        "
echo "=============================================="

# Check for root
if [ "$EUID" -ne 0 ]; then 
  echo "[!] Please run as root: sudo ./installer.sh"
  exit
fi

echo "This might take a few minutes... Time to grab a coffee or stretch a bit!"

echo "[+] Updating package lists..."
apt update

echo "[+] Installing essential tools..."
apt install -y golang git python3 python3-pip feroxbuster nmap curl

# Install Go-based recon tools
echo "[+] Installing Subfinder..."
go install -v github.com/projectdiscovery/subfinder/v2/cmd/subfinder@latest

echo "[+] Installing HTTPX..."
go install -v github.com/projectdiscovery/httpx/cmd/httpx@latest

echo "[+] Installing FFUF..."
go install -v github.com/ffuf/ffuf@latest

# Ensure Go binaries are in PATH
export PATH=$PATH:$(go env GOPATH)/bin
echo 'export PATH=$PATH:$(go env GOPATH)/bin' >> ~/.bashrc

# Python requirements (if any)
if [ -f requirements.txt ]; then
  echo "[+] Installing Python requirements..."
  pip3 install -r requirements.txt
else
  echo "[!] No requirements.txt found — skipping Python dependencies"
fi

# Create output directory if not exists
echo "[+] Creating output directory..."
mkdir -p output

# Test installations
echo "[+] Verifying installed tools..."
which subfinder && subfinder -version
which httpx && httpx -version
which ffuf && ffuf -h | head -n 1
which feroxbuster && feroxbuster -V

echo -e "\n[✓] Setup complete! You can now run your toolkit with:"
echo "    python3 main.py"

