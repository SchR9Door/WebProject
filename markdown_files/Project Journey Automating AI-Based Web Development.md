# Project Journey: Automating AI-Based Web Development with Bash Scripts

### **Introduction: The Idea**

In this project, I set out to create a fully automated system for generating websites using AI models. With limited hardware resources (an AMD FX 8-core processor), I wanted to explore how AI could be leveraged to generate real-time HTML content. The idea was to design a workflow where models, like `deepseek-r1:14b` and `deepseek-r1:1.5b`, would be used in a web studio-like environment to create and modify websites based on predefined inputs and changing model files.

### **The Setup**

I set up a virtual machine on my Proxmox server running Ubuntu Server and installed the necessary tools to get the automation process up and running. The core of the setup was creating a Bash script (`studio.sh`) that simulates a web studio. It interacts with various data sources and model files to create prompts that guide the AI models.

### **Key Components:**

1. **Proxmox VM** - The virtual machine is the foundation where all processing takes place.
2. **Ollama** - An AI tool that allows me to run different models for generating content.
3. **Studio Script (`studio.sh`)** - This script takes care of the automation process by managing the inputs, generating the prompts, and running the models.
4. **Model Files** - These files define the AI's instructions for generating different outputs, allowing me to test how different models (like `1.5b` and `14b`) perform in real-world tasks

![image.png](image.png)

### **Script Breakdown:**

Here is a quick look at the script itself:

```bash
bash
#!/bin/bash
starttime=$(date "+%H:%M:%S")
HTMLCOUNTER=`cat pages.txt`
VERSION="deepseek-r1:14b"
INPUT0=`cat var0.txt`
INPUT1=`cat var1.txt`
MODELFILE=`cat Modelfile`
OUTPUTMAIN=output.txt

# Generate prompt
echo "$MODELFILE < INPUT0> $INPUT0 </INPUT0 >  <INPUT1>  $INPUT1 </INPUT1>> " > prompt.txt
PROMPT=`cat prompt.txt`

# Start AI model processing
echo "$starttime Webmaster $VERSION → Started"
ollama run $VERSION "$PROMPT" > output.txt
echo "$endtime Webmaster $VERSION Finished ✅"

# Extract HTML content
echo "Extracting HTML content..."
awk 'BEGIN { RS="```"; ORS=""; } /<!DOCTYPE html>/ { sub(/^html[[:space:]]*/, ""); print $0 > "webpage.html"; page++; }' output.txt
echo "Extracted HTML page saved in webpage.html"
cp webpage.html "webpage$HTMLCOUNTER".html
echo "COPY HTML saved in webpage$HTMLCOUNTER.html"

# Clean output
echo " " > output.txt

```

### **How It Works:**

The `studio.sh` script follows a straightforward cycle:

1. **Inputs**: The script pulls values from various text files like `var0.txt` and `var1.txt`. These represent different parameters or themes for the websites.
2. **Model Execution**: Using `ollama run`, the script runs the AI model based on the selected version (e.g., `deepseek-r1:14b`). The prompt for the model is created dynamically by combining the inputs and model file.
3. **HTML Extraction**: After the AI model generates the output, the script parses the content to extract HTML and save it to files.
4. **File Management**: The script also manages an HTML counter to keep track of the generated pages and saves them in an organized manner.
5. **Cleaning**: After each cycle, the script cleans up the output files in preparation for the next generation of content.

![Screenshot 2025-02-04 163216.png](f0a9f12f-c942-4508-83ea-acf28fb94c10.png)

### **Testing the Models:**

To evaluate the differences between the models (`1.5b` and `14b`), I conducted tests to observe how the AI performed in terms of productivity and output quality. The major challenge during testing was the limited hardware. All calculations were done on an AMD FX 8-core processor, which was far from ideal for such intensive tasks. However, despite this limitation, I was able to gather insights into how the different models handled real-time website generation.

### **Standard Output Example:**

Here's a sample output of what the script produces during a typical run:

```

========== Studio Cycle 46 ==========
🟢 Injecting Creativity
📊 Adding Parameters:
   ── VAR0: 2040 - Real-Time Sentient Web AI
   ── VAR1: CSS-Only Maze Escape Game – Move through a text maze
🖥️ REXECUTING [webmaster]... (Crafting the HTML masterpiece)
17:22:48 Webmaster deepseek-r1:14b  → Started
Webmaster deepseek-r1:14b Finished ✅
Extracting HTML content...
Extracted HTML page saved in webpage.html
COPY HTML saved in webpage54.html
[ Duration: 53m 57s ]
📄 Pages Generated So Far: 55
📂 Last Output File: 46.html
🌀 Current Cycle: 46/50
🟣 [55 Websites Deployed!]
🟡 [⚡ STANDBY MODE: Next cycle in 0 minutes]
🧹 Running mop.sh... (Cleaning up for the next masterpiece)
Cycle 46 completed! On to the next one...

