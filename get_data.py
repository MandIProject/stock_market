import yfinance as yf
import matplotlib.pyplot as plt
from datetime import datetime, timedelta
import numpy as np

def get_stock_performance(symbol, start_date, end_date):
    try:
        # Retrieve stock data using yfinance
        stock_data = yf.download(symbol, start=start_date, end=end_date)
        return stock_data
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
    plt.plot(stock_data.index, stock_data['Volume'], color='blue', marker='o', linestyle='-')
    plt.title('Volume of Shares Sold for ABB India Ltd. (Day-wise)')
    plt.xlabel('Date')
    plt.ylabel('Volume')
    plt.grid(True)
    plt.show()

def plot_market_cap(stock_data):
    plt.figure(figsize=(10, 6))
    plt.plot(stock_data.index, stock_data['MarketCap'], color='red', marker='o', linestyle='-')
    plt.title('Market Capitalization for ABB India Ltd. (Day-wise)')
    plt.xlabel('Date')
    plt.ylabel('Market Cap')
    plt.grid(True)
    plt.show()

def plot_moving_average(stock_data, window_size):
    plt.figure(figsize=(10, 6))
    plt.plot(stock_data.index, stock_data['Close'], color='blue', label='Close Price')
    plt.plot(stock_data.index, stock_data['MovingAverage'], color='red', label=f'Moving Average ({window_size} days)')
    plt.title(f'Stock Price and Moving Average for ABB India Ltd. (Day-wise)')
    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.legend()
    plt.grid(True)
    plt.show()

def plot_percentage_change(stock_data):
    plt.figure(figsize=(10, 6))
    plt.plot(stock_data.index, stock_data['PercentageChange'], color='green', marker='o', linestyle='-')
    plt.title('Daily Percentage Change in Stock Prices for ABB India Ltd. (Day-wise)')
    plt.xlabel('Date')
    plt.ylabel('Percentage Change (%)')
    plt.grid(True)
    plt.show()

def plot_volatility(stock_data, window_size):
    plt.figure(figsize=(10, 6))
    plt.plot(stock_data.index, stock_data['Volatility'], color='purple', marker='o', linestyle='-')
    plt.title(f'Volatility of Stock Prices for ABB India Ltd. (Rolling {window_size} days)')
    plt.xlabel('Date')
    plt.ylabel('Volatility')
    plt.grid(True)
    plt.show()

def main():
    # Symbol for ABB India Ltd. on NSE
    symbol = "ABB.NS"
    
    # Calculate start and end dates for the last 3 months
    end_date = datetime.now().strftime("%Y-%m-%d")
    start_date = (datetime.now() - timedelta(days=90)).strftime("%Y-%m-%d")
    
    # Get stock market performance data
    stock_performance = get_stock_performance(symbol, start_date, end_date)
    
    if stock_performance is not None:
        print("Stock Market Performance for ABB India Ltd. (Last 3 Months):")
        print(stock_performance)
        
        # Calculate market cap
        stock_performance_with_market_cap = calculate_market_cap(stock_performance)
        
        # Plot volume, market cap, moving average, percentage change, and volatility in separate windows
        plot_volume(stock_performance)
        plot_market_cap(stock_performance_with_market_cap)
        
        window_size = 20  # Adjust window size as needed
        stock_performance_with_ma = calculate_moving_average(stock_performance, window_size)
        plot_moving_average(stock_performance_with_ma, window_size)
        
        stock_performance_with_percentage_change = calculate_percentage_change(stock_performance)
        plot_percentage_change(stock_performance_with_percentage_change)
        
        stock_performance_with_volatility = calculate_volatility(stock_performance_with_percentage_change, window_size)
        plot_volatility(stock_performance_with_volatility, window_size)
    else:
        print("Failed to retrieve stock market performance data.")

if __name__ == "__main__":
    main()
