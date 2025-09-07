import pandas as pd
import numpy as np

stock_day_change = np.load("../abu/gen/stock_day_change.npy")
print(stock_day_change.shape)

print(pd.DataFrame(stock_day_change).head())
print("--------------------------------")
print(pd.DataFrame(stock_day_change)[4:6])

print("--------------------------------")
days=pd.date_range('20170101', periods=stock_day_change.shape[1], freq='1d')
stock_symbols = ["Stock " + str(x) for x in range(stock_day_change.shape[0])]
print(pd.DataFrame(stock_day_change, index=stock_symbols, columns=days).head(2))
