import numpy as np
import scipy.stats as sp
import pandas as pd
pd.core.common.is_list_like = pd.api.types.is_list_like
import pandas_datareader as web

start = '2017-08-01'
end = '2018-08-31'
datasource = 'iex'

stocklist = ['AAPL']

prices_db = pd.DataFrame()

pct_change = pd.DataFrame()

for each_stock in stocklist:
    prices_db[each_stock] = web.DataReader(each_stock, datasource, start, end)['close']
    pct_change[each_stock] = prices_db[each_stock]/prices_db[each_stock].shift(1)-1
    average = pct_change.mean()
    std_dev = pct_change.std()
    maxValue = pct_change.nlargest(3, pct_change)
    
print("Prices as of close {}".format(prices_db))
print("Highest Return {}".format(maxValue))
