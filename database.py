import psycopg2
from psycopg2 import Error
from main_script import list_for_db
connection = psycopg2.connect(user="postgres",
                              password="123456",
                              host="127.0.0.1",
                              port="5432",
                              database="test_db")
cursor = connection.cursor()
cursor.execute("""
                      CREATE TABLE IF NOT EXISTS canal (
                      number INTEGER,
                      order_number INT NOT NULL,
                      price INTEGER,
                      delivery_time DATE,
                      price_in_rub TEXT)""")
connection.commit()


def bulk_insert(records):
    """insert values into database table"""
    try:
        connection = psycopg2.connect(user="postgres",
                                      password="123456",
                                      host="127.0.0.1",
                                      port="5432",
                                      database="test_db")
        cursor = connection.cursor()
        sql_insert_query = """ INSERT INTO canal (number, order_number, price,delivery_time,price_in_rub)
                                      VALUES (%s,%s,%s,%s,%s) """
        cursor.executemany(sql_insert_query, records)
        connection.commit()
        print(cursor.rowcount, "Запись(и) успешно вставлена(ы) в таблицу")

    except (Exception, Error) as error:
        print("Ошибка при работе с PostgreSQL", error)


bulk_insert(list_for_db[1:])
