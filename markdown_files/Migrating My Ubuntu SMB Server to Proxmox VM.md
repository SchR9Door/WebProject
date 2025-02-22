# Migrating My Ubuntu SMB Server to Proxmox VM for Efficiency and Flexibility

### **Introduction**

I recently upgraded my home server setup to improve performance and make it more versatile. My goal was to migrate my existing **Ubuntu SMB server** from bare metal to a virtual machine on **Proxmox**. This setup allows me to better manage resources, create snapshots for backups, and even use the same server for multiple tasks like **website hosting**. This document describes the step-by-step process, from creating a backup of my SMB configuration to restoring everything in a Proxmox VM and getting my network shares up and running again.

---

### **Step 1: Backing Up the Current SMB Configuration**

Before starting the migration, I created a backup script to save all important configuration files and system information from my existing server. These backups make it easy to quickly restore the server in a new environment without needing to set up everything from scratch.

Here’s the script I used:

```bash
bash
#!/bin/bash
BACKUP_DIR="/home/media/folder0/SMB"  # Directory to store backups
mkdir -p "$BACKUP_DIR"                # Create backup directory if it doesn't exist

# Backup important files
cp /etc/samba/smb.conf "$BACKUP_DIR/"     # Main Samba configuration file
lsblk > "$BACKUP_DIR/lsblkinfo.txt"        # Save disk and partition information
cp /etc/fstab "$BACKUP_DIR/"               # Backup fstab for mount point reference

echo "Backup completed! Files saved in $BACKUP_DIR."

```

### **Why This Backup is Important**

- **smb.conf** contains all the custom settings for my network shares. Restoring it saves time when setting up the new server.
- **lsblkinfo.txt** provides details about the disk structure, making it easier to map drives in the new VM.
- **fstab** helps ensure that mounted drives and directories are reconnected properly.

---

### **Step 2: Installing Proxmox VE**

To create a more flexible setup, I installed **Proxmox VE** on my server. Proxmox is a powerful virtualization platform that allows me to run multiple virtual machines on the same hardware.

**Why Proxmox?**

- **Resource management:** Allocate CPU, RAM, and storage to each VM as needed.
- **Snapshots:** Easily create backups and restore points for each VM.
- **Versatility:** Run different services (e.g., website hosting, media server) on separate VMs without affecting each other.

**LVM (Logical Volume Manager)** plays a crucial role in managing storage efficiently. I used LVM to create logical volumes for each VM, allowing me to make smaller backups and snapshots without wasting disk space.

![Screenshot 2025-01-25 170939.png](Screenshot_2025-01-25_170939.png)

---

### **Step 3: Installing Ubuntu Server on a Proxmox VM**

Once Proxmox was installed, I created a new VM for **Ubuntu Server 24.04.1 LTS**. During the installation, I enabled **LVM** to manage disk space effectively inside the VM. This setup helps with snapshots and simplifies expanding storage later if needed.

Key settings during Ubuntu installation:

- **Disk partitioning:** Use LVM for flexibility.
- **Networking:** Ensure a static IP address for easy access to the SMB server.
- **Minimal installation:** Install only necessary packages to keep the VM lightweight.

![Screenshot 2025-01-26 024003.png](Screenshot_2025-01-26_024003.png)

---

### **Step 4: Attaching the Physical HDD to the VM**

After creating the Ubuntu VM, I needed to attach my existing data HDDs to it. Proxmox provides a shell for managing disk attachments.

**Steps to attach the HDD:**

1. Identify the disk in Proxmox:

![Screenshot 2025-01-26 021543.png](Screenshot_2025-01-26_021543.png)

![Screenshot 2025-01-26 025109.png](Screenshot_2025-01-26_025109.png)

1. Attach the disk to the VM using Proxmox’s CLI:

```bash
bash
qm set <VMID> -virtio0 /dev/sdX

```

1. Mount the drive inside the VM and add it to **/etc/fstab** for automatic mounting.
    
    ![Screenshot 2025-01-26 160543.png](Screenshot_2025-01-26_160543.png)
    
    ![Screenshot 2025-01-26 165332.png](Screenshot_2025-01-26_165332.png)
    

---

### **Step 5: Restoring Configuration and Getting Network Shares Running**

With the data drives attached, I restored my **smb.conf** and other configuration files from the backup.

**Steps to restore and modify the configuration:**

1. Copy the backed-up `smb.conf` to `/etc/samba/`.
2. Check and adjust paths in `smb.conf` to match the new disk structure.
3. Restart the Samba service:
    
    ```bash
    bash
    sudo systemctl restart smbd
    
    ```
    
4. Test the network shares from another device to ensure everything works.

![Screenshot 2025-01-26 at 18.00.00.png](Screenshot_2025-01-26_at_18.00.00.png)

![Screenshot 2025-01-26 181307.png](Screenshot_2025-01-26_181307.png)

---

### **Conclusion**

By migrating my SMB server to Proxmox, I created a more efficient and flexible environment for my home lab. The server is now a virtual machine with the option to allocate part of the hardware for additional VMs, such as a **website hosting platform** or **media server**.

In summary, this process involved:

1. **Updating my server hardware** with an Intel Xeon processor and 8GB RAM.
2. **Installing Proxmox** as the main operating system.
3. **Migrating the SMB server** to a virtual machine.
4. **Restoring my original configuration** and getting my network shares running again.

My **PS00 mini-server** is now ready for new tasks, making it easier to manage and expand in the future.