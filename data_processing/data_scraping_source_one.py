# -*- coding: utf-8 -*-
"""
Created on Sun May 19 11:45:42 2023

@author: AKASH
"""
# Import the necessary libraries
import requests
from bs4 import BeautifulSoup
import csv
import urllib.parse

# Define a function to scrape the website
def scrape_website(url):
    # Send a GET request to the website
    response = requests.get(url)

    # Create a BeautifulSoup object to parse the HTML content
    soup = BeautifulSoup(response.content, 'html.parser')

    # Extract the clothing item descriptions and URLs
    descriptions = []
    urls = []
    for element in soup.find_all('a', class_='IRpwTa'):
        description = element.text
        url = element['href']
        descriptions.append(description)
        urls.append(url)

    return descriptions, urls

# Define a function to save the data to a CSV file
def save_data(descriptions, urls, filename):
    # Open the CSV file in append mode
    with open(filename, 'a', newline='', encoding='utf-8') as file:
        # Create a CSV writer object
        writer = csv.writer(file)

        # Write the header row
        writer.writerow(['Description', 'URL'])

        # Write the data rows
        for i in range(len(descriptions)):
            url = "https://www.flipkart.com" + urls[i]
            writer.writerow([descriptions[i], url])

# List of search terms
search_terms = [
    'Clothes',
    'Men Clothes',
    'Women Dresses',
    'Summer T-shirts',
    'Formal Wear',
    'Sports Jackets',
    'Casual Pants',
    'Winter Coats',
    'Party Dresses',
    'Swimwear',
    'Workout Leggings',
    'Formal Shirts',
    'Hoodies',
    'Skirts',
    'Denim Jeans',
    'Sneakers',
    'Blazers',
    'Tank Tops',
    'Shorts',
    'Watches',
    'Hats',
    'Socks',
    'Belts',
    'Jumpsuits',
    'Raincoats',
    'Suits',
    'Scarves',
    'Lingerie',
    'Polo Shirts',
    'Bikinis',
    'V-Neck Sweaters',
    'Windbreakers'
]

# Create a single CSV file
filename = 'clothing_data_flipkart.csv'

# Write the header row to the CSV file
with open(filename, 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Description', 'URL'])

# Scrape and save data for each search term
for term in search_terms:
    # Encode the search term
    encoded_term = urllib.parse.quote(term)

    # Create the base URL
    base_url = f"https://www.flipkart.com/search?q={encoded_term}&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=off&as=off&page="

    # Create empty lists to store the descriptions and URLs
    descriptions = []
    urls = []

    # Scrape multiple pages
    for page in range(1, 25):
        # Create the URL for the current page
        url = base_url + str(page)

        # Scrape the website
        page_descriptions, page_urls = scrape_website(url)

        # Add the descriptions and URLs to the lists
        descriptions.extend(page_descriptions)
        urls.extend(page_urls)

    # Save the data to the CSV file
    save_data(descriptions, urls, filename)
