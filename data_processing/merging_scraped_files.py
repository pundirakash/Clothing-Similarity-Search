# -*- coding: utf-8 -*-
"""
Created on Sun May 19 12:02:01 2023

@author: AKASH
"""
import pandas as pd

# Read the first CSV file
df1 = pd.read_csv('clothing_data_flipkart.csv')

# Read the second CSV file
df2 = pd.read_csv('clothing_data_amazon.csv')

# Merge the two dataframes
merged_df = pd.concat([df1, df2])

# Write the merged dataframe to a new CSV file
merged_df.to_csv('amazon_flipkart_data_uncleaned.csv', index=False)
