# Description: This script reads all the .sav files in the db folder and combines them into a single .csv file. Takes data from 2012 to 2021.
# Input: db/2012.sav, db/2013.sav, ..., db/2021.sav
# Output: defunciones.csv

import os
import pandas as pd
import pyreadstat

def read_sav_files():
    df_list = []
    for year in range(2012, 2022):
        file = f'db/{year}.sav'
        if os.path.exists(file):
            df, meta = pyreadstat.read_sav(file)
            df_list.append(df)

    # Combine all dataframes into a single dataframe
    df_all = pd.concat(df_list, ignore_index=True)
    
    # Save the dataframe to a csv file
    df_all.to_csv('defunciones.csv', index=False)

# Call the function
read_sav_files()

