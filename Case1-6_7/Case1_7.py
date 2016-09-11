import xlwings as xw
import numpy as np
import pandas as pd


@xw.func
def atr(close_prev, high, low):
    d1 = high - low
    d2 = abs(high - close_prev)
    d3 = abs(close_prev - low)
    return max(d1, d2, d3)


@xw.func
@xw.arg('x', np.array)
def ptp(x):
    return np.ptp(x)


@xw.func
@xw.arg('x', pd.DataFrame, index=False, header=False)
@xw.ret(index=False, header=False)
def describe(x):
    return x.describe().values
