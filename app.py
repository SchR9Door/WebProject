from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from config import SQLALCHEMY_DATABASE_URI
#import sqlite3
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Project(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    description = db.Column(db.Text, nullable=False)
    markdown_content = db.Column(db.Text, nullable=False)
    html_content = db.Column(db.Text, nullable=False)
    image_url = db.Column(db.String(300), nullable=True)

with app.app_context():
    db.create_all()  # Recreate missing tables
    print("Database and tables created successfully.")

@app.route('/')
def home():
    projects = Project.query.all()
    return render_template('home.html', projects=projects)

@app.route('/project/<int:project_id>')
def project_detail(project_id):
    project = Project.query.get_or_404(project_id)
    return render_template('project.html', project=project)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
