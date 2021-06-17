import csv
import sqlite3


conn = sqlite3.connect("C:\\Users\\atsuya.sugita\\testdb")
curs = conn.cursor()

with open('./WK_M_EMPLOYEE.csv','r', newline='', encoding='utf-8-sig') as csv_file:

    read = csv.DictReader(csv_file)
    d = []
    for row in read:
        print(row["EMPLOYEE_NO"], row["EMP_NAME"], row["DEPARTMENT_KBN"], row["MAIL_ADDRESS"])
        d.append({'EMPLOYEE_NO':row['EMPLOYEE_NO'],'EMP_NAME':row['EMP_NAME'] ,'DEPARTMENT_KBN':row['DEPARTMENT_KBN'], 'MAIL_ADDRESS':row['MAIL_ADDRESS']})
    for v in d:
        print(v)
        data = [list(v.values())]
        curs.executemany("INSERT INTO M_EMP(id, name, belong, mail) VALUES(?,?,?,?)", data)
conn.commit()

curs.execute("SELECT * FROM M_EMP")
print(curs.fetchall())
conn.close()