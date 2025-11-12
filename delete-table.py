import mysql.connector as SQLC

# Connect to MySQL
DataBase = SQLC.connect(
  host="localhost",
  user="root",
  password="TITAnic@2",
  database = "cloudnetwork"
)
def showtables():
  
  Cursor = DataBase.cursor()
  Cursor.execute("SHOW TABLES")
  for i in Cursor:
    if len(i)>0: #length check greater than 0
      
      print(i)
    else:
      print("no tables to display")   
# Create a cursor object
Cursor = DataBase.cursor()
print("Add the table to drop")

# Execute command to create the database
table_name = "clouditems1"  # Replace with the table you want to 
Cursor.execute("DROP TABLE IF EXISTS " + "variable")   #variable is the table name

print("table cloudtems1 dropped successfully")
# printing all the tables
showtables()

# finally closing the database connection
DataBase.close()