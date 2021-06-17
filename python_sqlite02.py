import sqlite3


conn = sqlite3.connect("C:\\Users\\atsuya.sugita\\testdb")
curs = conn.cursor()
conn.commit()

curs.execute("SELECT * FROM M_EMP")
print(curs.fetchall())
conn.close()