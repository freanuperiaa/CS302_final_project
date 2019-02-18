
# for plotting the data in graph
import matplotlib.pyplot as plt
from matplotlib import style
import matplotlib.ticker as mticker
#import matplotlib.finance as candlestick_ohlc

import data


def plot_hlc_average():
    data_forplot = data.get_hlc_average()
    style.use('seaborn-whitegrid')
    fig = plt.figure()
    plt.plot( data_forplot ,label = "HLC average")
    plt.xlabel('hlc average')
    plt.ylabel('')
    plt.title('Stock Prices of JFC in PSE ')
    plt.legend()
    plt.show()



def plot_ohlc_candlestick():
    print('test')
    data_forplot = data.get_ohlc()
    ls = []
    for x in data_forplot:
        string = x[1], x[2], x[3], x[4]
        ls.append(string)
    print(ls)



if __name__ == '__main__':
    plot_ohlc_candlestick()