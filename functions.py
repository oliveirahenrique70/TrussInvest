### Truss Interactive Report Functions ###
### April 2021 ###

# Import packages
import os
import glob
import pandas as pd
import ipywidgets as widgets

# 1. Function to get trades
def Get_Trades():

    # Get files names
    all_files = glob.glob('*.csv')
    
    # Remove receipt files
    all_files.remove('BR Receipt.csv')
    all_files.remove('US Futures Receipt.csv')
    all_files.remove('US Equities Receipt.csv')
    all_files.remove('All Trades Receipt.csv')

    # Create list of dfs
    list_of_dfs = [pd.read_csv(filename, index_col=None, error_bad_lines=False) for filename in all_files]
    
    # Return output
    return(list_of_dfs)

# 2. Set table negative values as red
def color_negative_red(x):
    color = 'red' if x < 0 else 'black'
    return 'color: %s' % color

# 3. Create submit button
def Button_Sumbmit():
    
    # Create button
    output = widgets.Button(description='Submmit',
                                tooltip = 'OK',
                                icon='check',
                                button_style = 'success')
    
    # Return output
    return(output)

# 5. Create clean button
def Button_Clean():
    
    # Create button
    output = widgets.Button(description='Clean',
                                tooltip = 'OK',
                                icon='remove',
                                button_style = 'danger')
    
    # Return output
    return(output)

# 6. Display red and bold text
def prRed(skk): print('\033[1m' + "\033[91m {}\033[00m" .format(skk))
