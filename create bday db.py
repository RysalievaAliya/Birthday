import sqlite3

conn = sqlite3.connect('bday.db')
c = conn.cursor()

c.execute('''
          CREATE TABLE IF NOT EXISTS bday
          ([id] INTEGER PRIMARY KEY, [name] TEXT, [date] TEXT)
          ''')


conn.commit()
