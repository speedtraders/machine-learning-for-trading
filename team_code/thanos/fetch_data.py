import yfinance as yf
import pandas as pd

# Fetch data from txt
data = pd.read_csv("data\\nasdaqlisted.txt", delimiter="|", index_col=False)
print(data)

# Get the tickers column, note column index might change
tickers = data['Symbol'].tolist()

# Remove any entries that are not valid tickers
tickers = [ticker for ticker in tickers if isinstance(ticker, str)]

# Save to a CSV file if you want
# pd.DataFrame(nyse_tickers, columns=["Ticker"]).to_csv("NYSE_Tickers.csv", index=False)

# Initialize an empty DataFrame to hold all OHLCV data
all_data = pd.DataFrame()

for ticker in tickers[:10]:
    print(f"Fetching data for {ticker}")
    data = yf.download(ticker, period='5y')
    ohlcv_data = data[['Open', 'High', 'Low', 'Close', 'Volume']]
    ohlcv_data['Ticker'] = ticker
    ohlcv_data.to_csv(f'data\\csvs\\{ticker}.csv', index=False)
    # Append the data to the all_data DataFrame
    # all_data = pd.concat([all_data, ohlcv_data.reset_index().rename(columns={'Date': 'Date_' + ticker})])

# Save to CSV file
# all_data.to_csv('NYSE_OHLCV_Last_Year.csv', index=False)
