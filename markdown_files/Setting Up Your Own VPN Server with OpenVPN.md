# Setting Up Your Own VPN Server with OpenVPN

In today’s interconnected world, securing online communications is more important than ever. Setting up a personal VPN server offers enhanced security, privacy, and control over your internet traffic. This guide walks you through installing and configuring OpenVPN on a Debian-based server.

---

### **1. Introduction**

OpenVPN is a versatile and widely-used VPN solution, offering robust security and flexibility. By hosting your own VPN, you eliminate the need to rely on third-party services, ensuring complete control over your data. This guide covers the steps to set up OpenVPN on a Debian-based VPS and configure clients to connect securely.

---

### **2. Preparation**

### **Choosing Your VPS**

For this project, a Debian 12 VPS was selected. The server is located in London, ensuring low-latency connections for users in the region. When choosing a VPS, consider the following:

- **Region:** Pick a server close to your primary usage area.
- **Specs:** A basic VPS with 1GB RAM and 1 vCPU is sufficient for personal use.
- **Security:** Opt for providers that offer DDoS protection and secure account management.

### **Initial Server Setup**

1. **Connect to Your VPS via SSH**
    
    ```
    ssh root@<server_ip>
    ```
    
2. **Update and Upgrade Packages**
    
    ```
    apt-get update && apt-get upgrade -y
    ```
    
3. **Install OpenSSH Client on Windows**
    
    ```
    PS Add-WindowsCapability -Online -Name OpenSSH.Client~~~~0.0.1.0
    ```
    
    ![image.png](image.png)
    
4. **Generate SSH Key on Windows**
    
    ```
    PS C:\WINDOWS\system32> ssh-keygen -t rsa -b 4096
    ```
    
    ![image.png](image%201.png)
    
5. **Create a New User**
    
    ```
    useradd -G sudo -m vpnivan
    passwd vpnivan
    ```
    
    ![image.png](image%202.png)
    
6. **Set Up SSH Key Authentication**
    
    ```
    mkdir /home/vpnivan/.ssh
    scp C:\Users\Alex\.ssh\id_rsa.pub root@<server_ip>:/home/vpnivan/.ssh/authorized_keys
    ```
    
    ![image.png](image%203.png)
    
7. **Enhance SSH Security**
Edit the SSH configuration file:
    
    ```
    nano /etc/ssh/sshd_config
    ```
    
    Change the following:
    
    ```
    Port 69
    PermitRootLogin no
    PasswordAuthentication no
    ```
    
    ![image.png](image%204.png)
    
    Restart the SSH service:
    
    ```
    systemctl restart sshd
    ```
    
8. **Verify New SSH Configuration**
Test the new setup by logging in with the SSH key:

```jsx
ssh -i C:\Users\Alex\.ssh\id_rsa vpnivan@<server_ip> -p 69
```

---

### **3. Installing OpenVPN**

### **Install Prerequisites**

To set up OpenVPN, install the required packages:

```
apt-get install openvpn easy-rsa -y
```

### **Download and Run the Installer**

A preconfigured script simplifies the installation process. Download and execute it:

```
wget https://git.io/vpn -O openvpn-install.sh
chmod +x openvpn-install.sh
bash openvpn-install.sh
```

The installation script prompts you for several configurations:

