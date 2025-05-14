import mysql.connector
connection = mysql.connector.connect(user='weijial2',
                                  password='209132117',
                                  host='10.8.37.226',
                                  database='weijial2_db')
cursor = connection.cursor()
choose = input ("Teacher or Student?")
student = input("Log in by inputting your ID:")
if choose == "Student":
    query = "CALL Get_Schedule(" + student + ")"
else:
    query = "CALL Get_Schedule_Teacher(" + student + ")"
    #CREATE PROCEDURE Get_Schedule_Teacher(student integer) SELECT period, course_name, room FROM Get_Sections WHERE teacher_id=name ORDER BY period ASC;

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
