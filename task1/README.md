# Task 1 - Docker Installation and Configuration on Linux

## Overview
This task involves setting up Linux on VirtualBox, installing Docker and Docker Compose, and configuring Docker to run without `sudo`.

## Steps Performed
1. Installed Linux (Ubuntu 22.04 LTS(Jammy Jellyfish) on VirtualBox.
2. Configured network settings for VirtualBox (NAT).
3. Installed Docker and Docker Compose on Linux.
4. Set up Docker to run without `sudo`.
5. Set up SSH access to the VirtualBox Linux system.

## Commands Used

### Step 1: Install Docker
```bash
sudo apt update && sudo apt upgrade -y

sudo apt install -y  \ ca-certificates \ curl \ gnupg \ lsb-release

sudo mkdir -p /etc/apt/keyrings

curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /etc/apt/keyrings/docker.gpg

echo "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null

sudo apt update

sudo apt install -y docker-ce docker-ce-cli containerd.io

docker --version

sudo apt-get install docker-compose-plugin

sudo usermod -aG docker $USER

docker-compose --version

docker run hello-world


---

#### **4. Commit and Push to GitHub**

1. Stage and commit your work:
```bash
git add .
git commit -m "Complete Task 1: Docker setup on Linux"

git push origin main



