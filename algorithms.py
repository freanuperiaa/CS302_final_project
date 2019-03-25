
#forecasting techniques

import data
import test
import pandas as pd


def double_exponential_smoothing():
    """
        Double Exponential Smoothing

        using the exponential smoothing with 
        respect to the trend in the historical
        data

    """
    #take values from the data module
    actual_data = list(data.get_hlc_average())

    #set the alpha and beta values
    alpha, beta = 0.35, 0.35

    #initialization of lists
    forecast_data = [actual_data[0],]
    estimated_trend = [0]
    trend_adjusted_forecast = [actual_data[0]]
    
    for x in range(len(actual_data)):
        if x == 0 :
            pass

        else:
            #calculating level/trend
            tt = (beta * (actual_data[x - 1] - forecast_data[x - 1])) + \
                        ((1 - beta) * estimated_trend[x - 1] )  
            estimated_trend.append(tt)
            #calculating forecast
            ft = (alpha * actual_data[x - 1]) + ((1 - alpha) * \
                        (forecast_data[x - 1] + estimated_trend[x - 1]))
            forecast_data.append(ft)
            #adjusting the forecast with the trend
            aft = ft + tt
            trend_adjusted_forecast.append(aft)

    #test accuracy here
    errors, total_error = test.test_accuracy(actual_data, trend_adjusted_forecast)
    print('the error percentage of the second-order exponential smoothing '
                                        'forecast is: ', total_error)
    return trend_adjusted_forecast


def weighted_moving_average():
    """
        Weighted Moving Average

        an improved version of the simple moving average,
        the Weighted Moving Average makes forecast based on
        previous actual data, depending on how far a particular 
        entry's time is from the time of the forecast
    """
    #take values from the data module
    actual_data = list(data.get_hlc_average())
    wma_forecast = []

    #weighted moving average
    for x in range(len(actual_data)):
        if x<4:
            #first four elements are going to take in actual data
            wma_forecast.append(actual_data[x])
        else:
            #this is where the forecast begins
            wma_forecast.append(
                ((actual_data[x - 4] * 0.4) + (actual_data[x - 3] * 0.3) +
                (actual_data[x - 2] * 0.2) + (actual_data[x - 1] * 0.1))
            )


     #test accuracy here
    errors, total_error = test.test_accuracy(actual_data, wma_forecast)
    print('the error percentage of the weighted moving average forecast is: '
                , total_error)
    return wma_forecast



def simple_moving_average():
    """
        Simple Moving Average

        a forecasting technique where it takes the last n actual values
        then takes the average of it as the forecast. This is not a good
        forecasting technique, this shall only be used for comparing to the
        other forecasting techniques
    """
    #take values from the data module
    actual_data = list(data.get_hlc_average())
    sma_forecast = []

    #simple moving average
    for x in range(len(actual_data)):
        if x<3:
            sma_forecast.append(actual_data[x])
        else:
            forecast = (actual_data[x - 3] + actual_data[x - 2] + actual_data[x - 1])/3
            sma_forecast.append(forecast)
    

    #test accuracy here
    errors, total_error = test.test_accuracy(actual_data, sma_forecast)
    print('the error percentage of the simple moving average forecast is: '
                , total_error)

    return sma_forecast        


if __name__ == '__main__':
    print(double_exponential_smoothing())



