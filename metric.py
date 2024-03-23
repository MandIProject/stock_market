import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

symbol = 'ABB.NS'

startDate = '2023-12-1'
endDate = '2024-03-1'

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

plt.plot(epsValue)
plt.title("EPS Value for ABB India Ltd. (Month-wise)")
plt.show()

# marketCap = stockData['Close'] * yf.Ticker(symbol).info['sharesOutstanding']
# print(marketCap)

peRatio = stockData['Close'] / yf.Ticker(symbol).info['trailingEps']
print(peRatio)

plt.plot(peRatio)
plt.title("P/E ratio for ABB India Ltd. (Month-wise)")
plt.show()

bookValue = yf.Ticker(symbol).info['bookValue']
pbRatio = stockData['Close'] / bookValue
print(pbRatio)

plt.plot(pbRatio)
plt.title("PB ratio for ABB India Ltd. (Month-wise)")
plt.show()

# psRatio = yf.Ticker(symbol).info['priceToSalesTrailing12Months']
# print(psRatio)

# dividendYield = yf.Ticker(symbol).info['trailingAnnualDividendYield']
# print(dividendYield)