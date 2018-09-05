import sqlite3

conn = sqlite3.connect('pythonsqlite.db')

c = conn.cursor()

c.execute("""DROP TABLE IF EXISTS students""")

c.execute("""CREATE TABLE students (
 		id integer,
 		fname text,
 		lname text,
  		username text,
  		email text,
  		password text
  		)""")

#c.execute("INSERT INTO students VALUES (12345678, 'Bill', 'Gates', 'bgs004', 'bgs004@student.usc.edu.au', 'billspass')")

#c.execute("SELECT * FROM students")

#print(c.fetchall())

conn.commit()

conn.close()