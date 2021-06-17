import csv
import sqlite3


conn = sqlite3.connect("C:\\Users\\atsuya.sugita\\testdb")
curs = conn.cursor()
#curs.execute("CREATE TABLE M_EMPLOYEE(emp_id int PRIMARY KEY, emp_name STRING)")

#curs.execute("INSERT INTO M_EMPLOYEE(emp_id, emp_name) VALUES(1, 'sugita')")
#curs.execute("INSERT INTO M_EMPLOYEE(emp_id, emp_name) VALUES(2, 'tanaka')")
#curs.execute("INSERT INTO M_EMPLOYEE(emp_id, emp_name) VALUES(3, 'takahashi')")
#curs.execute("INSERT INTO M_EMPLOYEE(emp_id, emp_name) VALUES(4, 'satou')")
#curs.execute("INSERT INTO M_EMPLOYEE(emp_id, emp_name) VALUES(5, 'suzuki')")

conn.commit()

#curs.execute("SELECT * FROM M_EMPLOYEE")
#print(curs.fetchall())

with open('./sqlite.csv','w',encoding='utf-8', newline='') as csv_file:
    curs.execute("SELECT * FROM M_EMPLOYEE")
    data = csv.writer(csv_file, lineterminator = "\n")
    data.writerow(['emp_id', 'emp_name'])
    data.writerows(curs.fetchall())


    conn.close()