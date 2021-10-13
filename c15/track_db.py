import sqlite3

conn = sqlite3.connect('tracks.sqlite')
cur = conn.cursor()

#cur.execute('DROP TABLE IF EXISTS Ages')

cur.execute('''
CREATE TABLE Artist (
  id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
  name TEXT
 )''')

cur.execute('''
CREATE TABLE Genre (
  id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
  name TEXT
 )''')

cur.execute('''
CREATE TABLE Album (
  id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
  artist_id INTEGER,
  title TEXT
 )''')

cur.execute('''
CREATE TABLE Track (
  id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
  album_id INTEGER,
  genre_id INTEGER,
  title TEXT,
  rating INTEGER,
  len INTEGER,
  count INTEGER
 )''')

cur.execute("INSERT INTO Artist (name) VALUES ('Led Zeppelin')")
cur.execute("INSERT INTO Artist (name) VALUES ('AC/DC')")

cur.execute("INSERT INTO Genre (name) VALUES ('Rock')")
cur.execute("INSERT INTO Genre (name) VALUES ('Metal')")

cur.execute("INSERT INTO Album (title, artist_id) VALUES ('Who Made Who', 2)")
cur.execute("INSERT INTO Album (title, artist_id) VALUES ('IV', 1)")

cur.execute("INSERT INTO Track (title, rating, len, count, album_id, genre_id) VALUES ('Black Dog', 5, 297, 0, 2, 1)")
cur.execute("INSERT INTO Track (title, rating, len, count, album_id, genre_id) VALUES ('Stairway', 5, 482, 0, 2, 1)")
cur.execute("INSERT INTO Track (title, rating, len, count, album_id, genre_id) VALUES ('About to Rock', 5, 313, 0, 1, 2)")
cur.execute("INSERT INTO Track (title, rating, len, count, album_id, genre_id) VALUES ('Who Made Who', 5, 207, 0, 1, 2)")


conn.commit()

# https://www.sqlite.org/lang_select.html
sqlstr = '''
SELECT Track.title, Artist.name, Album.title, Genre.name
FROM Track JOIN Genre JOIN Album JOIN Artist
ON Track.genre_id = Genre.id
AND Track.album_id = Album.id
AND Album.artist_id = Artist.id
'''
#
# for row in cur.execute(sqlstr):
#     print(str(row))

cur.close()
