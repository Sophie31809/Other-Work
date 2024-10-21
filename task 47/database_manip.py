import sqlite3

#creating the empty table
db = sqlite3.connect('task47_db')
cursor = db.cursor()
cursor.execute('''
    CREATE TABLE python_programming(id INTEGER PRIMARY KEY, name TEXT, grade INTEGER)
    ''')
db.commit()

#defining variables tp add to the table
id1 = 55
name1 = 'Carl Davis'
grade1 = 61

id2 = 66
name2 = 'Dennis Fredrickson'
grade2 = 88

id3 = 77
name3 = 'Jane Richards'
grade3 = 78

id4 = 12
name4 = 'Peyton Sawyer'
grade4 = 45

id5 = 2
name5 = 'Lucas Brooke'
grade5 = 99


#adding the data into the table
cursor.execute('''INSERT INTO python_programming(id, name, grade)
    VALUES(?,?,?)''', (id1, name1, grade1))
cursor.execute('''INSERT INTO python_programming(id, name, grade)
    VALUES(?,?,?)''', (id2, name2, grade2))
cursor.execute('''INSERT INTO python_programming(id, name, grade)
    VALUES(?,?,?)''', (id3, name3, grade3))
cursor.execute('''INSERT INTO python_programming(id, name, grade)
    VALUES(?,?,?)''', (id4, name4, grade4))
cursor.execute('''INSERT INTO python_programming(id, name, grade)
    VALUES(?,?,?)''', (id5, name5, grade5))

db.commit()

#fetching the rows in the table where the grade is between 60 and 80
cursor.execute('''SELECT id, name, grade FROM python_programming WHERE grade >=60 AND grade <=80''')
python_programming = cursor.fetchall()
print(python_programming)

#changing Carl Davis' grade to 65
cursor.execute('''UPDATE python_programming SET grade = ? WHERE id = ?''', (65, name1))
db.commit()

#deleting Dennis Fredrickson's row
cursor.execute('''DELETE FROM python_programming WHERE id = ?''', (66,))
db.commit()

#changing anyones grade that is below 55
cursor.execute('''UPDATE python_programming SET grade = ? WHERE grade < 55''', (100,))
db.commit()
