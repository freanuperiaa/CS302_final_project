
#forecasting techniques

import data
import pandas as pd


def double_exponential_smoothing():
    """
        double exponential smoothin

        using the exponential smoothing with 
        respect to the trend in the historical
        data

    """
    actual_data = list(data.get_hlc_average())
    print(actual_data)
    #set the alpha and beta values
    alpha, beta = 0.5, 0.5
    #initialization of lists
    forecast_data = [actual_data[0],]
    estimated_trend = [0]
    trend_adjusted_forecast = [actual_data[0]]
    
    for x in range(len(actual_data)):
        if x == 0 :
            pass

        else:
            tt = (beta * (actual_data[x - 1] - forecast_data[x - 1])) + ((1 - beta) * estimated_trend[x - 1] )  
            estimated_trend.append(tt)
            ft = (alpha * actual_data[x - 1]) + ((1 - alpha) * (forecast_data[x - 1] + estimated_trend[x - 1]))
            forecast_data.append(ft)
            aft = ft + tt
            trend_adjusted_forecast.append(aft)

    return trend_adjusted_forecast










if __name__ == '__main__':
    print(double_exponential_smoothing())



