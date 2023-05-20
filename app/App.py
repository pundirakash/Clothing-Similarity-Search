# -*- coding: utf-8 -*-
"""
This code is a Flask app that finds similar items based on a user's input text.

Created on Sat May 20 22:14:23 2023

@author: AKASH
"""

# Import necessary libraries
from flask import Flask, request, jsonify
import tensorflow_hub as hub
from sklearn.metrics.pairwise import cosine_similarity
import pandas as pd
import numpy as np
import os

# Get the current directory path
current_dir = os.path.dirname(os.path.abspath(__file__))

# Load the data
data = pd.read_csv(os.path.join(current_dir, '../data/amazonFlipkartData.csv'))

# Load the pre-trained Universal Sentence Encoder model
use_model = hub.load("https://tfhub.dev/google/universal-sentence-encoder-large/5")

# Create a Flask app
app = Flask(__name__)

# Define a function to get the text embedding for a given text
def get_text_embedding(text):
    # Get the sentence embedding for the text
    text_embedding = use_model([text])[0]
    return text_embedding

# Define a function to find the top-N most similar items to a given text
def find_similar_items(input_text, top_n):
    # Get the embedding of the input text
    input_embedding = get_text_embedding(input_text)

    # Load the embeddings of the items in the dataset
    use_embeddings = np.load(os.path.join(current_dir, '../data/use_embeddings.npy'))

    # Calculate the cosine similarity between the input embedding and the embeddings in use_embeddings
    similarities = cosine_similarity([input_embedding], use_embeddings)[0]

    # Get the indices of the top-N most similar items
    top_indices = similarities.argsort()[::-1][:top_n]

    # Retrieve the URLs of the top-N most similar items
    top_urls = data.iloc[top_indices]['URL'].values.tolist()

    return top_urls

# Define a route to find similar items based on a POST request
@app.route('/api/find_similar_items', methods=['POST'])
def find_similar_items_cloud():
    # Get the text input and top_n from the request
    input_text = request.json['input_text']
    top_n = request.json.get('top_n', 5)  # Default value is 5 if top_n is not specified

    # Find the similar items based on the input text and top_n value
    top_urls = find_similar_items(input_text, top_n)

    # Create a JSON response
    response = {
        'top_urls': top_urls
    }

    # Return the JSON response
    return jsonify(response)

# Run the app
if __name__ == '__main__':
    app.run()
