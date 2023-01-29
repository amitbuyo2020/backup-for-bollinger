
from tvDatafeed import TvDatafeed, Interval
import pandas as pd
import numpy as np
import datetime
import matplotlib.pyplot as plt
import mplfinance as mpf


tv = TvDatafeed()

ohlc_data = tv.get_hist(
    symbol='NIFTY',exchange='NSE',interval=Interval.in_15_minute,n_bars=5000, fut_contract = 1
)


## To get the Data from Market opening time
ohlc_data = ohlc_data[
    (ohlc_data.index.date>ohlc_data.index.date[0])
    & (ohlc_data.index.time >= datetime.time(9,15))
    & (ohlc_data.index.time <= datetime.time(15, 30))
]


##INTIAAL BALANCE
initial_balance = (
    ohlc_data[ohlc_data.index.time < datetime.time(9,45)]
    .resample("D") 
    .apply({"high" : "max", "low" : "min", "volume" : "sum"})
    .dropna()
)

##WIDTH OF INITIAL BALANCE
initial_balance["width"] = initial_balance["high"] - initial_balance["low"]




ohlc_data["ib_h"] = ohlc_data.index.map(
    lambda x: initial_balance.loc[pd.to_datetime(x.date())]["high"] 
    if x.time() >= datetime.time(9,45) 
    else np.nan
)

ohlc_data["ib_l"] = ohlc_data.index.map(
    lambda x: initial_balance.loc[pd.to_datetime(x.date())]["low"] 
    if x.time() >= datetime.time(9,45) 
    else np.nan
)



## Plotting the datas in chart
ib_plots = [
    mpf.make_addplot(ohlc_data[["ib_h", "ib_l"]]),
]

mpf.plot(ohlc_data, type="candle", style="yahoo", addplot=ib_plots)
