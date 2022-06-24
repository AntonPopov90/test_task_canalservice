import gspread
import requests
import schedule
import time
import psycopg2


scope = ['https://www.googlapis.com/auth/spreadsheets',
         'https://www.googlapis.com/auth/drive']
GOOGLE_CREDENTIALS = gspread.service_account(filename="creds.json")
SHEET = GOOGLE_CREDENTIALS.open("Test_copy").sheet1
cbrf_data = requests.get('https://www.cbr-xml-daily.ru/daily_json.js').json()
today_course = cbrf_data['Valute']['USD']['Value']


SHEET.update_cell(1, 5, 'стоимость в руб')  # create column 'стоимость в рублях'


def add_roubles_values():
    """Add values in rubles and returns list of orders"""
    orders_count = len(SHEET.col_values(1))
    price_in_dollars = SHEET.col_values(3)
    price_in_roubles = [today_course*int(x) for x in price_in_dollars[1:]]
    for i in range(orders_count-1):
        SHEET.update_cell(i+2, 5, price_in_roubles[i])


add_roubles_values()


def create_database():
    connection = psycopg2.connect(user="postgres",
                                  password="123456",
                                  host="127.0.0.1",
                                  port="5432",
                                  database="numbers_test_db")
    cursor = connection.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS numbers (
                          id TEXT PRIMARY KEY,
                          order_number TEXT NOT NULL,
                          price TEXT,
                          delivery_time DATE,
                          price_in_rub TEXT)''')
    connection.commit()


create_database()


def bulk_insert(records):
    """Insert values to database"""
    try:
        connection = psycopg2.connect(user="postgres",
                                      password="123456",
                                      host="127.0.0.1",
                                      port="5432",
                                      database="numbers_test_db")
        cursor = connection.cursor()
        sql_insert_query = ''' INSERT INTO numbers (id, order_number, price, delivery_time, price_in_rub)
                                      VALUES (%s,%s,%s,%s,%s) '''
        cursor.executemany(sql_insert_query, records)
        connection.commit()
        print(cursor.rowcount, "Запись(и) успешно вставлена(ы) в таблицу")
    except psycopg2.DatabaseError as error:
        print('ощибка базы данных', error)


first_values = SHEET.get_all_values()
bulk_insert(first_values[1:])


def check_changes_in_table(first_list):
    """checking for changes in a google sheets"""
    second_list = SHEET.get_all_values()
    differences = [x for x in first_list + second_list if x not in first_list or x not in second_list]
    if not differences:
        print("Lists are equal")
    else:
        connection = psycopg2.connect(user="postgres",
                                      password="123456",
                                      host="127.0.0.1",
                                      port="5432",
                                      database="numbers_test_db")
        cursor = connection.cursor()
        cursor.execute("DROP TABLE IF EXISTS numbers")
        connection.commit()

        create_database()

        bulk_insert(second_list)


schedule.every(30).seconds.do(check_changes_in_table, first_values)  # check updates in google sheets every 30 seconds


while True:
    schedule.run_pending()
    time.sleep(5)
