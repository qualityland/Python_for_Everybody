import sqlite3

conn = sqlite3.connect('agesdb.sqlite')
cur = conn.cursor()

cur.execute('DROP TABLE IF EXISTS Ages')

cur.execute('''CREATE TABLE Ages (
  name VARCHAR(128),
  age INTEGER
  )''')

cur.execute("INSERT INTO Ages (name, age) VALUES ('Exodi', 25)")
cur.execute("INSERT INTO Ages (name, age) VALUES ('Komal', 17)")
cur.execute("INSERT INTO Ages (name, age) VALUES ('Caolan', 40)")
cur.execute("INSERT INTO Ages (name, age) VALUES ('Dimitri', 29)")


conn.commit()

# https://www.sqlite.org/lang_select.html
sqlstr = 'SELECT hex(name || age) AS X FROM Ages ORDER BY X'

for row in cur.execute(sqlstr):
    print(str(row))

cur.close()
