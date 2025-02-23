Flask Markdown Portfolio - Project Documentation
===============================================

This is a Flask-based portfolio website that dynamically loads projects from Markdown files, 
stores them in a SQLite database, and displays them with images.


1️⃣ How to Start the Website
===========================

1. Install Python 3.x (if not already installed)
2. Open a terminal or command prompt and navigate to the project folder:
   cd flask_portfolio

3. (Optional) Create a virtual environment:
   python -m venv venv
   source venv/bin/activate  # macOS/Linux
   venv\Scripts\activate  # Windows

4. Install required modules:
   pip install -r requirements.txt

5. Run the Flask application:
   python app.py

6. Open your browser and go to:
   http://127.0.0.1:5000/


2️⃣ How to Add New Projects (Markdown Import)
==========================================

1. Create a new Markdown (.md) file inside the `markdown_files/` folder.
2. Add project content using Markdown format:
   Example:
3. Place project images inside `static/images/project_<ID>/`
4. Run the import script to add the project to the database:
python import_markdown.py
5. The project will now be visible on the website!


3️⃣ Modules Used in This Project
==========================

- **Flask** - The main web framework
- **Flask-SQLAlchemy** - Database management (SQLite)
- **Flask-Migrate** - Database migration tool
- **Markdown** - Converts Markdown files to HTML
- **SQLite3** - Lightweight database for storing projects
- **os** - Handles file operations for Markdown import
- **re** - Regular expressions to clean Markdown file paths


4️⃣ Database Management
==========================

- View all tables in the database:
python show_db.py

- Delete and reset the database:
rm database.db  # Linux/macOS
del database.db  # Windows
python app.py  # Recreate tables

- Manually add a project via Python:


5️⃣ Features & To-Do
==========================

✅ Import Markdown files as projects  
✅ Store project images in separate folders  
✅ Edit project content in the browser  
✅ Database for project storage  
🚀 Authentication for project editing (To-Do)  
🚀 Image upload via web UI (To-Do)  
🚀 Deploy on DigitalOcean/Heroku (To-Do)  





