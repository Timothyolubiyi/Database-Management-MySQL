import mysql.connector

# Connect to MySQL database
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="TITAnic@2",
    database="cloudnetwork"
)

cursor = conn.cursor()

table_name = "clouditems1"  # Replace with the table you want to drop
cursor.execute(f"DROP TABLE IF EXISTS {table_name}")

print(f"Table '{table_name}' dropped successfully (if it existed).")

cursor.close()
conn.close()
