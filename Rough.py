from tvDatafeed import TvDatafeed, Interval
import pandas as pd
import numpy as np
import datetime as dt
import matplotlib.pyplot as plt
import mplfinance as mpf
from pandas_datareader import data as pdr
import yfinance as yf
import finplot as fpt

## Trading Data
data = yf.download("BTC-USD", period="5d", interval="15m")
data = pd.DataFrame(data)
## separateing date and time if datetime is index
# data.index = pd.MultiIndex.from_arrays([data.index.date,
    # data.index.time], names=['Date','Time'])

## separateing date and time if datetime is in column not in index
data["Datetime"] = data.index
data['Date'] = data['Datetime'].dt.date
data['Time'] = data['Datetime'].dt.time
data = data.reset_index(drop=True)


## Plot the chart
# fpt.candlestick_ochl(data[["Datetime","Open", "Close", "High", "Low"]])
# fpt.add_line((data["Datetime"][200],data["High"][200]),(data["Datetime"][300],data["High"][200]), width = 3, interactive = False)
# fpt.show()
print(data)


## Get datas having higher than certain value
# b = data[data.High>22681.005859]
# print(b)

# g = data.loc[data['High'] == 22938.623047, 'Low']
# print(g)

# f = data.loc[data['Open'] == 22904.806641, 'High']
# print(f)

# e = data.query('Date == 2023-01-24')['High']
# print(e)
# data["Date"] = data.index
# a = pd.DataFrame(data, index = data["Date"])

## separateing date and time if datetime is in column not in index
# data['Dates'] = data['Date'].dt.date
# data['Time'] = data['Date'].dt.time



# print(data["Date"]["2023-01-23"])
# z = data.loc[["2023-01-23", "12:00:00" ]]
# print(z)


# print(data["High"])




## Financial Data





# tv = TvDatafeed()

# data = tv.get_hist(
#     symbol='NIFTY',exchange='NSE',interval=Interval.in_15_minute,n_bars=5000, fut_contract = 1
# )

# a = pd.DataFrame(data)
# # print(a.max())
# # print(a.max(axis = "2"))
# # print(a.groupby('datetime').high.transform('max'))
# # a['date'] = a.index
# a.index = a["datetime"]
# # data["NewColumn"] = pd.to_datetime(data["datetime"])

# print(a)



# ## Get OPEN data of each day
# # specific_time = data[data.index.time == pd.to_datetime("09:30:00").time()]
# # print(specific_time)

# # Explicitly convert to date
# # data['Date'] = pd.to_datetime(data['datetime'])

# # # Set your date column as index 
# # data.set_index('Date',inplace=True) 

# # # For monthly use 'M', If needed for other freq you can change.
# # data["high"].resample('D').sum()

