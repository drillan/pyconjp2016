import xlwings as xw
import os
from datetime import datetime
import pandas as pd
from pandas_datareader import data

script_dir = os.path.abspath(os.path.dirname(__file__))
data_dir = os.path.join(script_dir, 'data')
wb = xw.Book.caller()
sheet = wb.sheets['Case1-6_7']


def stock_price():
    code = sheet.range('A1').value
    try:
        # raise
        df = data.DataReader(code, 'yahoo', datetime(2006, 1, 1), datetime(2015, 12, 31))
    except:
        file_path = os.path.join(data_dir, code + '.mpack')
        df = pd.read_msgpack(file_path)
    sheet.range('A11').value = df


def clear_data():
    rng1 = sheet.range('A11').expand('table')
    rng1.clear()

