# JAN 2018 Question 4
# JUL 2017 Question 4
"""
Stock price of company X : USD200
Volatiity : 20%
Prevailing risk-free rate : 1%
Question : Via Black-Scholes formula, find price of a put option
and a call option with exercise price of USDB210 that matures 6 months
"""

import math
from scipy.stats import norm

def d1(s, k, sigma, t, r):
    x = (math.log(s * math.exp(r * t) / k) + 0.5 * sigma**2 * t) / (sigma * math.sqrt(t))
    return x

def d2(s, k, sigma, t, r):
    x = (math.log(s * math.exp(r * t) / k) - 0.5 * sigma**2 * t) / (sigma * math.sqrt(t))
    return x

def putprice(s, k, sigma, t, r):
    x = - s * norm.cdf(-d1(s, k, sigma, t, r)) + k * math.exp(-r * t) * norm.cdf(-d2(s, k, sigma, t, r))
    return x

def callprice(s, k, sigma, t, r):
    x = s * norm.cdf(d1(s, k, sigma, t, r)) - k * math.exp(-r*t)*norm.cdf(d2(s, k, sigma, t, r))
    return x

print(putprice(200,210,0.20,6./12,0.01))
print(callprice(200,210,0.20,6./12,0.01))

# JAN 2018 Question 5
zcy = [1.5/100, 1.8/100, 2.5/100, 3.5/100]

for i in range(len(zcy)):
    
    def f(rate, T):
        print(1/(1+rate)**T)
        
    f(zcy[i],i+1)

"""
          Spot        3mth Forw Swap    -Interest
AUDUSD   0.7430-59    17/15              1.75%
GBPUSD   1.2475-80    25/27              0.4%
"""
from decimal import Decimal

bid_AUDUSD = 0.7430
ask_AUDUSD = 0.7459
bid_GBPUSD = 1.2475
ask_GBPUSD = 1.2480
interest_AUD = 0.0175 #1.75% y
interest_GBP = 0.004   #0.4% x

bid_GBPAUD = bid_GBPUSD/ask_AUDUSD
ask_GBPAUD = ask_GBPUSD/bid_AUDUSD
Time = 90/365

f_bid = bid_GBPAUD * ((1+interest_AUD*Time)/(1+interest_GBP*Time))
f_ask = ask_GBPAUD * ((1+interest_AUD*Time)/(1+interest_GBP*Time))

print(round(bid_GBPAUD,4))
print(round(ask_GBPAUD,4))
print("------------")
print(round(f_bid,5))
print(round(f_ask,4))


