
# Docker-linux Tasks
# Task 1 - Docker Installation

## Overview
This task involved the following steps:
1. Setting up Ubuntu (22.04 LTS)(Jammy Jellyfish) on VirtualBox.
2. Installing Docker and Docker Compose on Linux.
3. Configuring Docker to run without `sudo`.
4. Verifying the Docker installation.
5. Cloning a GitHub repository and documenting the process.

---

## Steps Performed

### 1. Install Docker
Commands used to install Docker:

sudo apt update
sudo apt upgrade -y

sudo apt install -y \
    ca-certificates \
    curl \
    gnupg \
    lsb-release

sudo mkdir -p /etc/apt/keyrings

curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /etc/apt/keyrings/docker.gpg

echo \
"deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/ubuntu \
$(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null

sudo apt update

sudo apt install -y docker-ce docker-ce-cli containerd.io

---

### 2. Verify Docker Installation

Command used to check the Docker version:


docker --version
Expected output (example):

---

Docker version 22.x.x
 
###3. Install Docker Compose

Commands used to install Docker Compose:


sudo curl -L "https://github.com/docker/compose/releases/download/$(curl -s https://api.github.com/repos/docker/compose/releases/latest | grep -oP '"tag_name": "\K(.*)(?=")')/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose

sudo chmod +x /usr/local/bin/docker-compose

Verify the Docker Compose installation:

docker-compose --version

Expected output (example):

docker-compose version 2.x.x

---

###4. Configure Docker to Run Without sudo
Command used to add the current user to the docker group:

sudo usermod -aG docker $USER

Note: A reboot or re-login is required for this change to take effect.

---

###5. Test Docker
Command used to verify Docker functionality:

docker run hello-world
Expected output:

Hello from Docker!

This message shows that your installation appears to be working correctly.
---

###6. GitHub Repository Setup
Clone Repository
Commands used to clone the GitHub repository:

git clone https://github.com/sai-krishnaa1/docker-linux-tasks.git

cd docker-linux-tasks

Create task1 Directory:
Commands used to set up the task1 directory:


mkdir task1
cd task1

echo "# Task 1 - Docker Installation" > README.md
Commit and Push Changes
Commands used to commit and push changes to GitHub:


git add .
git commit -m "Add Task 1"
git push origin main

Notes:

->Docker and Docker Compose were successfully installed and verified.
->The hello-world container ran successfully, confirming the installation.
->The GitHub repository was updated with a task1 folder containing this README.md.

---

Conclusion:

-> The task was completed successfully, with Docker and Docker Compose installed and configured. The steps were documented, and the repository was updated for future tasks.




