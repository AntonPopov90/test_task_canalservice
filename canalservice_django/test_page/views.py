import json
import psycopg2
from datetime import datetime, date
from django.shortcuts import render
from .models import Numbers
number = []
orders_number = []
price = []
dates = []
sum_in_rub = []
sum_of_orders = 0
connection = psycopg2.connect(user="postgres",
                              password="123456",
                              host="127.0.0.1",
                              port="5432",
                              database="numbers_test_db")


cursor = connection.cursor()
postgreSQL_select_Query = "SELECT * FROM numbers"
cursor.execute(postgreSQL_select_Query)
canal_records = cursor.fetchall()
for row in canal_records:
    number.append(row[0])
    orders_number.append(row[1])
    price.append(int(row[2]))
    dates.append(row[3])
    sum_in_rub.append(row[4])
total_sum = sum(price)


def serialize_data(object):
    ''' Serialize dete format into JSON '''
    if isinstance(object, (datetime, date)):
        serial = object.isoformat()
        return serial
values_to_json = {'values': price}
dates_to_json = {'date': dates}
orders_price = json.dumps(values_to_json, default=serialize_data)
orders_dates = json.dumps(dates_to_json, default=serialize_data)

def home(request):
    return render(request, 'base.html', context={'orders_price':orders_price,'price': price,
                                                 'orders_dates': orders_dates, 'orders_number': orders_number,
                                                  'number': number,'dates':dates,
                                                 'total': total_sum})