```

### **Enhancing Automation: Lessons Learned and Optimizing Workflow**

### **The Importance of Prompts and Output Correction**

While working with AI models, especially the more basic ones, I realized that the prompt plays a crucial role in guiding the AI to produce the desired output. Early on, I noticed that a well-structured, clear prompt could drastically improve the AI's performance.

After experimenting, I concluded that using **XML** format for describing tasks in the prompt was particularly effective. It allowed me to structure the input more clearly, making it easier for the AI to understand the task and execute it with higher precision. This structure not only simplified task definitions but also made it easier to manage complex instructions for the AI.

```bash
Task:
Generate a **fully functional** 3-page website using **ONLY HTML, CSS, and JavaScript**.
The goal is to create an **incredibly effective** and **attention-grabbing** design with at least **one unique animation effect** that enhances user engagement.

 **Randomized Inputs:**
- **Client Role:** {input0} (Who is the client? Define their personality or business type.)
- **Site Functionality:** {input1} (What must be on the front side? E.g., Portfolio, Blog, Shop, Dashboard, etc.)
- **Time Vibe:** {input2} (What was trending in web design at that time? E.g., Dark Mode, Web 2.0, Neumorphism, etc.)

```

```bash
<purpose>
Generate a **historically accurate** single-page website using **only HTML, CSS, and JavaScript**.  
The goal is to **replicate** web designs from different time periods while **enhancing first impressions** with **immediate visual appeal**.
</purpose>

<instructions>
  <instruction>
    The website must reflect the **era's web technology** ({input0}) and include interactive **thematic content** ({input1}).
  </instruction>
  <instruction>
    The output must be a **fully functional single HTML file** with **embedded CSS and JavaScript**.
  </instruction>
  <instruction>
    **No external frameworks** (No Bootstrap, No Tailwind, No jQuery). Everything should be coded directly in HTML, CSS, and JavaScript.
  </instruction>
  <instruction>
    **Page must not be empty**—each section must contain meaningful content based on the era and thematic function.
  </instruction>
</instructions>

```

However, when working with basic AI models, I noticed that the output wasn’t always perfect. There were often bugs or inconsistencies that needed to be addressed. To solve this, I implemented a **loop** within my Bash script. After each task was completed, the script would automatically use the AI’s output as a prompt again, but with additional instructions to check for bugs and improve the generated code.

This approach turned out to be quite effective. It created a feedback loop that allowed the AI to self-correct over multiple iterations, ultimately leading to more accurate and polished outputs.

### **Considering More Efficient Languages: Python, JS, or Curl**

While the project started with a strong focus on clean **Bash** scripting, I eventually realized that using more powerful languages like **Python** or **JavaScript**, or leveraging **curl** for making requests, would significantly increase efficiency and flexibility.

- **Python**: Known for its powerful libraries and ease of use in automation tasks, Python would have been an excellent choice for handling HTTP requests, managing files, and interacting with the AI models.
- **JavaScript**: For web-related tasks, JS could streamline generating and modifying HTML content, providing interactive elements or client-side enhancements.
- **Curl**: A simple tool like **curl** could replace Bash’s complex request mechanisms for making API calls to the AI model, reducing verbosity and increasing flexibility.

Despite recognizing the potential benefits of these tools, I stuck with **Bash** for the initial release of the project. I wanted the system to be as lightweight and straightforward as possible, without the need to bring in extra dependencies or complexity.

### **Using SSH and SFTP for Remote Management**

One of the key aspects of managing this project remotely was using **SSH** to connect to my **Proxmox VM**. SSH allowed me to initiate scripts, monitor progress, and make changes directly on the virtual machine without needing to be physically present. It was crucial for running my automated cycles of AI prompts, model execution, and HTML generation.

For file transfers, I relied on **SFTP** to download old versions of scripts and HTML pages. It enabled me to keep a backup of each cycle's output and also facilitated the updating of scripts and data files. With SFTP, I could easily manage different versions of the project, ensuring that I didn’t lose any important work while iterating on the system.

![image.png](image%201.png)

### Webpages examples

![image.png](image%202.png)

[webpage14.html](webpage14.html)

![image.png](image%203.png)

[webpage19.html](webpage19.html)

![image.png](image%204.png)

[webpage21.html](webpage21.html)

![image.png](image%205.png)

[webpage3.html](webpage3.html)

![image.png](image%206.png)

[webpage11.html](webpage11.html)

![image.png](image%207.png)

[webpage15.html](webpage15.html)

### **Conclusion: Continuous Improvement and Future Plans**

Looking back at the entire process, I’m proud of how much I’ve learned about automating AI-based tasks using Bash. While I can see the benefits of integrating Python, JS, or curl into the project for greater efficiency, I’m happy that I maintained a clean Bash-based system for its simplicity.

The next steps will focus on refining the prompts and optimizing the feedback loop. I’ll also explore hardware upgrades to speed up model execution and further enhance the project’s overall performance.

By continuing to iterate on the AI's output and refining the way tasks are described, I believe this system could become a powerful tool for real-time web generation, helping to automate and streamline the development of creative digital content.