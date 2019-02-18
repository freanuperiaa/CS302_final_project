import pandas as pd
import numpy as np

#for reading CSV

def get_data():
    df_unfiltered  = pd.read_csv("data/data.csv", header=0 , usecols=['c','h','l','o','t','v','symbol']) #read csv, select these as header and columns
    df_unfiltered.columns = ['close','high','low','open','date','volume','symbol'] #change column names
    #make a new dataframe that only has jollibee in it
    #the JFC starts in 367305th row to 373331th row
    df = df_unfiltered[df_unfiltered['symbol'].isin(['JFC'])] 

    return df


def get_ohlc():
    df = get_data()

    #get the open, low, high, close  values in the dataframe for OHLC chart
    x = 0
    y = len(df)
    ohlc = []
    while (x<y):
        # curr_row = [df.at[x,'date'], df.iat[x,'open'], df.iat[x,'high'], df.iat[x,'low'],
        # df.iat[x,'close'], df.iat[x,'volume']]
        curr_row = [ df['date'].values[x], df['open'].values[x] , df['low'].values[x],
                    df['high'].values[x], df['close'].values[x], df['volume'].values[x]
        ]
        ohlc.append(curr_row)
        x += 1
#    for x in ohlc:
#        print(x)
    #return matrix of open, low, high, close, and average
    return ohlc

def get_hlc_average():
    df = get_data()
    
    #get the high, low, close and average it
    x = 0
    y = len(df)
    hlc = []
    while (x<y):
        total = df['high'].values[x] + df['low'].values[x] + df['close'].values[x]
        average = total/4
        hlc.append(average)
        x += 1
#    print(hlc)

    return hlc


if __name__ == '__main__':
    get_ohlc()  