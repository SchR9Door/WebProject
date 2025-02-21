import os

db_file = "database.db"

if os.path.exists(db_file):
    os.remove(db_file)
    print("Database deleted successfully.")
else:
    print("Database does not exist.")
