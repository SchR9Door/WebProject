# Report on Cybersecurity Capture The Flag (CTF) Room: Masterschool's Level One Room

Tools: Bash, GOBUSTER, John The Ripper, Linux, NMAP, hashid

*Practical Work Report by Aleksandr Kutuzov*

*Student of Cybersecurity Domain at MasterSchool*

*Date: 06/04/24*

*Mentor: Yashank Beniwal*

**Introduction:**

The following report documents the exploration and flag discovery process within the CTF room provided by Masterschool on TryHackMe. This report aims to provide a comprehensive overview of the steps taken, tools utilized, and flags discovered during the exercise.

**Initial Setup:**

**Obtaining the Target IP:** Upon starting the machine, an IP address was allocated. To facilitate ease of access and utilization, I assigned this IP to a variable.

```jsx
export IP=10.10.131.104
```

**Reconnaissance:**

**Ping and Nmap Scan:** The initial step involved verifying connectivity to the target IP through a ping test and conducting a comprehensive Nmap scan to enumerate open ports and services.

```bash
ping $IP
nmap $IP
```

![Untitled](Untitled.png)

## **Web Enumeration with Gobuster:**

Utilizing the Gobuster tool, I performed directory enumeration on the target web server to discover hidden directories and files.

```bash
gobuster dir -u $IP -w directory-list-2.3-medium.txt -x php,sh,txt,cgi,html,css,js,py
```

![Untitled](Untitled%201.png)

**Downloading Web Resources:** Using wget, I downloaded all available pages and files discovered during the enumeration process to facilitate offline inspection.

```jsx
wget -r "[http://$IP](http://$ip/)"{"","/hide.html","/secret.txt","/flag/flag","/index2.html"}
```

![Untitled](Untitled%202.png)

**Flag Discovery:**

**Inspection of index.html:** Upon navigating to the target IP directory, I inspected the index.html file using the nano text editor and discovered the flag **`{Another_Web_Flag}`** embedded within the file content.

```jsx

cd $IP
```

```jsx
ls -la
```

![Untitled](Untitled%203.png)

![Untitled](Untitled%204.png)

As I continued the inspection, I found **`{STUDENT_CTF_Web}`** within the index.html file. I used Ctrl+W to search for the `<h1>` tag.

![Untitled](Untitled%205.png)

Open the file index2.html.

```jsx
nano index2.html
```

Use Ctrl+W to find the <h1> tag.

It’s look like a standard Apache info page.

![Untitled](Untitled%206.png)

Use Ctrl+W to find a symbol.

Then, use **Alt+W:** to move forward to the next occurrence.

Find the flag: {C0nf1gur4t10n_Fl4g}

![Untitled](Untitled%207.png)

Open the file named hide.html.

```jsx
nano hide.html
```

Use Ctrl+W to find the h1 tag.

The hide.html file revealed the flag **`{H1d3_Fl4g}`** upon inspection.

![Untitled](Untitled%208.png)

```jsx
nano secret.txt
```

 The secret.txt file contained the flag **`{S3cr3t_Fl4g}`** upon examination.

![Untitled](Untitled%209.png)

```jsx
nano robots.txt
```

 The robots.txt file disclosed the flag **`{Robots_Flag}`**
 **Exploration of Flag Directory:** Within the flag directory, the files flag.txt and flag2.txt were discovered, containing the flags **`{Fl4g_fl4g_fl4g}`** and **`{Fl4g2_fl4g2_fl4g2}`** respectively.

![Untitled](Untitled%2010.png)

Open directory flag/flag/.

Here are two files: flag.txt and flag2.txt.

![Untitled](Untitled%2011.png)

```jsx
nano flag.txt
```

![Untitled](Untitled%2012.png)

```jsx
nano flag2.txt
```

**Decoding Base64:** The flag2.txt file contained a Base64-encoded string **`e0ZsNGcyX2ZsNGcyX2ZsNGcyfQ==`**

![Untitled](Untitled%2013.png)

```jsx
base64 -d 'flag2.txt'
```

 which upon decoding, revealed the flag **`{Fl4g2_fl4g2_fl4g2}`**.

