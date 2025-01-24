
# Docker-linux Tasks
# Task 1 - Docker and Docker Compose Installation 

## Overview
This task involved the following steps:
1. Setting up Ubuntu (22.04 LTS)(Jammy Jellyfish) on VirtualBox.
2. Installing Docker and Docker Compose on Linux.
3. Configuring Docker to run without `sudo`.
4. Verifying the Docker installation.
5. Cloning a GitHub repository and documenting the process.

---

# Installing Linux (Ubuntu 22.04 Jammy Jellyfish) on VirtualBox

## Overview
This guide provides step-by-step instructions to:
1. Install VirtualBox on your system.
2. Download the Ubuntu 22.04 ISO file.
3. Set up and run Ubuntu 22.04 as a virtual machine in VirtualBox.

---

## Prerequisites
1. **Host Operating System**: Windows/macOS/Linux.
2. **Software**: VirtualBox installed on your system. (Download: [https://www.virtualbox.org/](https://www.virtualbox.org/))
3. **Hardware**: Minimum 4GB of RAM and sufficient disk space (at least 20GB free).

---

## Steps to Install and Set Up Ubuntu 22.04 on VirtualBox

### 1. Download Ubuntu 22.04 ISO
- Visit the official Ubuntu downloads page: [https://ubuntu.com/download/desktop](https://ubuntu.com/download/desktop).
- Select **Ubuntu 22.04 LTS (Jammy Jellyfish)** and download the ISO file.

---

### 2. Install VirtualBox
- Download VirtualBox from [https://www.virtualbox.org/](https://www.virtualbox.org/).
- Install it by following the on-screen instructions for your operating system.

---

### 3. Create a New Virtual Machine
1. Open VirtualBox and click on **New**.
2. Enter the following details:
   - **Name**: `Ubuntu 22.04`
   - **Type**: Linux
   - **Version**: Ubuntu (64-bit)
3. Allocate resources:
   - **Memory**: Minimum 2GB (4GB recommended).
   - **Hard Disk**: Create a new virtual hard disk and allocate at least 20GB.
4. Click **Create** to finalize the VM setup.

---

### 4. Configure Virtual Machine Settings
Before starting the VM:
1. **Processor**:
   - Go to **Settings > System > Processor**.
   - Allocate at least 2 CPUs.
2. **ISO File**:
   - Go to **Settings > Storage**.
   - Under **Controller: IDE**, click on the empty disk icon.
   - Select the Ubuntu ISO file downloaded earlier.
3. **Networking**:
   - Go to **Settings > Network**.
   - Set **Adapter 1** to **NAT** or **Bridged Adapter** to enable internet connectivity.

---

### 5. Install Ubuntu 22.04
1. Start the VM by clicking **Start** in VirtualBox.
2. The Ubuntu installer will launch:
   - Select your language and click **Install Ubuntu**.
   - Choose your keyboard layout.
   - Select **Normal installation** and check the box for downloading updates during installation.
   - Choose **Erase disk and install Ubuntu** (this only affects the virtual disk).
   - Set up your user account by entering a username, password, and hostname.
3. Click **Install Now** and wait for the installation to complete.

---

### 6. Finalize Installation
1. Once installation is complete, reboot the VM.
2. Remove the ISO:
   - Go to **Devices > Optical Drives > Remove Disk from Virtual Drive** in VirtualBox.
   - Reboot the VM.
3. Log in with the username and password you created.

---

## Notes
- Ensure your VirtualBox installation is up to date for compatibility with Ubuntu 22.04.
- Allocate sufficient resources (RAM, CPU, and disk space) for a smooth experience.
- NAT networking is recommended for internet connectivity in most use cases, while Bridged Adapter is suitable for SSH access.

---

## Conclusion
Ubuntu 22.04 LTS is now successfully installed and running on VirtualBox. This setup provides a fully functional Linux environment for further tasks and development work.



## These are the Steps Performed to install docker and docker compose on linux.
### 1. Install Docker
Commands used to install Docker:
```bash
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
```
---

### 2. Verify Docker Installation

Command used to check the Docker version:
```bash

docker --version
Expected output (example):

---

Docker version 24.x.x
```
###3. Install Docker Compose

Commands used to install Docker Compose:
```bash

sudo curl -L "https://github.com/docker/compose/releases/download/$(curl -s https://api.github.com/repos/docker/compose/releases/latest | grep -oP '"tag_name": "\K(.*)(?=")')/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose

sudo chmod +x /usr/local/bin/docker-compose
```
Verify the Docker Compose installation:
```bash
docker-compose --version

Expected output (example):

docker-compose version 2.x.x
```
---

###4. Configure Docker to Run Without sudo
Command used to add the current user to the docker group:
```bash
sudo usermod -aG docker $USER

Note: A reboot or re-login is required for this change to take effect.

---
```
###5. Test Docker
Command used to verify Docker functionality:
```bash
docker run hello-world
Expected output:

Hello from Docker!
```
This message shows that your installation appears to be working correctly.
---

###6. GitHub Repository Setup
Clone Repository
Commands used to clone the GitHub repository:
```bash
git clone https://github.com/sai-krishnaa1/docker-linux-tasks.git

cd docker-linux-tasks
```
Create task1 Directory:
Commands used to set up the task1 directory:

```bash
mkdir task1
cd task1

echo "# Task 1 - Docker Installation" > README.md
Commit and Push Changes
Commands used to commit and push changes to GitHub:


git add .
git commit -m "Add Task 1"
git push origin main
```
Notes:

->Docker and Docker Compose were successfully installed and verified.
->The hello-world container ran successfully, confirming the installation.
->The GitHub repository was updated with a task1 folder containing this README.md.

---

Conclusion:

-> The task was completed successfully, with Docker and Docker Compose installed and configured. The steps were documented, and the repository was updated for future tasks.




