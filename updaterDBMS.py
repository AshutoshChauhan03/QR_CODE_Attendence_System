# using datatime library to find out the time when database is updated
from datetime import datetime

# using pymysql to connect to the mysql database
import pymysql

# Providing Error handling on connection
try:
    db = pymysql.connect(
        host='localhost',
        user='root',
        passwd='ashu',
        db='attendance',
        port=3307
    )
except Exception:
    print("Connection to Database Failed !")
    exit(0)

# Connection the database is successful
print("Connected to the database !")

# Opening the file where data is
file = open('attendance.txt', 'r')
names = file.read().split('\n')

# Cursor is a container containing all the resultant from query firing
cursor = db.cursor()

for name in names:
    # Error handling if names list if empty and also termination
    if name == '':
        print("User Attendance Updated")
        file.close()
        exit(0)
    # Finding out current time
    now = datetime.now()
    # Making a query
    query = "INSERT INTO `attendance`.`attendance` (`name`, `time`) VALUES ('{}', '{}');".format(name, now)
    # Executing the query
    cursor.execute(query)
    # Committing the changes to the database
    db.commit()
