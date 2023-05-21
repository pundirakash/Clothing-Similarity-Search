# -*- coding: utf-8 -*-
"""
Created on Sun May 19 12:11:59 2023

@author: AKASH
"""
import pandas as pd
import tensorflow_hub as hub
import numpy as np

# Load the dataset
data = pd.read_csv('amazonFlipkartData.csv')

# Load the pre-trained Universal Sentence Encoder model
use_model = hub.load("https://tfhub.dev/google/universal-sentence-encoder-large/5")

def get_text_embedding(text):
    # Get the sentence embedding for the text
    text_embedding = use_model([text])[0]
    return text_embedding

# Preprocess the dataset and generate embeddings
use_embeddings = [get_text_embedding(description) for description in data['Description']]
np.save('use_embeddings.npy', use_embeddings)