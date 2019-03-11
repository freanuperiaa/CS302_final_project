import matplotlib.pyplot as plt
from matplotlib import style
import matplotlib.ticker as mticker

#remove comments below if you're going to use the plot_ohlc_candlestick() method
#import plotly.plotly as ply
#import plotly.graph_objs as grapho

import data
import algorithms as algo

def plot_hlc_forecast():

    #get dates to be shown on graph
    df = data.get_data()
    dates = list(df['date'])
    date_show = [x for x in range(len(dates)) if x%(365//2) == 0]
    date = []
    for x in date_show:
        date.append(dates[x])

    #plot the graph
    data_forplot = data.get_hlc_average()
    style.use('seaborn-whitegrid')
    fig = plt.figure()
    plt.plot(data_forplot, label = "HLC average")


    # add the forecasted data
    plt.plot(algo.double_exponential_smoothing(), label = 'Double Exponential Smoothing Forecast')
    plt.plot(algo.weighted_moving_average(), label = 'Weighted Moving Average')


    plt.xlabel('time')
    plt.xticks(date_show, date, rotation = 50)
    plt.yticks([0,50,100,150,200], ['0 PHP', '50 PHP', '100 PHP', \
                                    '150 PHP', '200 PHP'])
    plt.ylabel('high,low, and close average')
    plt.title('Stock Prices of JFC in PSE ')
    plt.legend()
    plt.show()


def plot_ohlc_candlestick():
    """
        OHLC Candlestick Graph

        This plots the Opening, Low, High, and Closing stock price of the 
        JFC using the external API Plotly.
    """
    df = data.get_data()
    #plot the OHLC candlestick using Plotly
    trace = grapho.Ohlc(
        x = df['date'],
        open = df['open'],
        high = df['high'],
        low = df['low'],
        close = df['close']
    )
    data_ = [trace]
    ply.plot(data_, filename = 'JFC_candlestick')


def plot_hlc_average():
    data_forplot = data.get_hlc_average()
    #data_forplot = data.get_ohlc()   - should only use if
                                    #   you can do OHLC candlestick

    style.use('seaborn-whitegrid')
    fig=plt.figure()
    plt.plot( data_forplot ,label = "HLC average")
    plt.xlabel('hlc average')
    plt.ylabel('')
    plt.title('Stock Prices of JFC in PSE ')
    plt.legend()
    plt.show()



def plot_sma_forecast():

    #get dates to be shown on graph
    df = data.get_data()
    dates = list(df['date'])
    date_show = [x for x in range(len(dates)) if x%(365//2) == 0]
    date = []
    for x in date_show:
        date.append(dates[x])

    #plot the graph
    data_forplot = data.get_hlc_average()
    style.use('seaborn-whitegrid')
    fig = plt.figure()
    plt.plot(data_forplot, label = "HLC average")


    # add the forecasted data, remove the comments below to compare the sma forecast
    #to the Double Exponential Smoothing and Weighted Moving Average

    plt.plot(algo.double_exponential_smoothing(), label = 'Double Exponential Smoothing Forecast')
    plt.plot(algo.weighted_moving_average(), label = 'Weighted Moving Average')
    plt.plot(algo.simple_moving_average(), label = 'Simple Moving Average' )


    plt.xlabel('time')
    plt.xticks(date_show, date, rotation = 50)
    plt.yticks([0,50,100,150,200], ['0 PHP', '50 PHP', '100 PHP', \
                                    '150 PHP', '200 PHP'])
    plt.ylabel('high,low, and close average')
    plt.title('Stock Prices of JFC in PSE ')
    plt.legend()
    plt.show()

if __name__ == '__main__':
    plot_hlc_average()