import requests
from bs4 import BeautifulSoup
import sys

def scrape_fashion_articles(url):
    # Send a request to the website
    response = requests.get(url)
    
    # Check if the request was successful
    if response.status_code == 200:
        # Parse the HTML content
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Find the relevant sections for articles
        articles = soup.find_all('li', class_='highlight')  # Adjust the class name based on the website's structure
        
        # Loop through each article and extract information
        for article in articles:
            title = article.find('h2').text  # Adjust the tag and class name based on the website's structure
            date = article.find('time', class_='date-class')['datetime']  # Adjust the class name and attribute
            content = article.find('div', class_='content-class').text  # Adjust the class name

if __name__ == '__main__':
    if len(sys.argv) > 1:
        url = sys.argv[1]
        scrape_fashion_articles(url)
    else:
        print("No URL provided")
