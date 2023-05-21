# -*- coding: utf-8 -*-
"""
Created on Sun May 19 11:48:06 2023

@author: AKASH
"""
import pandas as pd
import re

# Read the scraped data from CSV file
df = pd.read_csv('amazonFlipkartDataUncleaned.csv')

# Preprocess the description column
def preprocess_text(text):
    # Convert to lowercase
    text = text.lower()

    # Remove punctuation
    text = re.sub(r'[^\w\s]', '', text)

    # Remove sizes or colors
    text = re.sub(r'\b(?:\d+ml|\d+oz|\d+cl|\d+ltr|s|m|l|xl|xxl|red|blue|green|black|white)\b', '', text)

    # Remove extra whitespaces
    text = re.sub(r'\s+', ' ', text).strip()

    return text

# Apply preprocessing to the description column
df['Description'] = df['Description'].apply(preprocess_text)

# Save the preprocessed data to a new CSV file
df.to_csv('amazonFlipkartData.csv', index=False)
