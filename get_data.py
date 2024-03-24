import yfinance as yf
import matplotlib.pyplot as plt
from datetime import datetime, timedelta
import mplfinance as mpf

def get_stock_performance(symbol):
    try:
        # Retrieve stock data using yfinance
        stock_data = yf.Ticker(symbol)
        return stock_data.history(period="6mo")
    except Exception as e:
        print("Error occurred:", str(e))
        return None

def calculate_market_cap(stock_data, symbol):
    # Calculate market cap (open price * volume)
    stock_data['MarketCap'] = stock_data['Close'] * yf.Ticker(symbol).info['sharesOutstanding']
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

def calculate_epsValue(symbol):
    #Calculate EPS value
    stock_metrics = yf.Ticker(symbol).quarterly_financials.iloc[22] / yf.Ticker(symbol).info['sharesOutstanding']
    return stock_metrics

def calculate_peRatio(stock_data, symbol):
    #Calculate PE Ratio
    stock_data['PE Ratio'] = stock_data['Close'] / yf.Ticker(symbol).info['trailingEps']
    return stock_data

def calculate_pbRatio(stock_data, symbol):
    #Calculate PB Ratio
    stock_data['PB Ratio'] = stock_data['Close'] / yf.Ticker(symbol).info['bookValue']
    return stock_data

def plot_candleStick(stock_data):
    mpf.plot(stock_data, type='candle', title="ABB India CandleStick Chart (daily)", style='yahoo', figscale=1.0, figratio=(0.3, 0.3))

def plot_volume(stock_data):
    plt.figure(figsize=(10, 6))
    plt.plot(stock_data['Volume'], color='blue')
    plt.title('Volume of Shares Sold for ABB India Ltd. (Month-wise)')
    plt.xlabel('Month')
    plt.ylabel('Volume')
    plt.grid(True)
    plt.show()

def plot_market_cap(stock_data):
    plt.figure(figsize=(10, 6))
    plt.plot(stock_data['MarketCap'], color='red', marker='o', linestyle='-')
    plt.title('Market Capitalization for ABB India Ltd. (Month-wise)')
    plt.xlabel('Month')
    plt.ylabel('Market Cap')
    plt.grid(True)
    plt.show()

def plot_moving_average(stock_data, window_size):
    plt.figure(figsize=(10, 6))
    plt.plot(stock_data['Close'], color='blue', label='Close Price')
    plt.plot(stock_data['MovingAverage'], color='red', label=f'Moving Average ({window_size} days)')
    plt.title(f'Stock Price and Moving Average for ABB India Ltd. (Month-wise)')
    plt.xlabel('Month')
    plt.ylabel('Price')
    plt.legend()
    plt.grid(True)
    plt.show()

def plot_percentage_change(stock_data):
    plt.figure(figsize=(10, 6))
    plt.plot(stock_data['PercentageChange'], color='green', marker='o', linestyle='-')
    plt.title('Monthly Percentage Change in Stock Prices for ABB India Ltd.')
    plt.xlabel('Month')
    plt.ylabel('Percentage Change (%)')
    plt.grid(True)
    plt.show()

def plot_volatility(stock_data, window_size):
    plt.figure(figsize=(10, 6))
    plt.plot(stock_data['Volatility'], color='purple', marker='o', linestyle='-')
    plt.title(f'Volatility of Stock Prices for ABB India Ltd. (Monthly, Rolling {window_size} days)')
    plt.xlabel('Month')
    plt.ylabel('Volatility')
    plt.grid(True)
    plt.show()

def plot_epsValue(stock_data):
    plt.figure(figsize=(10, 6))
    plt.plot(stock_data)
    plt.title("EPS Value for ABB India Ltd. (Month-wise)")
    plt.ylabel('EPS Value')
    plt.xlabel('Month')
    plt.grid()
    plt.show()

def plot_peRatio(stock_data):
    plt.figure(figsize=(10, 6))
    plt.plot(stock_data['PE Ratio'])
    plt.title("P/E ratio for ABB India Ltd. (Month-wise)")
    plt.ylabel('P/E Ratio')
    plt.xlabel('Month')
    plt.grid()
    plt.show()

def plot_pbRatio(stock_data):
    plt.figure(figsize=(10, 6))
    plt.plot(stock_data['PB Ratio'])
    plt.title("PB ratio for ABB India Ltd. (Month-wise)")
    plt.ylabel('PB Ratio')
    plt.xlabel('Month')
    plt.grid()
    plt.show()

def main():
    # Symbol for ABB India Ltd. on NSE
    symbol = "ABB.NS"
    
    # Get stock market performance data for the last 3 months
    stock_performance = get_stock_performance(symbol)
    
    if stock_performance is not None:
        print("Stock Market Performance for ABB India Ltd. (Last 6 Months):")
        print(stock_performance)

        plot_candleStick(stock_performance)

        # Calculate market cap
        stock_performance_with_market_cap = calculate_market_cap(stock_performance, symbol)
        
        # Plot volume, market cap, moving average, percentage change, volatility, EPS Value, P/E Ratio, PB Ratio
        plot_volume(stock_performance)
        plot_market_cap(stock_performance_with_market_cap)
        
        window_size = 50  # Adjust window size as needed
        stock_performance_with_ma = calculate_moving_average(stock_performance, window_size)
        plot_moving_average(stock_performance_with_ma, window_size)
        
        stock_performance_with_percentage_change = calculate_percentage_change(stock_performance)
        plot_percentage_change(stock_performance_with_percentage_change)
        
        stock_performance_with_volatility = calculate_volatility(stock_performance_with_percentage_change, window_size)
        plot_volatility(stock_performance_with_volatility, window_size)

        stock_performance_with_epsValue = calculate_epsValue(symbol)
        plot_epsValue(stock_performance_with_epsValue) 

        stock_performance_with_peRatio = calculate_peRatio(stock_performance, symbol)
        plot_peRatio(stock_performance_with_peRatio)

        stock_performance_with_pbRatio = calculate_pbRatio(stock_performance, symbol)
        plot_pbRatio(stock_performance_with_pbRatio)

        stock_incomeSheet = yf.Ticker(symbol).quarterly_income_stmt
        print(stock_incomeSheet)

        stock_info = yf.Ticker(symbol).info
        print("\nStock Info:")
        for key, value in stock_info.items():
            print(f"{key}: {value}")

        stock_balanceSheet = yf.Ticker(symbol).quarterly_balance_sheet
        print(stock_balanceSheet)
        print("\nABB Balance Sheet:")
        for key, value in stock_balanceSheet['2023-12-31'].items():
            print(f"{key}: {value}")

    else:
        print("Failed to retrieve stock market performance")

if __name__ == "__main__":
    main()
