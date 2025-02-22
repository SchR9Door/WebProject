# Upgrading My Home Lab Server

### Xeon Processorand RAM Enhancements

Introduction
To enhance the performance of my home lab file server, I decided to upgrade its processor and RAM.
The original configuration included an Intel Core 2 Duo processor and 4GB of RAM. By upgrading to
an Intel Xeon 5450 processor and increasing RAM to 8GB, I aimed to improve overall efficiency and
future-proof the system for more demanding tasks. This article documents the process step-by-step,
complete with screenshots and explanations.

### Step 1: Preparing the Motherboard

Motherboard: ECS G41T-M9
This motherboard supports basic configurations but required some adjustments to handle the Xeon
5450 processor.
Updating the BIOS
The motherboard’s BIOS needed to be updated to support the Xeon processor. Since the G41T-M9 does
not support easy flash, I had to use AFUDOS for the update. Here’s how I did it:

1. Download the Latest BIOS: I sourced the BIOS file from the manufacturer’s website.
2. Create a Bootable USB: Using Rufus, I created a bootable USB drive and copied the BIOS
update files to it.
    
    ![*(Screenshot 1: Rufus creating a bootable USB)*](Screenshot_2025-01-25_222937.png)
    
    *(Screenshot 1: Rufus creating a bootable USB)*
    
3. **Flash the BIOS**: Booted into DOS from the USB drive and ran the AFUDOS utility with the following command:
    
    ```
    afudos BIOS.rom /p /n /x /c /b
    ```
    
    - `/p` – Programs the main BIOS image
    - `/n` – Programs the NVRAM
    - `/x` – Ignores BIOS version check
    - `/c` – Clears CMOS settings after flashing
    - `/b` – Programs boot block
    
    ![*(Screenshot 2:* AFUDOS utility*)*](d30303a4-ba39-45f7-a0be-cbfc51b4f356.png)
    
    *(Screenshot 2:* AFUDOS utility*)*
    

### Troubleshooting

After flashing the BIOS, the system did not boot initially due to an "Intel C1E" issue. Disabling the Integrated Intel C1E Interface in the BIOS resolved this problem.

![*(Screenshot 3:*  Disabling C1E*)*](5c135b7f-523a-4559-b670-46dccc823fe1.png)

*(Screenshot 3:*  Disabling C1E*)*

After updating, the motherboard was ready for the new processor.

### Step 2: Modifying the Processor

The Xeon 5450 processor uses an LGA 771 socket, while my motherboard has an LGA 775 socket. To
make them compatible, I needed to:

1. Apply a 771-to-775 Adapter Sticker:
• This sticker remaps the pins to align with the LGA 775 configuration.

![ Screenshot 4: Close-up of the sticker applied to the Xeon processor](59fd68db-acf0-4d16-8446-e91e97e1236d.png)

 Screenshot 4: Close-up of the sticker applied to the Xeon processor

1. Modify the Motherboard Socket:
• Carefully removed the plastic alignment pins on the socket to accommodate the Xeon
processor.
With these changes, the Xeon processor fit perfectly into the motherboard.

    
    ![Screenshot 4.1](image.png)
    
    Screenshot 4.1
    
    ![Screenshot 4.2 Modified socket with pins removed](image%201.png)
    
    Screenshot 4.2 Modified socket with pins removed
    
    ![Screenshot 4.3](image%202.png)
    
    Screenshot 4.3
    

### Step 3: Upgrading the RAM

The server originally had 4GB of RAM installed. I added two more 2GB sticks, bringing the total to
8GB. The G41T-M9 motherboard supports up to 8GB, so this was the maximum possible upgrade.

1. Check Compatibility:
• Ensured the new RAM matched the specifications of the motherboard (DDR3).
2. Install the RAM:
• Inserted the RAM sticks into the empty DIMM slots.
Step 4: Testing the System
After assembling everything, I powered on the machine and verified the following:
3. BIOS Detection:
• Confirmed that the BIOS recognized the new processor and 8GB of RAM.
4. Operating System Boot:
• Booted into Ubuntu Server and checked the system resources.
    
    ![Screenshot 5.1: Terminal output showing CPU and RAM details](d8c56815-4c92-464e-a4a9-cdfcd025a67e.png)
    
    Screenshot 5.1: Terminal output showing CPU and RAM details
    
    ![Screenshot 5.2: Terminal output showing CPU and RAM details](808c61d9-0257-46ac-8858-647cf4cf5c26.png)
    
    Screenshot 5.2: Terminal output showing CPU and RAM details