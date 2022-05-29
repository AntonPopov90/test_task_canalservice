import telebot
import psycopg2
from datetime import date
today = date.today()
past_orders = []
bot = telebot.TeleBot("5445102483:AAF8ohdfD941VIMUNG7_IOLRJzJjaepkymE")


connection = psycopg2.connect(user="postgres",
                              password="123456",
                              host="127.0.0.1",
                              port="5432",
                              database="test_db")


cursor = connection.cursor()
postgreSQL_select_Query = "SELECT * FROM canal"
cursor.execute(postgreSQL_select_Query)
canal_records = cursor.fetchall()
for row in canal_records:
    if row[3] < today:
        past_orders.append(row[1])


@bot.message_handler(commands=['start'])
def send_expired_orders(message):
    bot.send_message(message.chat.id, "Привет, высылаю номера заказов, с прошедшим сроком поставки")
    bot.send_message(message.chat.id, str(past_orders))


bot.polling()
