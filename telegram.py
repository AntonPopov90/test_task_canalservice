import telebot
import psycopg2
from datetime import date
today = date.today()
past_orders = []  # list of past orders
dates = []  # list of dates with past orders
bot = telebot.TeleBot("5499237282:AAGqR_PzKAkMn7JQ5A-5BA5yq93sZyGVU74")


connection = psycopg2.connect(user="postgres",
                              password="123456",
                              host="127.0.0.1",
                              port="5432",
                              database="numbers_test_db")


cursor = connection.cursor()
postgreSQL_select_Query = "select order_number,delivery_time from numbers"  #
cursor.execute(postgreSQL_select_Query)
canal_records = cursor.fetchall()
for row in canal_records:
    if row[1] < today:  # check past dates
        past_orders.append(row[0])  # add orders to list, which will send in telegram


@bot.message_handler(commands=['start'])
def send_expired_orders(message):
    bot.send_message(message.chat.id, "Привет,высылаю номера заказов, с прошедшим сроком поставки")
    bot.send_message(message.chat.id, str(past_orders))


bot.polling()