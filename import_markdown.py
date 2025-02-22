import os
import markdown
import re
from flask import Flask
from models import db, Project

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

def fix_image_paths(md_content, project_id):
    """
    Converts local image paths in Markdown to Flask static paths.
    Example: ![Image](image.png) -> ![Image](/static/images/project_1/image.png)
    """
    return re.sub(r'!\[(.*?)\]\((.*?)\)', rf'![\1](/static/images/project_{project_id}/\2)', md_content)

def import_project(md_file):
    if not os.path.exists(md_file):
        print(f"Error: File {md_file} not found.")
        return

    project_title = os.path.basename(md_file).replace('.md', '').replace('_', ' ').title()

    with open(md_file, 'r', encoding='utf-8') as file:
        md_content = file.read()

    with app.app_context():
        # Create new project entry
        new_project = Project(title=project_title, description="Auto-imported from Markdown",
                              markdown_content=md_content, html_content="", image_url=None)
        db.session.add(new_project)
        db.session.commit()

        # Use project ID for image folder
        project_id = new_project.id
        project_folder = f"static/images/project_{project_id}"

        # Create the project folder if it doesn't exist
        os.makedirs(project_folder, exist_ok=True)

        # Fix image paths with project-specific folder
        md_content = fix_image_paths(md_content, project_id)
        html_content = markdown.markdown(md_content)

        # Update the project entry with HTML content
        new_project.markdown_content = md_content
        new_project.html_content = html_content
        db.session.commit()

        print(f"Imported: {project_title} (Stored images in {project_folder})")

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
