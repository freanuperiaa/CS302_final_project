import algorithms as algo
import numpy as np


def test_accuracy(actual_data, forecast):
    """
        Test for Accuracy

        This method is going to compare the values yielded by a forecast from
        the algorithms module to the actual value by computing the percentage
        error for each day, then summing it all up by averaging
    """

    err_perc = []
    if len(actual_data) != len(forecast):
        print('size of forecast list is not the same with actual data')
    else:
        for x in range(len(actual_data)):
            error = abs(forecast[x] - actual_data[x])
            percentage = error/actual_data[x]
            err_perc.append(percentage)
    
    total_perc = 0
    sum = 0
    for x in range(len(err_perc)):
        sum += err_perc[x]
    total_perc = sum / len(err_perc)

    return err_perc, total_perc
    

