import pandas as pd
# import bokeh.io
import yfinance as yf
import datetime
# from bokeh.plotting import figure, show

# bokeh.io.output_notebook()
nvda = yf.Ticker("NVDA")

nvda.info

data = yf.download("NVDA", period="1mo")
print(data.head())