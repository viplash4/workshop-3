import cx_Oracle
import csv
username = 'SYSTEM'
password = '3poli=TEX'
databaseName = 'localhost/xe'
connection = cx_Oracle.connect(username,password, databaseName)
cursor = connection.cursor()
tables = ["states","full_city_address","city_info"]
try:
    for i in tables: # для кожної таблиці зі списку
        with open(i + '.csv', 'w', newline='') as file:
            cursor.execute("SELECT * FROM " + i)
            row = cursor.fetchone()

            headers = []
            for k in cursor.description: #створення заголовків
                headers.append(k[0])
            print(headers)
            csv_writer = csv.writer(file, delimiter=',')
            csv_writer.writerow(headers)

            while row:
                csv_writer.writerow(row)
                row = cursor.fetchone()

except: #індикатор помилки
    print('error happened')
cursor.close()
connection.close()