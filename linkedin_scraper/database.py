
import sqlite3

conn = sqlite3.connect('profiler.db')
c = conn.cursor()

c.execute("""CREATE TABLE persons (
        name text,
        profile text,
        url text,
        roles text,
        skills text
        )""")



conn.commit()

conn.close()
