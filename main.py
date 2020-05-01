import cx_Oracle
import re
import chart_studio
import plotly.graph_objects as go
import chart_studio.plotly as py
import chart_studio.dashboard_objs as dashboard
#----------------------------------------------------------
chart_studio.tools.set_credentials_file(username='viplash4', api_key='7wRkW7UNx1GSEZfh48AE')
username = 'SYSTEM'
password = '3poli=TEX'
databaseName = 'localhost/xe'
connection = cx_Oracle.connect(username,password, databaseName)
cursor = connection.cursor()

def fileId_from_url(url):
    url_raw = url.split('/')
    cleared = [s.strip('~') for s in url_raw] # remove the ~
    nickname = cleared[3]
    id = cleared[4]
    fileId = nickname + ':' + id
    return fileId


# query 1 ------------------------------------------------------
query_1 = '''SELECT
    city_name,
    city_gdp
FROM
    city_data
WHERE
    stat_year = 2015'''
cursor.execute(query_1)
names_1 = []
values_1 = []
for data in cursor.fetchall():
    names_1.append(data[0])
    values_1.append(data[1])
print(names_1)
print(values_1)
# query 2 -----------------------------------------------------

query_2 = '''SELECT
    city_name,
    SUM(city_gdp)
FROM
    city_data
GROUP BY
    city_name'''
cursor.execute(query_2)
names_2 = []
values_2 = []
for data in cursor.fetchall():
    names_2.append(data[0])
    values_2.append(data[1])
print(names_2)
print(values_2)

# query 3------------------------------------------------------

query_3 = '''SELECT
    city_name,
    stat_year,
    city_rating
FROM
    city_data
WHERE
    city_name = 'Autauga, Alabama'
ORDER BY
    stat_year'''
cursor.execute(query_3)
names_3 = []
values_3 = []
for data in cursor.fetchall():
    names_3.append(data[2])
    values_3.append(data[1])
print(names_3)
print(values_3)
#----graph 1------------------------------------------------------------

bar = go.Bar(x=names_1,
             y=values_1
             )


graph_1 = py.plot([bar], auto_open= False, filename='task 1')
print(graph_1)
#------graph 2----------------------------------------------------------

pie = go.Pie(labels=names_2,
             values=values_2
             )
graph_2 = py.plot([pie], auto_open= False, filename='task 2')
print(graph_2)

#--------graph 3-------------------------------------------------------

scatter = go.Scatter(
    x = values_3,
    y = names_3
    )
graph_3 = py.plot([scatter], auto_open= False, filename='task 3')
print(graph_3)
#dashboard creation ---------------------------------------------------


my_dboard = dashboard.Dashboard()

graph_1_id = fileId_from_url(graph_1)
graph_2_id = fileId_from_url(graph_2)
graph_3_id = fileId_from_url(graph_3)

box_1 = {
    'type': 'box',
    'boxType': 'plot',
    'fileId': graph_1_id,
    'title': 'Внутрішній валовий продукт США за 2015 рік'
}
box_2 = {
    'type': 'box',
    'boxType': 'plot',
    'fileId': graph_2_id,
    'title': 'Внутрішній валовий продукт США за весь час'
}
box_3 = {
    'type': 'box',
    'boxType': 'plot',
    'fileId': graph_3_id,
    'title': 'Динаміка зміни рейтингу м.Отога'
}

my_dboard.insert(box_1)
my_dboard.insert(box_2, 'below', 1)
my_dboard.insert(box_3, 'left', 2)

py.dashboard_ops.upload(my_dboard, 'Workshop №3')

cursor.close()
connection.close()