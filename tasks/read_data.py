# + tags=["parameters"]
upstream = None
# -
from src.data.get_historical_data import main


def get_data(symbols, start_str="2022-03-1"):

    interval = "5m" 
    df_total = main(interval=interval, start_str=start_str, symbols_list=symbols)
    df_validation = df_total.iloc[:500]
    df_total = df_total.iloc[500:]
    return df_validation, df_total

def save_data(symbols, start_str, product):
    print(product)
    symbols = symbols.replace(" ", "").split(",")
    symbols = tuple(symbols)
    df_validation, df_total = get_data(symbols, start_str=start_str)
    df_total.to_csv(product["data_train"])
    df_validation.to_csv(product["data_validation"])