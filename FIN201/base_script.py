import numpy as np
import scipy.stats as sp
import pandas as pd
pd.core.common.is_list_like = pd.api.types.is_list_like
import pandas_datareader as web

start = '2017-08-01'
end = '2018-08-31'
datasource = 'iex'

stocklist = ['AAPL', 'MCD']

prices_db = pd.DataFrame()

pct_change = pd.DataFrame()

for each_stock in stocklist:
    prices_db[each_stock] = web.DataReader(each_stock, datasource, start, end)['close']
    pct_change[each_stock] = prices_db[each_stock]/prices_db[each_stock].shift(1)-1
    average = pct_change.mean()
    std_dev = pct_change.std()
    
print("Prices as of close {}".format(prices_db))
print("Mean of daily returns is {}".format(average))
print("Standard deviation of daily returns is {}".format(std_dev))

r_list = (1 + pct_change.mean().values)**252 - 1
std_list = np.sqrt(252)*pct_change.std().values

correlation = pct_change.corr().values

print("----------------------------------------------------")
print('Annualised mean return of stocks is {}'.format(r_list))
print("Annualised volatility of daily returns is {}".format(std_list))
print("Correlation coefficient of stocks: \n{}".format(correlation))

# a user-defined function to calculate portfolio mean and standard deviation, given
# w_list : a list of weights for each stock
# r_list : a list of annualised return for each stock
# std_list : a list of annualised standard deviation for each stock
# c_matrix : a 2D list for the correlation coefficient

def portfolio_metric(w_list, r_list, std_list, c_matrix):
    risk = 0.0
    count_x = 0
    for one_a in w_list:
        count_y = 0
        for one_b in w_list:
            risk = risk + c_matrix[count_x][count_y]*one_a*one_b*std_list[count_x]*std_list[count_y]
            count_y = count_y + 1
        count_x = count_x + 1
    
    # return a two-item list - [portfolio return, portfolio standard deviation] 
    return [np.dot(w_list, r_list), np.sqrt(risk)]
    
w = [0.3, 0.7]

[m, v] = portfolio_metric(w, r_list, std_list, correlation)

print("-------------------------")
print("mean = ", m, "volatility", v)

required_rate = (1 + np.rate(12, -1000, -30000, 50000))**12-1
prob = sp.norm.cdf(required_rate, loc = m, scale = v)
print("Probability = ", 1-prob)
print(required_rate)
