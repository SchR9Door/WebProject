# Hosting My Own Onion Website

### **Introduction**

In this project, I built and hosted a **Tor hidden service**—a personal **onion website**—using **Ubuntu Server** on a **Proxmox VM**. The goal was to learn about private web hosting on the Tor network while experimenting with virtualized environments and Nginx. This process involved initial trials with Ubuntu Desktop, followed by a transition to a headless Ubuntu Server setup for a more streamlined and secure environment.

### **Part 1: Initial Experiment with Ubuntu Desktop**

I started with **Ubuntu Desktop** to quickly get a GUI-based environment for testing.

1. **Installing Snap and OnionShare:**
    - Installed `snapd` to manage software and installed **OnionShare** for testing file sharing and basic services on the Tor network.
    - Verified the setup by connecting to the onion service using **Tor Browser** on another machine.
2. **First Website Test:**
    - Created a simple HTML site and hosted it using OnionShare.
    - Successfully accessed the site over the onion network, confirming that the service worked.

![image.png](image.png)

```bash
sudo apt install snapd
```

![image.png](image%201.png)

```bash
sudo snap install onionshare
```

![image.png](image%202.png)

```bash
onionshare
```

![image.png](image%203.png)

![image.png](image%204.png)

![image.png](image%205.png)

![image.png](image%206.png)

### **Part 2: Transition to Ubuntu Server on Proxmox**

After the initial success, I decided to set up the website on **Ubuntu Server** for better performance and control.

1. **Installing Ubuntu Server:**
    - Used **Proxmox** to create a new virtual machine with **LVM** (Logical Volume Manager) for flexible disk management.
    - Reserved unallocated space during setup for future snapshots and volume expansion.

**LVM Disk Management Configuration (Ubuntu Server)**

- Configured LVM during Ubuntu Server installation on a 32 GB disk for flexible storage management.
- Created a separate `/boot` partition (2 GB) outside LVM for system stability.
- Initialized a 29.9 GB LVM volume group (`ubuntu-vg`) with a 14.9 GB logical volume (`ubuntu-lv`) mounted as root (`/`).
- Reserved 15 GB of unallocated space for future snapshots and volume expansion.
- Implemented best practices for snapshot creation and disk resizing using `lvcreate`, `lvextend`, and `resize2fs`.

![image.png](image%207.png)

![image.png](image%208.png)

**Hosting the Website with Nginx:**

- Installed **Nginx** and uploaded my website files to `/var/www` using **SCP** (Secure Copy Protocol).

```jsx
scp C:\path\to\yourfile.html username@your-server-ip:/path/to/destination
```

![image.png](image%209.png)

![image.png](image%2010.png)

```jsx
apt update
apt install nginx
```

![image.png](image%2011.png)

Edited the Nginx configuration (`/etc/nginx/sites-available/default`) to serve my custom page.

```jsx
 sudo cp -r /home/chinas/website /var/www
```

```jsx
nano /etc/nginx/sites-available/default
```

![image.png](image%2012.png)

```jsx
nginx -t
```

![image.png](image%2013.png)

```jsx
sudo systemctl restart nginx
```

![image.png](image%2014.png)

**Configuring Tor for Hidden Services:**

- Installed **Tor** and configured it to enable hidden services by editing `/etc/tor/torrc`.
- Added the necessary configuration to publish the website on the Tor network, creating an **onion address**:

```bash

lsb_release -a
```

![image.png](image%2015.png)

![image.png](image%2016.png)

```jsx
deb [signed-by=/usr/share/keyrings/tor-archive-keyring.gpg] https://deb.torproject.org/torproject.org <DISTRIBUTION> main
deb-src [signed-by=/usr/share/keyrings/tor-archive-keyring.gpg] https://deb.torproject.org/torproject.org <DISTRIBUTION> main
```

```jsx

wget -qO- https://deb.torproject.org/torproject.org/A3C4F0F979CAA22CDBA8F512EE8CBC9E886DDD89.asc | gpg --dearmor | tee /usr/share/keyrings/deb.torproject.org-keyring.gpg >/dev/null
```

```bash
sudo apt install tor deb.torproject.org-keyring
```

```jsx
 nano /etc/tor/torrc
```

![image.png](image%2017.png)

```bash
HiddenServiceDir /var/lib/tor/hidden_service/  
HiddenServicePort 80 127.0.0.1:80  
```

![image.png](image%2018.png)

**Testing and Troubleshooting:**

- After restarting the Tor service, my website was accessible at its unique onion address:
- 👉 **smxn6c7rpd43sqekufabrwcfgbxx6zlhypqkyphpfcukm2fkaewxjcid.onion**
- Spent time troubleshooting repository issues and permissions while setting up the Tor package from the official repository.

### **Lessons Learned**

- **Virtualization:** Running this project on **Proxmox** allowed me to manage resources more efficiently and create snapshots for safe experimentation.
- **LVM for Disk Management:** LVM helped simplify disk management and provided flexibility for expanding storage in the future.
- **Security and Privacy:** Hosting a site on the **Tor network** introduced me to secure web hosting concepts and the importance of safeguarding services.

---

### **Conclusion**

This project demonstrated how to set up and manage a **Tor hidden service** in a virtualized environment. The transition from a GUI-based Ubuntu Desktop to a headless Ubuntu Server provided a better understanding of Linux server management and web hosting on the onion network. It also opened new possibilities for expanding my home lab with more secure and private services.

Future improvements might include automating the deployment process and monitoring the service for uptime and performance.

https://support.torproject.org/apt/

https://www.youtube.com/watch?v=CurcakgurRE