import sqlite3

# Connect to the database
conn = sqlite3.connect("database.db")
cursor = conn.cursor()

# Get all table names
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
tables = cursor.fetchall()

print("Tables in database:")
for table in tables:
    print(table[0])

conn.close()


def show_table_data(db_name, table_name):
    # Connect to the database
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()

    # Get column names
    cursor.execute(f"PRAGMA table_info({table_name})")
    columns = [col[1] for col in cursor.fetchall()]

    # Fetch data
    cursor.execute(f"SELECT * FROM {table_name}")
    rows = cursor.fetchall()

    # Print column headers
    print("\n" + table_name.upper())
    print("-" * 50)
    print(" | ".join(columns))
    print("-" * 50)

    # Print rows
    for row in rows:
        print(" | ".join(str(item) for item in row))

    conn.close()


# Run the function for 'projects' table
show_table_data("database.db", "project")

conn = sqlite3.connect("database.db")
cursor = conn.cursor()

cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
tables = cursor.fetchall()

print("Tables in database:", tables)

conn.close()