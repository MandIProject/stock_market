import yfinance as yf
import pandas as pd

# Function to get quarterly financial data for a given ticker
def get_quarterly_data(ticker):
    stock = yf.Ticker(ticker)
    income_statement = stock.quarterly_financials
    balance_sheet = stock.quarterly_balance_sheet
    historical_data = stock.history(period="6mo")
    cashFlow_data = stock.cashflow
    return income_statement, balance_sheet, historical_data, cashFlow_data

# Function to get stock information
def get_stock_info(ticker):
    stock = yf.Ticker(ticker)
    return stock.info

# Main function to fetch data and save to Excel
def fetch_and_save_data(ticker, filename):
    income_statement, balance_sheet, historical_data, cashFlow_data = get_quarterly_data(ticker)
    historical_data.index = historical_data.index.tz_convert(None)

    # Create a Pandas Excel writer using Openpyxl as the engine.
    writer = pd.ExcelWriter(filename, engine='openpyxl')

    # Write each DataFrame to a specific sheet.
    income_statement.to_excel(writer, sheet_name='Income Statement')
    balance_sheet.to_excel(writer, sheet_name='Balance Sheet')
    historical_data.to_excel(writer, sheet_name='Historical Sheet')
    cashFlow_data.to_excel(writer, sheet_name='Cash Flow Sheet')

    # Close the Pandas Excel writer and output the Excel file.
    writer._save()

# Example usage:
if __name__ == "__main__":
    ticker = "ABB.NS"  # ABB India Ltd ticker symbol
    filename = "ABB_India_Data.xlsx"
    fetch_and_save_data(ticker, filename)
    print(f"Data for {ticker} has been saved to {filename}")
