import yfinance as yf
import matplotlib.pyplot as plt
from datetime import datetime, timedelta
import pandas as pd

def get_stock_performance(symbol):
    try:
        # Retrieve stock data using yfinance
        stock_data = yf.Ticker(symbol)
        print(stock_data.quarterly_income_stmt)
        print(stock_data.quarterly_balance_sheet)
        return stock_data.history(period="3mo")
    except Exception as e:
        print("Error occurred:", str(e))
        return None

def calculate_market_cap(stock_data):
    # Calculate market cap (open price * volume)
    stock_data['MarketCap'] = stock_data['Open'] * stock_data['Volume']
    return stock_data

def calculate_moving_average(stock_data, window_size):
    # Calculate moving average
    stock_data['MovingAverage'] = stock_data['Close'].rolling(window=window_size).mean()
    return stock_data

def calculate_percentage_change(stock_data):
    # Calculate daily percentage change
    stock_data['PercentageChange'] = stock_data['Close'].pct_change() * 100
    return stock_data

def calculate_volatility(stock_data, window_size):
    # Calculate volatility using standard deviation of percentage change
    stock_data['Volatility'] = stock_data['PercentageChange'].rolling(window=window_size).std()
    return stock_data

def plot_volume(stock_data):
    plt.figure(figsize=(10, 6))
    plt.bar(stock_data.index.strftime('%Y-%m'), stock_data['Volume'], color='blue')
    plt.title('Volume of Shares Sold for ABB India Ltd. (Month-wise)')
    plt.xlabel('Month')
    plt.ylabel('Volume')
    plt.xticks(rotation=45)
    plt.grid(True)
    plt.show()

def plot_market_cap(stock_data):
    plt.figure(figsize=(10, 6))
    plt.plot(stock_data.resample('MS').last().index, stock_data.resample('MS').last()['MarketCap'], color='red', marker='o', linestyle='-')
    plt.title('Market Capitalization for ABB India Ltd. (Month-wise)')
    plt.xlabel('Month')
    plt.ylabel('Market Cap')
    plt.grid(True)
    plt.show()

def plot_moving_average(stock_data, window_size):
    plt.figure(figsize=(10, 6))
    plt.plot(stock_data.resample('MS').last().index, stock_data.resample('MS').last()['Close'], color='blue', label='Close Price')
    plt.plot(stock_data.resample('MS').last().index, stock_data.resample('MS').last()['MovingAverage'], color='red', label=f'Moving Average ({window_size} days)')
    plt.title(f'Stock Price and Moving Average for ABB India Ltd. (Month-wise)')
    plt.xlabel('Month')
    plt.ylabel('Price')
    plt.legend()
    plt.grid(True)
    plt.show()

def plot_percentage_change(stock_data):
    plt.figure(figsize=(10, 6))
    plt.plot(stock_data.resample('MS').last().index, stock_data.resample('MS').last()['PercentageChange'], color='green', marker='o', linestyle='-')
    plt.title('Monthly Percentage Change in Stock Prices for ABB India Ltd.')
    plt.xlabel('Month')
    plt.ylabel('Percentage Change (%)')
    plt.grid(True)
    plt.show()

def plot_volatility(stock_data, window_size):
    plt.figure(figsize=(10, 6))
    plt.plot(stock_data.resample('MS').last().index, stock_data.resample('MS').last()['Volatility'], color='purple', marker='o', linestyle='-')
    plt.title(f'Volatility of Stock Prices for ABB India Ltd. (Monthly, Rolling {window_size} days)')
    plt.xlabel('Month')
    plt.ylabel('Volatility')
    plt.grid(True)
    plt.show()

def main():
    # Symbol for ABB India Ltd. on NSE
    symbol = "ABB.NS"
    
    # Get stock market performance data for the last 3 months
    stock_performance = get_stock_performance(symbol)
    
    if stock_performance is not None:
        print("Stock Market Performance for ABB India Ltd. (Last 3 Months):")
        print(stock_performance)

        # Calculate market cap
        stock_performance_with_market_cap = calculate_market_cap(stock_performance)
        
        # Plot volume, market cap, moving average, percentage change, and volatility month-wise
        plot_volume(stock_performance)
        plot_market_cap(stock_performance_with_market_cap)
        
        window_size = 20  # Adjust window size as needed
        stock_performance_with_ma = calculate_moving_average(stock_performance, window_size)
        plot_moving_average(stock_performance_with_ma, window_size)
        
        stock_performance_with_percentage_change = calculate_percentage_change(stock_performance)
        plot_percentage_change(stock_performance_with_percentage_change)
        
        stock_performance_with_volatility = calculate_volatility(stock_performance_with_percentage_change, window_size)
        plot_volatility(stock_performance_with_volatility, window_size)

        stock_info = yf.Ticker(symbol).info
        print("\nStock Info:")
        for key, value in stock_info.items():
            print(f"{key}: {value}")

    else:
        print("Failed to retrieve stock market performance")

if __name__ == "__main__":
    main()
