### Truss Interactive Report Functions ###
### March 2021 ###

# Import packages
import os
import glob
import pandas as pd
import datetime as dt
import ipywidgets as widgets

# 1. Function to get trades
def Get_Trades(x):

    # Change working directory
    os.chdir(x)

    # Get files names
    all_files = glob.glob('*.csv')

    # Create list of dfs
    list_of_dfs = [pd.read_csv(filename, index_col=None, error_bad_lines=False, sep=',') for filename in all_files]
    
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

# 6. Refine BR receipt
def Refine_BR_receipt(x):

    # Fill missing values 
    x['FX Description'].fillna('-', inplace=True)
    x['Valor dos Negocios'].fillna('-', inplace=True)
    x['Comm'].fillna('-', inplace=True)
    x['Exc Fee'].fillna('-', inplace=True)
    x = x.fillna(0)

    # Create Nota BM&F cumulative sum
    x['Nota BM&F Cum Sum'] = x['Nota BM&F'].cumsum()
    x['FX Value Cum Sum'] = x['FX Value'].cumsum()

    # Create Settlement cumulative sum
    x['Settlement Cum Sum'] = x['Nota BM&F'].shift(1)
    x['Settlement Cum Sum'] = x['Settlement Cum Sum'].fillna(0) + x['FX Value']
    x['Settlement Cum Sum'] = x['Settlement Cum Sum'].cumsum()

    # Create total vector
    x['Total Cum Sum'] = x['Nota BM&F'] + x['FX Value']

    # Apply cumulative sum to total vector
    x['Total Cum Sum'] = x['Total Cum Sum'].cumsum()
    
    # Return output
    return(x)