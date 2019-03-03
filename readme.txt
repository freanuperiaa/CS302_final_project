in order to run the external API plotly, you should

1.) install plotly
    $pip3 install plotly
    or
    $sudo pip3 install plotly

2.) enter python interactive mode
    $ python3

3.) enter to the shell:
    >>> import plotly 
    >>> plotly.tools.set_credentials_file(\
    ... username='magnussonfrancis', api_key='C84T65u0x47jOpd1hgvq')

        *note: the password mentioned is not my password :P*

4.) then just simply just import plot module, then use plot_ohlc_candlestick()
    >>> import plot
    >>> plot.plot_ohlc_candlestick()

    -this will link you to a site where they will show you the graph


