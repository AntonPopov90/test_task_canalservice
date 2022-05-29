import psycopg2
from django.shortcuts import render
categories = []
values = []

connection = psycopg2.connect(user="postgres",
                              password="123456",
                              host="127.0.0.1",
                              port="5432",
                              database="test_db")


cursor = connection.cursor()
postgreSQL_select_Query = "SELECT price,delivery_time FROM canal"
cursor.execute(postgreSQL_select_Query)
canal_records = cursor.fetchall()
for row in canal_records:
    values.append(row[0])
    categories.append(row[1])
def home(request):
    context = {"values": values, 'categoriees': categories}
    return render(request, 'base.html', context=context)

