import yfinance as yf 

data = yf.download("AAPL" , start = "2010-01-01")
data.columns = data.columns.get_level_values(0)
data = data.dropna()
data = data.reset_index()

data.to_csv('aapl_stock.csv' , index=False)