![Untitled](Untitled%2014.png)

1. {STUDENT_CTF_Web} -> index.html
2. {Another_Web_Flag} -> index.html
3. {C0nf1gur4t10n_Fl4g} -> index2.html 
4. {H1d3_Fl4g} -> hide.html
5. {S3cr3t_Fl4g} -> secret.txt
6. {Robots_Flag} -> robots.txt
7. {Fl4g_fl4g_fl4g} -> flag.txt
8. {Fl4g2_fl4g2_fl4g2}  -> flag2.txt

**Conclusion for Part 1: Reconnaissance and Web Enumeration**

In concluding the exploration of reconnaissance and web enumeration, it's evident that meticulous examination and systematic enumeration are foundational to successful cybersecurity endeavors. Through the utilization of various tools and techniques, including Nmap scans, Gobuster directory enumeration, and wget for web resource retrieval, significant insights were gained into the target environment. The discovery of multiple flags underscores the importance of thorough reconnaissance in uncovering hidden information and vulnerabilities. This experience reinforces the notion that thorough preparation and reconnaissance lay the groundwork for effective cybersecurity operations.

---

## **FTP Exploration and Flag Discovery:**

**Introduction:**
In this section, we delve into the exploration of the FTP (File Transfer Protocol) service on the target machine. The objective is to identify hidden directories, retrieve hash files, crack them using John the Ripper, and ultimately discover flags concealed within.

**Preparing Dictionary Files:**

To initiate the password cracking process, I created a small dictionary file named **`ncrackdic.txt`** containing potential usernames and passwords.

![Untitled](Untitled%2015.png)

I used Ncrack to bruteforce FTP credentials using the dictionary file created.

```jsx
ncrack -U ncrackdic.txt -P ncrackdic.txt  [ftp://$IP](ftp://$ip/)
```

![Untitled](Untitled%2016.png)

To ensure comprehensive coverage, I utilized Hydra for further bruteforcing attempts, employing the same dictionary file.

```jsx
hydra -L ncrackdic.txt -P ncrackdic.txt [ftp://$IP](ftp://$ip/)
```

![Untitled](Untitled%2017.png)

**Accessing FTP Service:**

With successful credentials, I connected to the FTP service using the command

```jsx
ftp $IP
```

![Untitled](Untitled%2018.png)

**Retrieving Hash Files:**

Upon exploration, I discovered a directory named **`hash_to_crack`** containing hash files. Using wget, I downloaded all hash files from the FTP server.

```jsx
wget -r --ftp-user=ctf --ftp-password=ctf [ftp://$IP/hash_to_crack](ftp://$ip/hash_to_crack) 
```

![Untitled](Untitled%2019.png)

**Hash Analysis and Cracking:**

After downloading the hash files, I navigated to the **`hash_to_crack`** directory and identified the hash formats using the hashid tool.

```jsx
cd $IP/hash_to_crack
```

![Untitled](Untitled%2020.png)

Use Hashid to determine the format of all these hash files.

```jsx
hashid hash1.txt
```

![Untitled](Untitled%2021.png)

Following identification, I proceeded to crack the hashes using John the Ripper, utilizing a wordlist (**`wordlist.txt`**).

hash1 MD5 C0d3_0b5cur3r_Flag

```jsx
john --format=raw-md5 --wordlist=wordlist.txt hash1.txt
```

hash2 SHA-1 C0d3_5l4y3r_Flag

```jsx
john --format=raw-sha1 --wordlist=wordlist.txt hash2.txt
```

hash3 SHA-512 H4ck3r_Flag

```jsx
john --format=raw-sha512 --wordlist=wordlist.txt hash3.txt
```

hash4 SHA-256 L0ck_Flag

```jsx
john --format=raw-sha256 --wordlist=wordlist.txt hash4.txt
```

hash5 MD5 S3cur1ty_Flag

```jsx
john --format=raw-md5 --wordlist=wordlist.txt hash5.txt
```

To ensure accuracy, I used John's **`--show`** command to display all cracked passwords and confirmed the flags obtained from the hashes.

