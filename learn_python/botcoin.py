print('Hello world!')  # Python 3 syntax

# Read raw bitcoin price history from a csv file
mtgox_raw = read_bitcoin_csv('data/mtgoxUSD.csv')
# Get bitcoin OHLC data frame with 5min frequency
mtgox_ohlc = get_bitcoin_ohlc(mtgox_raw, '5min')
# Sample output
mtgox_ohlc['2013-01-01':].head()