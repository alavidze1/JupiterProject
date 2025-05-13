import mysql.connector
connection = mysql.connector.connect(user='weijial2',
                                  password='209132117',
                                  host='10.8.37.226',
                                  database='weijial2_db')
cursor = connection.cursor()
student = input("Enter a student's ID")
query = "CALL Get_Schedule(" + student + ")"
cursor.execute(query)
list1 = list(cursor.fetchall())
options = list1
for x in range(0, len(options)-1):
 print("Period: " + str(options[x][0]))
 print("Course: " + str(options[x][1]))
 print("Room: " + str(options[x][2]))
 print("Teacher: " + str(options[x][3]))
cursor.close()
connection.close()
