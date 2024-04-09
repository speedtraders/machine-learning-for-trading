# W6KJD1T3NB2V19OL
import pandas as pd
import requests
import csv

API_KEY = "W6KJD1T3NB2V19OL"
symbols = "GOOG"  # Add more symbols as needed
horizon = "3month"

data = []

# for symbol in symbols:
#     url = f"http://www.alphavantage.co/query?function=EARNINGS_CALENDAR&symbol={symbol}&horizon={horizon}&apikey={API_KEY}"
#     with requests.Session() as s:
#         download = s.get(url, verify=False)
#         decoded_content = download.content.decode('utf-8')
#         cr = csv.reader(decoded_content.splitlines(), delimiter=',')
#         my_list = list(cr)
#         for row in my_list:
#             data.append([symbol] + row)
#
# # Create a DataFrame from the data list
# columns = ['Symbol'] + data[0][1:]  # Use the header from the first row
# df = pd.DataFrame(data[1:], columns=columns)
#
# # Remove rows containing the value 'name'
# df = df[~df.apply(lambda row: 'name' in row.values, axis=1)]
#
# # Drop the duplicate column 'symbol'
# df = df.loc[:, ~df.columns.duplicated()]
#
# # Remove rows with None values in the 'reportDate' column
# df = df.dropna(subset=['reportDate'])
#
# # Save the DataFrame to a CSV file
# output_file_path = "/content/drive/Othercomputers/hp/FILES/Alpha_vantage/calendar_data.csv"
# df.to_csv(output_file_path, index=False)

from finance_calendars import finance_calendars as fc
from datetime import datetime, date
import pandas as pd

earnings = fc.get_earnings_today()
with pd.option_context('display.max_rows', None, 'display.max_columns', None):  # more options can be specified also
    # print(df)
    df = earnings
    # print(earnings[earnings['time'] == 'time-after-hours'] and earnings[earnings['time'] == 'time-after-hours'])
    print(df[(df['time'] == 'time-after-hours') & (df['marketCap'].str.len() > len('$1,000,000,00'))])  # 'time-after-hours'
