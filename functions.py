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
    all_files.remove('Trades BR Receipt.csv')
    
    # Create list of dfs
    list_of_dfs = [pd.read_csv(filename, index_col=None, error_bad_lines=False) for filename in all_files]
    
    #Return output
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
