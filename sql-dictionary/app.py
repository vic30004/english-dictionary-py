import mysql.connector

con = mysql.connector.connect(
user = "ardit700_student",
password= "ardit700_student",
host="108.167.140.122",
database="ardit700_pm1database"
)

cursor = con.cursor()

query = cursor.execute("SELECT * FROM Dictionary")
result = cursor.fetchall()

for item1,item2 in result:
    print(item1,item2)