1. **Protocol:** Choose UDP (recommended) for better performance.
2. **Port:** Use port 443 to mimic HTTPS traffic and bypass potential restrictions.
3. **DNS Provider:** Select 1.1.1.1 (Cloudflare) for reliable DNS resolution.
4. **Client Name:** Provide a unique name for the client, e.g., `vpnuk`.
- Process of installing OpenVPN on a Debian-based system using an automated script
    
    ### **1. Preparation Before Installation**
    
    - The script starts with a prompt: *"OpenVPN installation is ready to begin. Press any key to continue..."*
    - It updates the system repositories by fetching package information from sources such as:
        - `http://security.debian.org/debian-security`
        - `http://deb.debian.org/debian`
    
    These repositories provide security updates and the latest software packages.
    
    ---
    
    ### **2. Checking and Installing Dependencies**
    
    - The script checks the system for the required dependencies:
        - **openssl**: Ensures secure communication and encryption.
        - **ca-certificates**: Validates SSL/TLS certificates.
    - Since these are already up-to-date on the system, they are not reinstalled.
    - Additional packages to be installed include:
        - **libip6tc2**, **liblzo2-2**, **libnetfilter-conntrack3**, **libnfnetlink0**, **libnl-3-200**, **libnl-genl-3-200**, **libpkcs11-helper1**: These are low-level libraries that support networking, packet filtering, and VPN operations.
        - **iptables**: Manages firewall rules, which are essential for VPN security.
        - **openvpn**: The primary software for creating and managing the VPN.
    
    The script ensures all these components are fetched from the Debian repositories, downloading approximately 1.2 MB of files.
    
    ---
    
    ### **3. Package Installation**
    
    - The script unpacks and installs the packages in sequence. For example:
        - `libip6tc2` is unpacked and installed, followed by `libnfnetlink0`, and so on.
    - Each library or tool is set up to be ready for use.
    - OpenVPN is the last package installed and configured. The installation process also sets up system services:
        - A symlink is created to enable the OpenVPN service (`/etc/systemd/system/multi-user.target.wants/openvpn.service`).
    
    ---
    
    ### **4. Configuration Initialization**
    
    - The script initializes the Public Key Infrastructure (PKI) environment:
        - A new PKI directory is created at `/etc/openvpn/server/easy-rsa/pki`.
        - The `ca.crt` file is generated, which acts as the root certificate for signing other certificates.
    - The system generates:
        - A server certificate and private key (`server.crt` and `server.key`).
        - A client certificate and private key (`vpnuk.crt` and `vpnuk.key`).
        - Certificate Revocation List (CRL) files to revoke compromised client keys if needed.
    
    ---
    
    ### **5. Final Steps**
    
    - OpenVPN configuration files are created and stored:
        - `/root/vpnuk.ovpn`: This file contains the client configuration for connecting to the server.
    - The OpenVPN service is restarted to apply the configuration changes.
    
    ---
    
    ### **6. Key Outcomes**
    
    - The system is now ready to run OpenVPN securely:
        - It listens on the specified port (e.g., 443).
        - It supports the chosen protocol (e.g., UDP).
        - It uses Cloudflare DNS for name resolution.
    
    This process ensures a functional OpenVPN server with proper certificates, firewall integration, and secure configurations.
    
    ```jsx
    Welcome to this OpenVPN road warrior installer!
    
    Which protocol should OpenVPN use?
       1) UDP (recommended)
       2) TCP
    Protocol [1]: 1
    
    What port should OpenVPN listen to?
    Port [1194]: 443
    
    Select a DNS server for the clients:
       1) Current system resolvers
       2) Google
       3) 1.1.1.1
       4) OpenDNS
       5) Quad9
       6) AdGuard
    DNS server [1]: 3
    
    Enter a name for the first client:
    Name [client]: vpnuk
    
    OpenVPN installation is ready to begin.
    Press any key to continue...
    Hit:1 http://security.debian.org/debian-security bookworm-security InRelease
    Hit:2 http://deb.debian.org/debian bookworm InRelease
    Hit:3 http://deb.debian.org/debian bookworm-updates InRelease
    Reading package lists... Done
    Reading package lists... Done
    Building dependency tree... Done
    Reading state information... Done
    openssl is already the newest version (3.0.15-1~deb12u1).
    openssl set to manually installed.
    ca-certificates is already the newest version (20230311).
    The following additional packages will be installed:
      libip6tc2 liblzo2-2 libnetfilter-conntrack3 libnfnetlink0 libnl-3-200 libnl-genl-3-200 libpkcs11-helper1
    Suggested packages:
      firewalld resolvconf openvpn-dco-dkms openvpn-systemd-resolved
    Recommended packages:
      easy-rsa
    The following NEW packages will be installed:
      iptables libip6tc2 liblzo2-2 libnetfilter-conntrack3 libnfnetlink0 libnl-3-200 libnl-genl-3-200 libpkcs11-helper1
      openvpn
    0 upgraded, 9 newly installed, 0 to remove and 1 not upgraded.
    Need to get 1,279 kB of archives.
    After this operation, 5,119 kB of additional disk space will be used.
    Get:1 http://deb.debian.org/debian bookworm/main amd64 libip6tc2 amd64 1.8.9-2 [19.4 kB]
    Get:2 http://deb.debian.org/debian bookworm/main amd64 libnfnetlink0 amd64 1.0.2-2 [15.1 kB]
    Get:3 http://deb.debian.org/debian bookworm/main amd64 libnetfilter-conntrack3 amd64 1.0.9-3 [40.7 kB]
    Get:4 http://deb.debian.org/debian bookworm/main amd64 iptables amd64 1.8.9-2 [360 kB]
    Get:5 http://deb.debian.org/debian bookworm/main amd64 liblzo2-2 amd64 2.10-2 [56.9 kB]
    Get:6 http://deb.debian.org/debian bookworm/main amd64 libnl-3-200 amd64 3.7.0-0.2+b1 [63.1 kB]
    Get:7 http://deb.debian.org/debian bookworm/main amd64 libnl-genl-3-200 amd64 3.7.0-0.2+b1 [21.6 kB]
    Get:8 http://deb.debian.org/debian bookworm/main amd64 libpkcs11-helper1 amd64 1.29.0-1 [51.2 kB]
    Get:9 http://deb.debian.org/debian bookworm/main amd64 openvpn amd64 2.6.3-1+deb12u2 [651 kB]
    Fetched 1,279 kB in 0s (11.9 MB/s)
    Preconfiguring packages ...
    Selecting previously unselected package libip6tc2:amd64.
    (Reading database ... 28417 files and directories currently installed.)
    Preparing to unpack .../0-libip6tc2_1.8.9-2_amd64.deb ...
    Unpacking libip6tc2:amd64 (1.8.9-2) ...
    Selecting previously unselected package libnfnetlink0:amd64.
    Preparing to unpack .../1-libnfnetlink0_1.0.2-2_amd64.deb ...
    Unpacking libnfnetlink0:amd64 (1.0.2-2) ...
    Selecting previously unselected package libnetfilter-conntrack3:amd64.
    Preparing to unpack .../2-libnetfilter-conntrack3_1.0.9-3_amd64.deb ...
    Unpacking libnetfilter-conntrack3:amd64 (1.0.9-3) ...
    Selecting previously unselected package iptables.
    Preparing to unpack .../3-iptables_1.8.9-2_amd64.deb ...
    Unpacking iptables (1.8.9-2) ...
    Selecting previously unselected package liblzo2-2:amd64.
    Preparing to unpack .../4-liblzo2-2_2.10-2_amd64.deb ...
    Unpacking liblzo2-2:amd64 (2.10-2) ...
    Selecting previously unselected package libnl-3-200:amd64.
    Preparing to unpack .../5-libnl-3-200_3.7.0-0.2+b1_amd64.deb ...
    Unpacking libnl-3-200:amd64 (3.7.0-0.2+b1) ...
    Selecting previously unselected package libnl-genl-3-200:amd64.
    Preparing to unpack .../6-libnl-genl-3-200_3.7.0-0.2+b1_amd64.deb ...
    Unpacking libnl-genl-3-200:amd64 (3.7.0-0.2+b1) ...
    Selecting previously unselected package libpkcs11-helper1:amd64.
    Preparing to unpack .../7-libpkcs11-helper1_1.29.0-1_amd64.deb ...
    Unpacking libpkcs11-helper1:amd64 (1.29.0-1) ...
    Selecting previously unselected package openvpn.
    Preparing to unpack .../8-openvpn_2.6.3-1+deb12u2_amd64.deb ...
    Unpacking openvpn (2.6.3-1+deb12u2) ...
    Setting up libip6tc2:amd64 (1.8.9-2) ...
    Setting up liblzo2-2:amd64 (2.10-2) ...
    Setting up libpkcs11-helper1:amd64 (1.29.0-1) ...
    Setting up libnfnetlink0:amd64 (1.0.2-2) ...
    Setting up libnl-3-200:amd64 (3.7.0-0.2+b1) ...
    Setting up libnetfilter-conntrack3:amd64 (1.0.9-3) ...
    Setting up libnl-genl-3-200:amd64 (3.7.0-0.2+b1) ...
    Setting up openvpn (2.6.3-1+deb12u2) ...
    Created symlink /etc/systemd/system/multi-user.target.wants/openvpn.service → /lib/systemd/system/openvpn.service.
    Setting up iptables (1.8.9-2) ...
    update-alternatives: using /usr/sbin/iptables-legacy to provide /usr/sbin/iptables (iptables) in auto mode
    update-alternatives: using /usr/sbin/ip6tables-legacy to provide /usr/sbin/ip6tables (ip6tables) in auto mode
    update-alternatives: using /usr/sbin/iptables-nft to provide /usr/sbin/iptables (iptables) in auto mode
    update-alternatives: using /usr/sbin/ip6tables-nft to provide /usr/sbin/ip6tables (ip6tables) in auto mode
    update-alternatives: using /usr/sbin/arptables-nft to provide /usr/sbin/arptables (arptables) in auto mode
    update-alternatives: using /usr/sbin/ebtables-nft to provide /usr/sbin/ebtables (ebtables) in auto mode
    Processing triggers for man-db (2.11.2-2) ...
    Processing triggers for libc-bin (2.36-9+deb12u9) ...
    
    Notice
    ------
    'init-pki' complete; you may now create a CA or requests.
    
    Your newly created PKI dir is:
    * /etc/openvpn/server/easy-rsa/pki
    
    Using Easy-RSA configuration:
    * undefined
    .......+.+........+.+..+.........+.+.........+...........+.......+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++*.+...+..+............+.+...+.........+.....+.+..+.............+..+....+...+.....+.+..+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++*..+......+...+..+............................+........................+......+.....+.......+..+.+.........+...+........+.......+.........+.....+...+.......+...........+...+.........+...+....+...+.....+...+...+............+.......+.....+.+......+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    ...+......+.................+.........+......+.............+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++*.............+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++*....+......+....+...............+..+....+......+..+.......+...+.................+....+............+..............+.+.....+...+....+.....+...+.......+...........+............+..........+..+............+.+..+......+....+..+.........+..........+..+.......+..+....+...............+......+........+...+...........................+.+.....+.......+............+...+...+.........+........+.............+.....+.......+..+................+......+.....+......+...+.+...+........+....+..............+....+.....+...+............+.+..+...+....+......+..+....+...............+.....+.+............+.....+.......+.........+.....+.........+..........+..+....+...............+......+..............+......+.+.....+............+...+.............+..+...+.......+...+..+.......+..+...+...+.......+...+...............+..+......+.+........+.............+..+.......+.....+.........+......+....+......+........+...+.......+......+.....+....+..+..........+.....+......+....+.....+.............+..+.+...+..............+.......+........+..........+...............+......+............+.....+...+.+......+..+.............+...+..+.......+...+.....+.............+......+...+...+........+......+...............+...+.+.....+.+........................+.....+....+.....+.+.........+..+................+..+...+...+.+......+...............+..+...+.........................+...+.....+.........+.......+...+............+.........+..+....+......+..+......+.........+...+.........+.+.........+......+........+....+............+...+........+.......+...+.....+............+.+...........+....+.........+...+..+......+.+.....+....+............+.........+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    
    Notice
    ------
    CA creation complete. Your new CA certificate is at:
    * /etc/openvpn/server/easy-rsa/pki/ca.crt
    
    Create an OpenVPN TLS-AUTH|TLS-CRYPT-V1 key now: See 'help gen-tls'
    
    Build-ca completed successfully.
    
    ..+.+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++*...+......+.+..+...+.......+......+......+........+...+...+.+...+..+.........+.......+.........+...+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++*..+...............+...+.............+...........+....+............+........+............+.......+...+.....+.......+..+......+...+............+...+.+.....+...............+.+..+.............+........+.+......+...+............+.....+.........+......+....+......+.....+...+....+...+..+.......+.........+..+....+....................+.+...+.........+..+...+.+..+.........+..................+......+.+........+.......+.....+...+.+..+...+....+.....+...+..........+........+......+......+....+...+........+...+.......+..+.............+...+.....+.+........+.+.....+......+.............+......+.....+......+.........................+...+..................+..+.............+..+...............+...+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    ...+.....+.+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++*......+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++*............+..+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    -----
    
    Notice
    ------
    Private-Key and Public-Certificate-Request files created.
    Your files are:
    * req: /etc/openvpn/server/easy-rsa/pki/reqs/server.req
    * key: /etc/openvpn/server/easy-rsa/pki/private/server.key
    
    Using configuration from /etc/openvpn/server/easy-rsa/pki/698743ae/temp.6.1
    Check that the request matches the signature
    Signature ok
    The Subject's Distinguished Name is as follows
    commonName            :ASN.1 12:'server'
    Certificate is to be certified until Jan 11 16:21:18 2035 GMT (3650 days)
    
    Write out database with 1 new entries
    Database updated
    
    Notice
    ------
    Inline file created:
    * /etc/openvpn/server/easy-rsa/pki/inline/private/server.inline
    
    Notice
    ------
    Certificate created at:
    * /etc/openvpn/server/easy-rsa/pki/issued/server.crt
    
    .+.+.....+...+.......+...+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++*...+......+..+...............+..........+.....+.............+...............+..+.+..+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++*....+.........+...+........+.......+......+.........+...+.....+.......+...............+.....+.+.....+......+.+..+............+...+..........+...+..+...+...+.+...........+............+.+......+.....+...+...+..........+..+...+.......+...+........+..........+..+..........+........+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    .......+..........+.....+.+.........+.....+...+....+......+........+.+........+......+.+.....+......+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++*...........+..+...+...+....+...+........+.+......+.........+.....+...+......+......+.+........+.........+.+...............+.....+.+......+...+..+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++*.......+...+...........+..........+......+........+....+...+..+......+....+......+.........+......+......+........+.............+...+..+...+.+........+.............+..+......+......+......+...............+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    -----
    
    Notice
    ------
    Private-Key and Public-Certificate-Request files created.
    Your files are:
    * req: /etc/openvpn/server/easy-rsa/pki/reqs/vpnuk.req
    * key: /etc/openvpn/server/easy-rsa/pki/private/vpnuk.key
    
    Using configuration from /etc/openvpn/server/easy-rsa/pki/53577d67/temp.6.1
    Check that the request matches the signature
    Signature ok
    The Subject's Distinguished Name is as follows
    commonName            :ASN.1 12:'vpnuk'
    Certificate is to be certified until Jan 11 16:21:19 2035 GMT (3650 days)
    
    Write out database with 1 new entries
    Database updated
    
    Notice
    ------
    Inline file created:
    * /etc/openvpn/server/easy-rsa/pki/inline/private/vpnuk.inline
    
    Notice
    ------
    Certificate created at:
    * /etc/openvpn/server/easy-rsa/pki/issued/vpnuk.crt
    
    Using configuration from /etc/openvpn/server/easy-rsa/pki/ba92357b/temp..1
    
    Notice
    ------
    An updated CRL DER copy has been created:
    * /etc/openvpn/server/easy-rsa/pki/crl.der
    
    An updated CRL has been created:
    * /etc/openvpn/server/easy-rsa/pki/crl.pem
    
    Created symlink /etc/systemd/system/multi-user.target.wants/openvpn-iptables.service → /etc/systemd/system/openvpn-iptables.service.
    Created symlink /etc/systemd/system/multi-user.target.wants/openvpn-server@server.service → /lib/systemd/system/openvpn-server@.service.
    
    Finished!
    
    The client configuration is available in: /root/vpnuk.ovpn
    New clients can be added by running this script again.
    ```
    

