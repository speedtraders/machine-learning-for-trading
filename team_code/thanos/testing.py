from zipline.api import order, record, symbol
from zipline import run_algorithm
import pandas as pd
import pandas_datareader.data as web



def initialize(context):
    pass


def handle_data(context, data):
    order(symbol('AAPL'), 10)
    record(AAPL=data.current(symbol('AAPL'), 'price'))


start = pd.Timestamp('2014')
end = pd.Timestamp('2018')

# start = datetime(2015, 1, 1, 0, 0, 0, 0, pytz.utc)
# end = datetime(2016, 1, 1, 0, 0, 0, 0, pytz.utc)

sp500 = web.DataReader('SP500', 'fred', start, end).SP500

benchmark_returns = sp500.pct_change()

result = run_algorithm(start=start,
                       end=end,
                       initialize=initialize,
                       handle_data=handle_data,
                       capital_base=100000,
                       benchmark_returns=benchmark_returns,
                       bundle='quandl',
                       data_frequency='daily')

print(result)