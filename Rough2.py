import pandas as pd
import yfinance as yf
import finplot as fplt
import numpy as np
import datetime 

## Trading Data
data = yf.download("TSLA", period = "5d", interval = "15m")
data = pd.DataFrame(data)

## separateing date and time if datetime is in column not in index
data["Datetime"] = data.index
data['Date'] = data['Datetime'].dt.date
data['Time'] = data['Datetime'].dt.time
data = data.reset_index(drop=True)


## Bollinger Band formula
def get_sma(prices, rate):
    return prices.rolling(rate).mean()

def get_bollinger_bands(prices, rate=20):
    sma = get_sma(prices, rate)
    std = prices.rolling(rate).std()
    bollinger_up = sma + std * 2 # Calculate top band
    bollinger_down = sma - std * 2 # Calculate bottom band
    return bollinger_up, bollinger_down, sma

## separateing date and time if datetime is index
# data.index = pd.MultiIndex.from_arrays([data.index.date,
#     data.index.time], names=['Date','Time'])


# print(data)


## Removing time from pandas series of date
# a = data["Datetime"].dt.date
# for i in a:
#     b = (data.loc[a]["High"].max())
#     print(i)
#     print(b)



bollinger_up, bollinger_down, sma = get_bollinger_bands(data["Close"])
data["bollinger_up"] = bollinger_up
data["bollinger_down"] = bollinger_down
data["SMA"] = sma
# data["SMA"] = sma
# print(data)


# data = data.dropna()
# ax1,ax2,ax3,ax4,ax5 = fplt.create_plot('Bitcoin/Dollar long term analysis', rows=5, maximize=False)
# fplt.set_y_scale(ax=ax1, yscale='log')
# data['ma200'] = data.Close.rolling(20).mean()
# data['ma50'] = data.Close.rolling(50).mean()
# fplt.plot(data.ma200, legend='MA20')
# fplt.plot(data.ma50, legend='MA50', ax=ax1)

## Plot the chart
# fplt.plot(data["Datetime"],data.SMA)
# fplt.plot(data["Datetime"], data["bollinger_up"])
# fplt.plot(data["Datetime"],data["bollinger_down"])
# fplt.candlestick_ochl(data[["Datetime","Open", "Close", "High", "Low"]])
# fplt.show()


# rows_with_nan = [index for index, row in data.iterrows() if row.isnull().any()]

# print(rows_with_nan)

# # Syntax of enumerate()
# enumerate(data[bollinger_up],start=0)


# data["bollinger_up", ["bollinger_down"], ["SMA"]] = data["bollinger_up", "bollinger_down"], ["SMA"].dropna()

##Swing High

# for i in data:
#     if data.loc(i, "bollinger_up") >= data.loc(i,"High"):
#             data["Swing"] = "SwingHigh"
#             print(data["Swing"])

# data["Swing"] = data.groupby(['High', 'bollinger_up']).apply(data.High >= data.bollinger_up)
data['Swing_High'] = np.where((data["High"] >= data["bollinger_up"]),
     data["High"], np.nan)
data["Swing_High"] = pd.DataFrame(data["Swing_High"])
data['Swing_Low'] = np.where((data["Low"] <= data["bollinger_down"]),
     data["Low"], np.nan)
data["Swing_Low"] = pd.DataFrame(data["Swing_Low"])

# data = data.dropna()

# data.to_csv("Rough2.csv")

## Plot the chart
fplt.plot(data["Datetime"],data["SMA"])
fplt.plot(data["Datetime"], data["bollinger_up"])
fplt.plot(data["Datetime"],data["bollinger_down"])

## Plotting Swing Highs
# for i in range(len(data)):
#     print(data.loc[i, "Datetime"], data.loc[i, "Swing_High"])
    # fplt.add_text((data.loc[i, "Datetime"], data.loc[i, "Swing_High"]), "H", color = "#bb7700")

## Swing Lows
# for i in range(len(data)):
    # print(data.loc[i, "Datetime"], data.loc[i, "Swing_Low"])
    # fplt.add_text((data.loc[i, "Datetime"], data.loc[i, "Swing_Low"]), "H", color = "#bb7700")





## FInding first Index of non-NAN Swing Low Value
First_Swing_Low = (data["Swing_Low"].first_valid_index())
# fplt.add_text((data.loc[First_Swing_Low, "Datetime"], data.loc[First_Swing_Low, "Swing_Low"]), "Low", color = "#bb7700")


## Plotting FIrst Swing High after finding  first index of Swing low
First_Swing_High = (data["Swing_High"][:First_Swing_Low  + 1].last_valid_index())
fplt.add_text((data.loc[First_Swing_High, "Datetime"], data.loc[First_Swing_High, "Swing_High"]), "H", color = "#bb7700")

## Next High touching BB
Shell_Swing_High = (data["Swing_High"][First_Swing_Low+1:].first_valid_index())
fplt.add_text((data.loc[Shell_Swing_High, "Datetime"], data.loc[Shell_Swing_High, "Swing_High"]), "H", color = "#bb7700")

## Finding Exact Swing Low
Exact_Swing_Low = data["High"][First_Swing_High:Shell_Swing_High].idxmin()
fplt.add_text((data.loc[Exact_Swing_Low, "Datetime"], data.loc[Exact_Swing_Low, "Swing_Low"]), "Low", color = "#bb7700")
print(Exact_Swing_Low)

## Plotting candlestick and showing all the Plots
fplt.candlestick_ochl(data[["Datetime","Open", "Close", "High", "Low"]])
fplt.show()
# print(data)














## Downloading financial Data
# data = yf.Ticker("AAPL")
# Balance_Sheet = yf.get_balance_sheet("AAPL")
# b = data.quarterly_balance_sheet
# dividend = data.dividends
# dividend.index = pd.MultiIndex.from_arrays([dividend.index.date,
#     dividend.index.time], names=['Date','Time'])
# dividend = pd.DataFrame(dividend)
# dividend["Datetime"] = dividend.index
# dividend["Date"] = dividend["Datetime"].dt.date
# dividend["Time"] = dividend["Datetime"].dt.time
# print(dividend)



