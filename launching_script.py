import schedule
import time
from main_script import work
from database import bulk_insert
from telegram import send_expired_orders
schedule.every(5).minutes.do(work)
schedule.every(7).minutes.do(bulk_insert)
schedule.every().day.at("10:00").do(send_expired_orders)

while True:
    schedule.run_pending()
    time.sleep(5)
