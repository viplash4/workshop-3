
import cx_Oracle
import csv
import random
username = 'SYSTEM'
password = '3poli=TEX'
databaseName = 'localhost/xe'
connection = cx_Oracle.connect(username,password, databaseName)
cursor = connection.cursor()
filename = "C:/Users/vipla/PycharmProjects/workshop-3/countygdp.csv"
def gdp_normalization(gdp):
    normal_gdp = gdp.replace(',', '')
    return int(normal_gdp)
tables = ["city_info","full_city_address","states"]
for i in tables:
    cursor.execute("DELETE FROM " + i)
line_count = 0
states = []
gdps_2015 = []
gdps_2016 = []
gdps_2017 = []
gdps_2018 = []
cities = dict()
with open(filename) as file:
    reader = csv.reader(file)
    for row in reader:
        line_count += 1 #пропуск першого рядку
        if line_count == 300:
            break
        if line_count > 1:
            state = row[10]
            city = row[0]
            cities[state] = []
            if state not in states:
                states.append(state)
#---------------------------------------------------------
line_count = 0 # обнуляємо допоміжну змінну для наступного проходження по файлу
with open(filename) as file:
    reader = csv.reader(file)
    for row in reader:
        line_count += 1 #пропуск першого рядку
        if line_count == 300:
            break
        if line_count > 1:
            state = row[10]
            city = row[0]
            gdp_2015 = gdp_normalization(row[1])
            gdp_2016 = gdp_normalization(row[2])
            gdp_2017 = gdp_normalization(row[3])
            gdp_2018 = gdp_normalization(row[4])
            gdps_2015.append(gdp_2015)
            gdps_2016.append(gdp_2016)
            gdps_2017.append(gdp_2017)
            gdps_2018.append(gdp_2018)
            cities[state].append(city)
            if state not in states:
                states.append(state)
#--------------------------------------------------------------
city_states = list(cities.keys())
print(gdps_2015)
print(gdps_2016)
print(gdps_2017)
print(gdps_2018)

gdp_count = 0 # це допоміжна змінна як кастиль, тому що через фор в мене руки криві
# УВАГА УВАГА ДАЛІ SHITCODE !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
for i in range(0,len(city_states)):
    query = '''INSERT INTO States(city_state) VALUES(:city_state)'''
    cursor.execute(query,city_state = city_states[i])
    print(city_states[i])

    for j in range(0,len(cities[city_states[i]])):
        sql_helper = str(cities[city_states[i]][j])
        query = '''INSERT INTO full_city_address(city_name, city_state) VALUES (:city_name,:city_state)'''
        cursor.execute(query,city_name= sql_helper, city_state= city_states[i])
        #наступні рядки заповнюють таблицю city_info

        query = '''INSERT INTO city_info(city_name,city_state,stat_year,city_gdp,city_rating) VALUES (:city_name,:city_state,:stat_year,:city_gdp,:city_rating)'''
        cursor.execute(query, city_name=sql_helper, city_state=city_states[i], stat_year= 2015,
                           city_gdp=gdps_2015[gdp_count], city_rating=random.randint(1, 100))
        query = '''INSERT INTO city_info(city_name,city_state,stat_year,city_gdp,city_rating) VALUES (:city_name,:city_state,:stat_year,:city_gdp,:city_rating)'''
        cursor.execute(query, city_name=sql_helper, city_state=city_states[i], stat_year=2016,
                       city_gdp=gdps_2016[gdp_count], city_rating=random.randint(1, 100))
        query = '''INSERT INTO city_info(city_name,city_state,stat_year,city_gdp,city_rating) VALUES (:city_name,:city_state,:stat_year,:city_gdp,:city_rating)'''
        cursor.execute(query, city_name=sql_helper, city_state=city_states[i], stat_year=2017,
                       city_gdp=gdps_2017[gdp_count], city_rating=random.randint(1, 100))
        query = '''INSERT INTO city_info(city_name,city_state,stat_year,city_gdp,city_rating) VALUES (:city_name,:city_state,:stat_year,:city_gdp,:city_rating)'''
        cursor.execute(query, city_name=sql_helper, city_state=city_states[i], stat_year=2018,
                       city_gdp=gdps_2018[gdp_count], city_rating=random.randint(1, 100))
        gdp_count +=1 #йдемо до ввп яке відповідає наступному місту

#---------------------------------------------------------------------------------------------------------------




connection.commit()
cursor.close()
connection.close()