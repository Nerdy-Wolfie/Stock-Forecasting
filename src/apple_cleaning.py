import yfinance as yf 
import pandas as pd 
import os

os.makedirs("data", exist_ok=True)

data = yf.download("AAPL" , start = "2010-01-01" , end = "2024-12-31")
data = data.dropna()
data = data.reset_index()

data.to_csv('data/apple_stock.csv' , index=False)
