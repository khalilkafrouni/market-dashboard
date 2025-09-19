# Dashboard with equity (SPY), forex (USD), commodities (Gold, crude oil, wheat), bonds (Inflation-linked bonds).
# Data about growth, inflation, volatility, and yield.
# Data goes back as far as possible, with widget slider to choose time frame.

# import streamlit as st 
import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

# Getting the data for SPY (daily)
# Closing prices only
# data = yf.download("SPY")['Close']
# data.to_csv("spy_data.csv")
# print(data.index)
# print('\n\n\n\n')

spy = (pd.read_csv("spy_data.csv", index_col=0, parse_dates=True)['SPY'].pct_change() + 1).cumprod()

# # Check for missing values
# missing_values = data.isnull().sum() # number is zero, no missing values

# Plot the data
spy.plot(label='SPY')
plt.ylabel("SPY Closing Price")
plt.title("SPY Closing Price Over Time")
plt.yscale('log')

# forex using USD index
usd = (yf.download("DX-Y.NYB", start=spy.index.min())['Close'].pct_change() + 1).cumprod()
usd['DX-Y.NYB'].plot(label='USD Index')

plt.legend()
plt.show()