```jsx
john --show --format=raw-md5  hash1.txt &&  john --show --format=raw-sha1 hash2.txt && john --show --format=raw-sha512 hash3.txt && john --show --format=raw-sha256 hash4.txt && john --show --format=raw-md5 hash5.txt
```

![Untitled](Untitled%2022.png)

**Exploring FTP Anonymously:**

Additionally, I accessed the FTP server anonymously to retrieve further files, including **`flag.txt`** and **`files.zip`**.

![Untitled](Untitled%2023.png)

```jsx
ftp $IP
```

```jsx
get flag.txt
```

```jsx
get files.zip
```

```jsx
cat flag.txt
```

Upon downloading **`flag.txt`**, I opened the file and confirmed the presence of the flag: **`{ftp_server_4_lyfe}`**.

![Untitled](Untitled%2024.png)

**Discovery of Flags within files.zip:**

To access the contents of **`files.zip`**, I first generated a hash of the zip file using the **`zip2john`** tool and saved it to a file named **`ziphash.txt`**.

```jsx
zip2john files.zip > ziphash.txt
```

![Untitled](Untitled%2025.png)

Next, I used John the Ripper to crack the password for **`files.zip`** by providing the generated hash and a wordlist (**`Masterschool_Wordlist.txt`**).

```jsx
john ziphash.txt --wordlist=Masterschool_Wordlist.txt  
```

After successfully cracking the password, I unzipped **`files.zip`** to reveal its contents

```jsx
unzip files.zip 
```

Inside **`files.zip`**, I discovered another archive named **`secret.zip`** along with a **`wordlist.txt`** file.

**Hashing and Cracking secret.zip:**

Similarly, I generated a hash of **`secret.zip`** using **`zip2john`** and saved it to a file named **`secrethash.txt`**.

```jsx
zip2john secret.zip > secrethash.txt
```

Subsequently, I utilized John the Ripper to crack the password for **`secret.zip`** by providing the generated hash and the same wordlist used previously.

```jsx
john secrethash.txt --wordlist=wordlist.txt  
```

![Untitled](Untitled%2026.png)

Upon successful password cracking, I unzipped **`secret.zip`** to reveal its contents

```jsx
unzip secret.zip
```

Inside **`secret.zip`**, I found a file named **`john_flag.txt`**.
Upon examining the contents of **`john_flag.txt`**, I confirmed the presence of the flag: **`{LetMe1n123!@#}`**.

![Untitled](Untitled%2027.png)

**Conclusion for Part 2: FTP Analysis and Hash Cracking**

In wrapping up the analysis of FTP services and hash cracking, it's clear that persistence and adaptability are essential traits in the realm of cybersecurity. The exploration of FTP services, coupled with password cracking techniques using Ncrack, Hydra, and John the Ripper, provided valuable insights into authentication vulnerabilities and password security best practices. The successful extraction of flags from hash files highlights the importance of robust password management and encryption practices. This experience emphasizes the significance of continuously evolving techniques and strategies to navigate complex cybersecurity challenges effectively.

---

## **SSH Inspection and Flag Discovery:**

**Accessing SSH Service:**

To begin the exploration of SSH, I accessed the SSH service using the command

```jsx
ssh ctf@$IP 
```

Upon successful SSH login, I observed the flag **`{h4ck3r5_r_us}`** embedded within the SSH header.

![Untitled](Untitled%2028.png)

**Search for Flags within Directory:**

To comprehensively search for flags within the **`flag`** directory, I utilized the **`grep`** command, specifying to search within text files (**`.txt`**) recursively in the directory.

```jsx
grep --include=\*.txt -rnw '/home/ctf/flag' -e ' '
```

This search yielded the following flags:

**`{St0ry_Fl4g}`**

**`{Y0u_G0T_1t}`**

![Untitled](Untitled%2029.png)

To further explore the directory for hidden files, I navigated one directory up and listed all files using the command:

```jsx
cd .. && ls -la
```

**Discovery of Hidden Flag:**

Within the directory, I discovered a hidden file named **`.f.txt`**.

Upon inspection of the hidden file, I found the flag **`{H1d3_1n_pl41n_s1gh7}`** embedded within.

