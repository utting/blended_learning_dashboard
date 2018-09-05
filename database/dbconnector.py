import sqlite3

class Dbconnector:

	def addStudent(id, fname, lname, username, email, password): 

		conn = sqlite3.connect('pythonsqlite.db')
		c = conn.cursor()

		c.execute("INSERT INTO students VALUES (?, ?, ?, ?, ?, ?)", (id, fname, lname, username, email, password))

		conn.commit()
		conn.close()

	def removeStudent(id):
		conn = sqlite3.connect('pythonsqlite.db')
		c = conn.cursor()

		c.execute("DELETE FROM students WHERE id =="+str(id))

		conn.commit()
		conn.close()


	def getStudent(id):
		conn = sqlite3.connect('pythonsqlite.db')
		c = conn.cursor()

		c.execute("SELECT * FROM students WHERE id =="+str(id))
		return c.fetchone()

		conn.commit()
		conn.close()


	def getAll():
		conn = sqlite3.connect('pythonsqlite.db')
		c = conn.cursor()

		c.execute("SELECT * FROM students")
		print(c.fetchall())

		conn.commit()
		conn.close()

Dbconnector.getAll()
Dbconnector.addStudent(12345678, 'Bill', 'Gates', 'bgs004', 'bgs004@student.usc.edu.au', 'billspass')
Dbconnector.addStudent(87654321, 'David', 'Cunningham', 'dcn123', 'dcn123@student.usc.edu.au', '123abc')
Dbconnector.getAll()
print(Dbconnector.getStudent(12345678))
Dbconnector.removeStudent(12345678)
Dbconnector.getAll()




