import yaml
import pandas as pd
from binance.client import Client
from functools import lru_cache

def get_credentials():
    with open("config/keys.yaml", "r") as cfg_file:
        cfg = yaml.safe_load(cfg_file)
    return cfg

def load_credentials():
    cfg = get_credentials()
    API_KEY = cfg["REAL_ACCOUNT"]["API_KEY"]
    SECRET_KEY = cfg["REAL_ACCOUNT"]["SECRET_KEY"]
    return API_KEY, SECRET_KEY

def retrieve_data(*args, **kwargs):
    bars = client.get_historical_klines(*args, **kwargs)
    df = pd.DataFrame(bars)
    df["Date"] = pd.to_datetime(df.iloc[:,0], unit = "ms")
    df.columns = ["Open Time", "Open", "High", "Low", "Close", "Volume",
                  "Clos Time", "Quote Asset Volume", "Number of Trades",
                  "Taker Buy Base Asset Volume", "Taker Buy Quote Asset Volume", "Ignore", "Date"]
    df = df[["Date", "Open", "High", "Low", "Close", "Volume"]].copy()
    df.set_index("Date", inplace = True)
    for column in df.columns:
        df[column] = pd.to_numeric(df[column], errors = "coerce")
    return df

@lru_cache()
def main(interval, start_str, symbols_list=tuple(["BTCUSDT"])):
    df_total = pd.DataFrame()
    for symbol in symbols_list:
        df = retrieve_data(symbol=symbol, interval = interval, start_str=start_str)
        df.columns = ((symbol, k) for k in df.columns)
        df_total = pd.concat([df_total, df], axis=1)

    df_total.columns = pd.MultiIndex.from_tuples(df_total.columns)
    return df_total

# Load credentials
API_KEY, SECRET_KEY = load_credentials()

# Access real account Client
client = Client(api_key = API_KEY, api_secret = SECRET_KEY, tld = "com", testnet = False)

if __name__ == "__main__":
    df_total = main()
    print(df_total)