![Untitled](Untitled%2030.png)

**Conclusion for Part 3: SSH Inspection and Directory Traversal**

As we conclude the investigation into SSH inspection and directory traversal, it's evident that attention to detail and thorough examination are critical components of cybersecurity operations. The exploration of SSH services, coupled with directory traversal techniques and grep searches, yielded valuable insights into flag locations and hidden information within the target environment. The discovery of multiple flags, including those embedded within SSH headers and hidden directories, underscores the importance of comprehensive reconnaissance and examination. This experience reaffirms the importance of meticulous investigation and adaptability in navigating diverse cybersecurity scenarios effectively.

---

Reflections on the Masterschool Cybersecurity Capture The Flag (CTF) Experience

In conclusion, the exploration of Masterschool's Cybersecurity Capture The Flag (CTF) Level One Room on TryHackMe has been both challenging and rewarding. Throughout the journey, various cybersecurity skills were put to the test, ranging from web enumeration and FTP analysis to SSH inspection and directory traversal.

By delving into real-world scenarios and gamified tasks, this CTF room provided a platform for hands-on experience and practical application of theoretical knowledge. The diverse range of challenges encountered in this room emulates the complexities of cybersecurity in today's digital landscape.

Through meticulous reconnaissance, utilization of various tools and techniques, and attention to detail, multiple flags were successfully discovered. Each flag represents a milestone achieved, reflecting the progress made in honing cybersecurity skills and problem-solving acumen.

Moreover, this CTF experience serves not only as a test of technical abilities but also as a testament to perseverance, critical thinking, and dedication to continuous learning in the field of cybersecurity.

As the journey in this CTF room comes to an end, the valuable lessons learned and experiences gained will undoubtedly contribute to the development of a robust cybersecurity portfolio. It is my hope that the skills acquired here will serve as a solid foundation for future endeavors in the realm of cybersecurity.

Special thanks to the Masterschool Team for curating this immersive and educational CTF experience. Your efforts in providing a platform for cybersecurity enthusiasts to test their skills and expand their knowledge are truly commendable.

In closing, I extend my gratitude for the opportunity to embark on this exciting journey. May the lessons learned here propel me further towards becoming a seasoned cybersecurity professional.

---

## List of Flags

1. **`{Another_Web_Flag}`** - Found in **`index.html`**.
2. **`{STUDENT_CTF_Web}`** - Found in **`index.html`**.
3. **`{C0nf1gur4t10n_Fl4g}`** - Found in **`index2.html`**.
4. **`{H1d3_Fl4g}`** - Found in **`hide.html`**.
5. **`{S3cr3t_Fl4g}`** - Found in **`secret.txt`**.
6. **`{Robots_Flag}`** - Found in **`robots.txt`**.
7. **`{Fl4g_fl4g_fl4g}`** - Found in **`flag.txt`**.
8. **`{Fl4g2_fl4g2_fl4g2}`** - Found in **`flag2.txt`**.
9. **`{h4ck3r5_r_us}`** - Discovered in SSH header.
10. **`{St0ry_Fl4g}`** - Found within files in the **`flag`** directory.
11. **`{Y0u_G0T_1t}`** - Found within files in the **`flag`** directory.
12. **`{H1d3_1n_pl41n_s1gh7}`** - Found in the hidden file **`.f.txt`**.
13. **`{LetMe1n123!@#}`** -  Found in**`john_flag.txt` from secret**.zip
14. **`{ftp_server_4_lyfe}`** - Found in **`flag.txt`** from FTP.
15. **`{C0d3_0b5cur3r_Flag}`** - Found by cracking **`hash1.txt`**.
16. **`{C0d3_5l4y3r_Flag}`** - Found by cracking **`hash2.txt`**.
17. **`{H4ck3r_Flag}`** - Found by cracking **`hash3.txt`**.
18. **`{L0ck_Flag}`** - Found by cracking **`hash4.txt`**.
19. **`{S3cur1ty_Flag}`** - Found by cracking **`hash5.txt`**.
20. **`{Masterschool}`** - Password for **`files.zip`**.