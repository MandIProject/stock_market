import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

symbol = 'ABB.NS'

startDate = '2023-11-1'
endDate = '2024-04-1'

stockData = yf.Ticker(symbol).history(start=startDate, end=endDate)
print(stockData)

stockDataNetIncome = yf.Ticker(symbol).quarterly_financials
print(stockDataNetIncome)

stock_info = yf.Ticker(symbol).info
print("\nStock Info:")
for key, value in stock_info.items():
    print(f"{key}: {value}")

epsValue = stockDataNetIncome.iloc[22] / yf.Ticker(symbol).info['sharesOutstanding']
print(epsValue)

plt.figure(figsize=(10, 6))
plt.plot(epsValue)
plt.title("EPS Value for ABB India Ltd. (Month-wise)")
plt.ylabel('EPS Value')
plt.xlabel('Month')
plt.grid()
plt.show()

# marketCap = stockData['Close'] * yf.Ticker(symbol).info['sharesOutstanding']
# print(marketCap)

peRatio = stockData['Close'] / yf.Ticker(symbol).info['trailingEps']
print(peRatio)

plt.figure(figsize=(10, 6))
plt.plot(peRatio)
plt.title("P/E ratio for ABB India Ltd. (Month-wise)")
plt.ylabel('P/E Ratio')
plt.xlabel('Month')
plt.grid()
plt.show()

bookValue = yf.Ticker(symbol).info['bookValue']
pbRatio = stockData['Close'] / bookValue
print(pbRatio)

plt.figure(figsize=(10, 6))
plt.plot(pbRatio)
plt.title("PB ratio for ABB India Ltd. (Month-wise)")
plt.ylabel('PB Ratio')
plt.xlabel('Month')
plt.grid()
plt.show()

balance_sheet = yf.Ticker(symbol).quarterly_balance_sheet
for key, value in balance_sheet['2023-12-31'].items():
    print(f'{key}: {value}')

# psRatio = yf.Ticker(symbol).info['priceToSalesTrailing12Months']
# print(psRatio)

# dividendYield = yf.Ticker(symbol).info['trailingAnnualDividendYield']
# print(dividendYield)