import gspread
import requests

scope = ['https://www.googlapis.com/auth/spreadsheets',
         'https://www.googlapis.com/auth/drive']
GOOGLE_CREDENTIALS = gspread.service_account(filename="creds.json")
SHEET = GOOGLE_CREDENTIALS.open("test_copy").sheet1
cbrf_data = requests.get('https://www.cbr-xml-daily.ru/daily_json.js').json()
today_course = cbrf_data['Valute']['USD']['Value']


def get_values():
    values_list = SHEET.col_values(1)
    count = len(values_list)
    """Add column with price in rubles separate list into many little lists,grouped by orders"""
    for i in range(2, count):
        val = int(SHEET.cell(i, 3).value)*today_course
        SHEET.update_cell(i, 5, val)
        list_of_lists_by_orders = SHEET.get_all_values()
        return list_of_lists_by_orders


list_for_db = get_values()