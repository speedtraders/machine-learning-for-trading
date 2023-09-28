import pandas as pd
import yfinance as yf
import pandas as pd

# Fetch the table from Wikipedia
url = "https://en.wikipedia.org/wiki/Companies_listed_on_the_New_York_Stock_Exchange_(A)"
tables = pd.read_html(url)

# Get the correct table
nyse_table = tables[0]  

# Get the tickers column, note column index might change
nyse_tickers = nyse_table['Symbol'].tolist()

# Remove any entries that are not valid tickers
nyse_tickers = [ticker for ticker in nyse_tickers if isinstance(ticker, str)]

# Save to a CSV file if you want
pd.DataFrame(nyse_tickers, columns=["Ticker"]).to_csv("NYSE_Tickers.csv", index=False)

# Initialize an empty DataFrame to hold all OHLCV data
all_data = pd.DataFrame()

for ticker in nyse_tickers:
    print(f"Fetching data for {ticker}")
    data = yf.download(ticker, period='1y')
    ohlcv_data = data[['Open', 'High', 'Low', 'Close', 'Volume']]
    ohlcv_data['Ticker'] = ticker
    
    # Append the data to the all_data DataFrame
    all_data = pd.concat([all_data, ohlcv_data.reset_index().rename(columns={'Date': 'Date_' + ticker})])

# Save to CSV file
all_data.to_csv('NYSE_OHLCV_Last_Year.csv', index=False)
