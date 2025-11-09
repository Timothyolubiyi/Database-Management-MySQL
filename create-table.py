# importing required libraries
import mysql.connector
 
dataBase = mysql.connector.connect(
  host ="localhost",
  user ="root",
  passwd ="TITAnic@2",
  database = "cloudnetwork"
)
def showtables():
  
  cursorObject = dataBase.cursor()
  cursorObject.execute("SHOW TABLES")
  for i in cursorObject:
    if len(i)>0:   #length check greater than 0
      
      print(i)
    else:
      print("no tables to display")  
# preparing a cursor object
cursorObject = dataBase.cursor()
 
# creating table 
Records = """CREATE TABLE Clouditems (
             Id INT NOT NULL AUTO_INCREMENT,
             Clouditems VARCHAR(255) NOT NULL,
             Cloudcategory VARCHAR(155) NOT NULL,
             PRIMARY KEY (Id)
                   )"""
 
# table created
cursorObject.execute(Records) 
print("shift table created successfully")
showtables()
# disconnecting from server
dataBase.close()