import schedule
import time
from main_script import get_values
from database import bulk_insert
from telegram import send_expired_orders
#from canalservice_django import manage
schedule.every(5).minutes.do(get_values)
schedule.every(5).minutes.do(bulk_insert)
schedule.every(5).minutes.do(send_expired_orders)


while True:
    schedule.run_pending()
    time.sleep(5)
