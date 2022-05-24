from datetime import datetime
import psycopg2
from django.db.models import Sum, Avg
from django.shortcuts import render
from .models import GoogleSheet
from qsstats import QuerySetStats
from datetime import date
from dateutil.relativedelta import relativedelta
today = date.today()

def time_series(queryset, date_field, interval, func=None):
    qsstats = QuerySetStats(queryset, date_field, func)
    return qsstats.time_series(*interval)

def home(request):
    series = {'count': [], 'total': []}
    series['count'].append(date)
    series['total'].append(price)



    print(series['total'])
    return render(request, 'base.html', {'series': series})
