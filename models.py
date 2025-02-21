from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Project(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    description = db.Column(db.Text, nullable=False)
    markdown_content = db.Column(db.Text, nullable=False)
    html_content = db.Column(db.Text, nullable=False)
    image_url = db.Column(db.String(300), nullable=True)