Once the installation is complete, the server configuration and client profile are generated automatically. The client configuration file is saved as `/root/vpnuk.ovpn`.

![image.png](image%205.png)

### **Final Server Configuration**

Edit the OpenVPN configuration file to minimize logging:

```
nano /etc/openvpn/server/server.conf
```

Set the verbosity level to 0:

```
verb 0
```

![image.png](image%206.png)

Restart the OpenVPN service to apply changes:

```
systemctl restart openvpn-server@server.service
```

---

```jsx
 hostnamectl set-hostname mrvbot
```

![image.png](image%207.png)

### **4. Client Configuration**

### **Download the Client Configuration File**

Use SFTP to transfer the `.ovpn` file to your local machine:

```
PS C:\Users\Alex> sftp -i C:\Users\Alex\.ssh\id_rsa -P 69 vpnivan@<server_ip>
sftp> get /root/vpnuk.ovpn
Fetching /root/vpnuk.ovpn to vpnuk.ovpn
vpnuk.ovpn                                                                                      100% 4971    64.7KB/s   00:00
sftp> exit
```

### **Set Up the Client**

1. **Windows**
    - Install the OpenVPN client from [openvpn.net](https://openvpn.net/).
    - Import the `.ovpn` file and connect.
2. **macOS**
    - Use Tunnelblick, a free OpenVPN client.
    - Import the configuration file and establish the connection.
3. **Linux**
    - Install OpenVPN:
        
        ```
        sudo apt-get install openvpn
        sudo openvpn --config vpnuk.ovpn
        ```
        
4. **Mobile (Android/iOS)**
    - Download the OpenVPN Connect app.
    - Transfer and import the `.ovpn` file.

# **Conclusion**

Setting up your own OpenVPN server empowers you with privacy, security, and control over your data. Whether for personal or small-team use, this project provides a robust solution to secure online communications. Expand on this setup by exploring advanced configurations or integrating additional security measures, ensuring your VPN server remains both reliable and safe.

---

info:

https://learn.microsoft.com/en-us/windows-server/administration/openssh/openssh_keymanagement