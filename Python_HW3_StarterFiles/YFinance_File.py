"""
Date: 10.16.2024
Author: KL
Description: Calculate % change for Adj Close price of a stock.
"""
import numpy as np
import pandas as pd


def YahooData2returns(YahooData):
    # Yahoo Data = raw downloaded data from Yahoo Finance using yfinance
    # returns = % returns of 'Adj Close' as a data vector (not a data frame)
    if 'Adj Close' not in YahooData.columns:
        raise ValueError("Given dataset doesn't include 'Adj Close' column.")
    else:
        # Drop first row result, which will be NaN
        returns = YahooData['Adj Close'].pct_change().dropna()

    return returns


# Unit test data
# Set up dataframe
d = {'Open': [100, 102, 101, 103],
     'High': [105, 104, 103, 105],
     'Low': [98, 100, 99, 101],
     'Close': [101, 103, 102, 104],
     'Adj Close': [101, 103, 102, 104],
     'Volume': [1000, 1200, 900, 1100]}
index = pd.to_datetime(['2023-10-26', '2023-10-27', '2023-10-28', '2023-10-29'])
tempdata = pd.DataFrame(d, index=index)
# Set up results from function and expectation
actual_returns = YahooData2returns(tempdata)
expect_returns = np.array([0.01980198, -0.00970874, 0.01960784])
# Check if function returns are close to the expectation
assert np.allclose(actual_returns,expect_returns,atol=1e-8), \
    f"Expected {expect_returns}, but got {actual_returns}"

print("YahooData2returns unit test passed.")
