# Dashboard with equity (SPY), forex (USD), commodities (Gold ($GC=F), crude oil ($WTI, or $USO), wheat ($ZW=F))), bonds ($^TNX) Inflation-linked bonds).
# Data about growth, inflation, volatility, and yield.
# Data goes back as far as possible, with widget slider to choose time frame.

# import streamlit as st 
import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

# Getting the data for SPY (daily)
# Closing prices only
# spy = yf.download("SPY")['Close']
# spy.to_csv("spy_data.csv")
# print(spy.index)
# print('\n\n\n\n')

# Data Download
def data_download(ticker, filename):
    data = yf.download(ticker)['Close']
    data.to_csv(filename)

ticker_filename = {
    "SPY": "spy.csv",
    "DX-Y.NYB": "usd.csv",
    "GC=F": "gold.csv",
    "WTI": "wti.csv",
    "ZW=F": "wheat.csv",
    "^TNX": "bonds.csv"
}

# for ticker, filename in ticker_filename.items():
#     data_download(ticker, filename)

# Sanity Checks
# Check for missing values
def check_na(data):
    null_sum = data.isna().sum()
    null_percentage = null_sum/len(data)
    print(f"Ratio of missing values: {null_percentage}\n Count of missing values: {null_sum}")


spy = pd.read_csv('spy.csv', index_col=0, parse_dates=True)
check_na(spy)

# # Check for missing values
# missing_values = data.isnull().sum() # number is zero, no missing values

# Plot the data
# spy.plot(label='SPY')
# plt.ylabel("SPY Closing Price")
# plt.title("SPY Closing Price Over Time")
# plt.yscale('log')

# # forex using USD index
# usd['DX-Y.NYB'].plot(label='USD Index')

# plt.legend()
# plt.show()

