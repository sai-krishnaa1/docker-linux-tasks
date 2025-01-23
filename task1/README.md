# Docker and Docker Compose Installation Guide for Ubuntu

# Step 1: Update and upgrade your system
sudo apt update
sudo apt upgrade -y

# Step 2: Install required packages
sudo apt install -y \
    ca-certificates \
    curl \
    gnupg \
    lsb-release

# Step 3: Set up Docker's official GPG key
sudo mkdir -p /etc/apt/keyrings
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /etc/apt/keyrings/docker.gpg

# Step 4: Set up the Docker repository
echo \
"deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/ubuntu \
$(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null

# Step 5: Install Docker
sudo apt update
sudo apt install -y docker-ce docker-ce-cli containerd.io

# Step 6: Verify Docker installation
docker --version

# Step 7: Install Docker Compose
sudo curl -L "https://github.com/docker/compose/releases/download/$(curl -s https://api.github.com/repos/docker/compose/releases/latest | grep -oP '"tag_name": "\K(.*)(?=")')/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose

# Step 8: Make Docker Compose executable
sudo chmod +x /usr/local/bin/docker-compose

# Step 9: Verify Docker Compose installation
docker-compose --version

# Step 10: Add your user to the Docker group
sudo usermod -aG docker $USER

# Step 11: Test Docker installation
docker run hello-world

# Additional steps for task documentation

# Clone the repository (replace <your-username> with your actual GitHub username)
git clone https://github.com/<your-username>/docker-linux-tasks.git

# Navigate to the task directory
cd docker-linux-tasks
cd task1

# Create a README file
echo "# Task 1 - Docker Installation" > README.md

# Commit and push changes
git add .
git commit -m "Add Task 1"
git push origin main

echo "Docker and Docker Compose installation complete!"
echo "Please log out and log back in for group changes to take effect."
