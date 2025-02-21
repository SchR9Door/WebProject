import os
import markdown
import re
from flask import Flask
from models import db, Project

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)


def fix_image_paths(md_content):
    """
    Converts local image paths in Markdown to Flask static paths.
    Example: ![Image](tor_logo.png) -> ![Image](/static/images/tor_logo.png)
    """
    return re.sub(r'!\[(.*?)\]\((.*?)\)', r'![\1](/static/images/\2)', md_content)


def import_project(md_file):
    if not os.path.exists(md_file):
        print(f"Error: File {md_file} not found.")
        return

    project_title = os.path.basename(md_file).replace('.md', '').replace('_', ' ').title()

    with open(md_file, 'r', encoding='utf-8') as file:
        md_content = file.read()

    # Fix image paths
    md_content = fix_image_paths(md_content)

    # Convert Markdown to HTML
    html_content = markdown.markdown(md_content)

    description = next((line for line in md_content.split('\n') if line.strip()), "No description provided.")

    with app.app_context():
        existing_project = Project.query.filter_by(title=project_title).first()
        if existing_project:
            print(f"Project '{project_title}' already exists. Skipping import.")
            return

        new_project = Project(
            title=project_title,
            description=description,
            markdown_content=md_content,
            html_content=html_content,
            image_url=None  # Can be extracted from Markdown if needed
        )

        db.session.add(new_project)
        db.session.commit()
        print(f"Imported: {project_title}")


if __name__ == '__main__':
    folder_path = "markdown_files"
    if not os.path.exists(folder_path):
        print(f"Error: Folder '{folder_path}' not found.")
    else:
        md_files = [f for f in os.listdir(folder_path) if f.endswith('.md')]
        if not md_files:
            print("No Markdown files found.")
        else:
            with app.app_context():
                for md_file in md_files:
                    import_project(os.path.join(folder_path, md_file))
