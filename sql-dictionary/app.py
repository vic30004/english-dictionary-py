import mysql.connector

con = mysql.connector.connect(
user = "ardit700_student",
password= "ardit700_student",
host="108.167.140.122",
database="ardit700_pm1database"
)

cursor = con.cursor()

def getDefinition():
    ProbUser = input("Would you like to look for a word. type Y for yes and N for no ")
    while ProbUser.lower()=="y":
        wordToLookUp= str(input("What word would you like to look up?"))
        query = cursor.execute(f"SELECT * FROM Dictionary WHERE Expression ='{wordToLookUp}'")
        result = cursor.fetchall()
        if result:
            for item1,item2 in result:
                print(f"{item1}: {item2}")
        else: 
            print("Sorry we couldn't find that. Please try again")
        ProbUser = input("Would you like to look for a word. type Y for yes and N for no ")

    else:
        print("We are sorry to see you go. Thank you for using us.")
        return

getDefinition()


