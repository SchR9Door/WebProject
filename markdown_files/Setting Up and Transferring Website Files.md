# Setting Up and Transferring Website Files Using Docker NGINX

### **Introduction**

In this part of the project, I documented the process of transferring a website from my local machine to a remote server using **SFTP**. This guide highlights key steps such as navigating directories, creating remote folders, and recursively transferring files using SFTP commands.

---

### **Prerequisites**

1. A working **SSH connection** to the remote server.
2. **SFTP access** enabled on the server.
3. Properly configured **private and public keys** for authentication (or a password for login).
4. The website files stored in a local directory.

---

### **Step 1: Preparing the Local Environment**

The local folder containing the website files was located at `X:\for VM 01\Progekts\Web`, consisting of:

- A **compressed archive** (`apache.zip`).
- A `public` folder with subdirectories containing **HTML, CSS, JavaScript, PHP**, and image files.

---

### **Step 2: Starting SFTP and Connecting to the Server**

To initiate an SFTP session, I used the following command:

```bash
bash
sftp -i "X:\for VM 01\Progekts\Web" -P 22 merlin@192.168.188.94

```

**Issue Encountered:**

The following warning appeared due to overly permissive permissions on the private key file:

```bash
bash
WARNING: UNPROTECTED PRIVATE KEY FILE! Permissions for 'X:\\for VM 01\\Progekts\\Web' are too open.

```

**Solution:**

I resolved this by either restricting file permissions on the private key or switching to password-based authentication.

---

### **Step 3: Navigating the Remote Directory**

After successfully connecting to the server, I created a directory to store the website files:

```bash
bash
mkdir web
cd web
pwd

```

**Output:**

```bash
bash
Remote working directory: /home/merlin/web

```

---

### **Step 4: Transferring Files Recursively**

To upload all files and subdirectories from the local `public` folder to the `/web` directory on the server, I used the `put -r` command:

```bash
bash
lcd "X:\\for VM 01\\Progekts\\Web"
put -r .

```

---

### **Step 5: Verifying the Uploaded Files**

To ensure all files were transferred successfully, I listed the contents of the remote directory:

```bash
bash
ls -a

```

**Example of the Remote Directory Structure:**

```bash
bash
/web/
    apache.zip
    public/auth/
    public/bei/
    public/t1/t2/

```

---

### **Key Commands Used**

| Command | Description |
| --- | --- |
| `sftp -i <identity_file>` | Starts an SFTP session with private key authentication. |
| `lcd <path>` | Changes the local working directory. |
| `pwd` | Displays the current remote directory. |
| `mkdir <directory>` | Creates a new directory on the remote server. |
| `put -r <path>` | Recursively uploads files and directories. |

---

### **Conclusion**

Using SFTP, I successfully transferred all website files to the server. This process reinforced the importance of managing file permissions and demonstrated how commands like `put -r` can simplify large file transfers.

---

# **2. Installing Docker on Debian 12 (Bookworm)**

### **Introduction**

Docker is a platform for containerization, allowing developers to package applications with all dependencies into a single image. This makes it easy to run applications across different environments. In this part of the project, I installed Docker on **Debian 12 (Bookworm)** and set up a containerized environment for web hosting.

---

### **Step-by-Step Installation**

1️⃣ **Update the System:**

```bash
bash
sudo apt update
sudo apt upgrade -y

```

2️⃣ **Install Dependencies:**

```bash
bash
sudo apt install -y apt-transport-https ca-certificates curl software-properties-common

```

3️⃣ **Add Docker’s GPG Key and Repository:**

```bash
bash
curl -fsSL https://download.docker.com/linux/debian/gpg | sudo tee /etc/apt/trusted.gpg.d/docker.asc

```

Add the Docker repository to `/etc/apt/sources.list.d/docker.list`:

```
plaintext
deb [arch=amd64] https://download.docker.com/linux/debian bookworm stable

```

4️⃣ **Install Docker:**

```bash
bash
sudo apt update
sudo apt install -y docker-ce docker-ce-cli containerd.io

```

5️⃣ **Verify Docker Installation:**

```bash
bash
sudo docker --version

```

---

### **Running Docker Containers**

To test the Docker installation, I ran the **hello-world** container:

```bash
bash
sudo docker run hello-world

```

---

# **3. Setting Up an Nginx Web Server in Docker**

### **Introduction**

The final part of this project involved setting up **Nginx** in a Docker container to serve my website. This included configuring Nginx, resolving permission issues, and customizing the Nginx configuration.

---

### **Steps to Set Up Nginx**

1️⃣ **Running Nginx in Docker:**

```bash
bash
docker run -d -p 8080:80 --name nginx-container nginx

```

At first, this served the default Nginx welcome page.

2️⃣ **Mounting Custom Website Files:**

```bash
bash
docker run -d -p 8080:80 --name nginx-container \
-v /home/merlin/web/public:/usr/share/nginx/html nginx

```

Initially, I encountered a **403 Forbidden** error due to incorrect permissions.

3️⃣ **Fixing Permissions:**

```bash
bash
chmod -R 755 /home/merlin/web/public
chown -R www-data:www-data /home/merlin/web/public

```

4️⃣ **Customizing Nginx Configuration:**

I created a custom `nginx.conf` file for more control:

```
plaintext
server {
  listen 80;
  server_name localhost;
  root /usr/share/nginx/html;
  index index.html index.htm;
  location / {
    try_files $uri $uri/ =404;
  }
}

```

---

### **Conclusion**

This part of the project demonstrated how to set up a Dockerized web server with Nginx. The ability to mount website files and modify configurations dynamically made managing the website much easier.