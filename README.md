# Clothing Similarity Search

Clothing Similarity Search is an API-based application that finds similar clothing items based on a user's input text. It uses natural language processing techniques to analyze product descriptions and recommend similar items to the user. The application scrapes data from multiple sources, performs data preprocessing, generates embeddings using a pre-trained model, and utilizes cosine similarity for item matching.

## Features

- Scrapes data from Flipkart and Amazon to create a comprehensive dataset of clothing descriptions and url.
- Preprocesses the clothing description data by removing punctuation, sizes, and colors.
- Generates sentence embeddings using the Universal Sentence Encoder model.
- Provides an API endpoint for users to search for similar clothing items.
- Supports searching by providing a text query and retrieving a list of similar clothing items based on their descriptions.

## Installation

1. Clone the repository:
   ```shell
   git clone https://github.com/pundirakash/Clothing-Similarity-Search.git
   
2. Install the required dependencies: 
   ```shell
   pip install -r requirements.txt
 
3. Run the Flask application: 
   ```shell
   python app/app.py
   
## API Documentation

The Clothing Similarity Search API exposes the following endpoint:

### Endpoint
    URL: http://localhost:5000/api/find_similar_items
    Method: POST
### Request Body
The API expects a JSON object in the request body with the following structure:
Make a POST request to the **/api/find_similar_items** endpoint with the following JSON payload:

		{
    		"input_text": "blue summer dress",
    		"top_n": 5
		}
		
- input_text: The text describing the item you want to find similar items for.
- top_n (optional): The number of similar items to retrieve (default value is 5 if not specified).

### Response
The server will respond with a JSON object containing the top-N most similar items based on the input text. Each item will include a description and a URL. Here's an example response:
		
	{
			"results": [
					{
							"description": "Women's Blue Summer Dress",
							"url": "https://www.example.com/product/123"
					},
					{
							"description": "Blue Floral Print Summer Dress",
							"url": "https://www.example.com/product/456"
					},
					...
			]
	}


- The results array contains the top-N similar items, where each item has a description and a url.		

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvement, please open an issue or submit a pull request.


   
    

