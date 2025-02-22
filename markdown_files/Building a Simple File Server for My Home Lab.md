# Building a Simple File Server for My Home Lab

## Introduction

I started my home lab with a practical project: creating a Samba file server using Ubuntu Server on an old PC. The machine has an Intel Core 2 Duo processor, 4GB RAM, and a 120GB SSD. This guide documents my process, from hardware setup to sharing files across multiple devices.

---

## Hardware Preparation

- **PC Setup:** The old PC was prepared with the SSD and additional HDDs connected. (Photo 1)
- **USB Boot Disk:** I downloaded Ubuntu Server 24.04.1 LTS and created a bootable USB drive using BalenaEtcher. (Photo 2)

![Photo 1](image.png)

Photo 1

![Photo 2](image%201.png)

Photo 2

## Installing Ubuntu Server

I installed Ubuntu Server from the bootable USB drive and created a system user during installation. After completing the setup, I logged into the server. (Photo 3: Ubuntu installation, Photo 4: First login and system info)

![Photo 3](77f9bcde-c4f1-42e5-932c-5ad0b8d14957.png)

Photo 3

![Photo 4](713b83ef-c24f-40b4-bef3-8c786a4b86e4.png)

Photo 4

## Remote Access Configuration

I enabled SSH to manage the server remotely. After logging in via SSH from my Windows desktop using the `cmd` terminal, I configured my router to assign a static IP to the server. (Photo 5: SSH login, Photo 6: Static IP setup)

![Photo 5](image%202.png)

Photo 5

![Photo 6](image%203.png)

Photo 6

## Installing Samba and Configuring the File Server

1. **Installing Samba:**
    
    ```
    sudo apt update
    sudo apt install samba
    ```
    
2. **Creating a Samba User Group and Adding Users:**
    
    ```
    sudo groupadd smbgroup
    sudo usermod -aG smbgroup <username>
    sudo smbpasswd -a <username>
    ```
    
3. **Configuring Samba (`/etc/samba/smb.conf`):**
    
    ```
    [MediaShare]
    path = /home/media/folder1
    browseable = yes
    writable = yes
    valid users = @smbgroup
    create mask = 0660
    directory mask = 2770
    vfs objects = recycle
    recycle:repository = .recycle
    recycle:keeptree = yes
    recycle:versions = yes
    ```
    
4. **Restarting Samba Services:**
    
    ```
    sudo systemctl restart smbd nmbd
    ```
    

---

## Preparing Storage Disks

I prepared a 1.5TB HDD with the following steps:

1. **Partitioning and Formatting:**
    
    ```
    sudo fdisk /dev/sda
    sudo mkfs.ext4 /dev/sda1
    ```
    
2. **Checking for Bad Sectors:**
    
    ```
    sudo badblocks -v /dev/sda
    ```
    

![Photo 7 `fdisk -l` output after using `badblocks -v /dev/sda`](image%204.png)

Photo 7 `fdisk -l` output after using `badblocks -v /dev/sda`

1. **Mounting the Disk and Configuring `/etc/fstab`:**
    
    ```
    sudo mkdir -p /home/media/folder1
    sudo mount /dev/sda1 /home/media/folder1
    echo '/dev/sda1 /home/media/folder1 ext4 defaults 0 2' | sudo tee -a /etc/fstab
    sudo systemctl daemon-reload
    ```
    

![Photo 8 `lsblk` output after mounting folder1](image%205.png)

Photo 8 `lsblk` output after mounting folder1

## Assigning Permissions

```
sudo chown -R root:smbgroup /home/media/folder1
sudo chmod -R 2770 /home/media/folder1
```

---

## Testing the Setup

After completing the setup, I successfully added the network share on my Windows desktop and Mac laptop using the created Samba user credentials. 

![Photo 9 `lsblk` output after mounting a new HDD partition as folder2](32beea7b-8485-4f11-b392-a8a7c0455321.png)

Photo 9 `lsblk` output after mounting a new HDD partition as folder2

![Photo 10 Final `/etc/fstab` configuration](image%206.png)

Photo 10 Final `/etc/fstab` configuration

![Photo 11 MacOS Finder showing network disks](Screenshot_2025-01-14_at_13.56.16.png)

Photo 11 MacOS Finder showing network disks

![Photo 12 Windows Explorer showing network disks](image%207.png)

Photo 12 Windows Explorer showing network disks

## Conclusion

This simple file server provides a functional and efficient way to share files across multiple devices in my home lab. It also serves as a foundation for more complex projects in the future. Now, I am able to access my file server from my desktop, MacBook, and even from a virtual machine, which is very useful.