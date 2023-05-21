# -*- coding: utf-8 -*-
"""
Created on Sun May 19 11:56:20 2023

@author: AKASH
"""
# Import necessary libraries
import requests
from bs4 import BeautifulSoup
import csv
import urllib.parse

# Function to scrape a website
def scrape_website(url):
    # Set headers for the GET request
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.93 Safari/537.36',
        'Accept': '*/*',
        'Accept-Language': 'en-US, en;q=0.5',
        'Cookie':'<cookie-data>'
    }

    # Send a GET request to the website
    response = requests.get(url, headers=headers)

    # Check if the request was successful
    if response.status_code == 200:
        # Create a BeautifulSoup object to parse the HTML content
        soup = BeautifulSoup(response.content, 'html.parser')

        # Extract the clothing item descriptions and URLs
        descriptions = []
        urls = []
        for element in soup.find_all('div', class_='a-section a-spacing-small puis-padding-left-micro puis-padding-right-micro'):
            description = element.find('span', class_='a-size-base-plus a-color-base a-text-normal').text.strip()
            url = element.find('a')['href']
            descriptions.append(description)
            urls.append(url)

        return descriptions, urls
    else:
        # Raise an exception if the request failed
        raise Exception('Request failed with status code {}'.format(response.status_code))

# Function to save data to a CSV file
def save_data(descriptions, urls, filename):
    with open(filename, 'a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        for i in range(len(descriptions)):
            url = "https://www.amazon.in" + urls[i]
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

# Scrape multiple search terms and pages on Amazon
for term in search_terms:
    descriptions = []
    urls = []

    # Scrape multiple pages for each search term
    for page in range(1, 11):  # Scraping pages 1 and 2, change the range as per your requirement
        base_url = f"https://www.amazon.in/s?k={urllib.parse.quote(term)}&page="
        url = base_url + str(page)
        page_descriptions, page_urls = scrape_website(url)
        descriptions.extend(page_descriptions)
        urls.extend(page_urls)

    # Save scraped data to a CSV file
    save_data(descriptions, urls, 'clothing_data_amazon.csv')
