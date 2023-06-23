import streamlit as st
st.set_page_config(
    page_title="Webscraping Methods (BeautifulSoup)",
    page_icon="🕷",

)
st.sidebar.success("develop by : HOSSEIN QASHQAEII 🧛")
st.image("bbb.png",width=500)

st.header("Static Scraping Example using BeautifulSoup: 🍜 ")


code = '''
import requests
from bs4 import BeautifulSoup

# Send an HTTP GET request to the target URL
response = requests.get('https://example.com')

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(response.text, 'html.parser')

# Extract specific data from the parsed HTML
title = soup.title.text
paragraphs = soup.find_all('p')
first_paragraph = paragraphs[0].text

# Print the extracted data
print('Title:', title)
print('First Paragraph:', first_paragraph)
'''
st.code(code, language="python")
st.write("This example demonstrates how to use the requests library to send an HTTP GET request to a web page and then use BeautifulSoup to parse the HTML content. It extracts the title of the page and the text from the first paragraph.")
st.markdown("---")
#___________________________________

st.header("Scraping HTML with BeautifulSoup: 🍜 ")
code = """
import requests
from bs4 import BeautifulSoup

# Send a GET request to the webpage
response = requests.get('https://www.example.com')

# Create a BeautifulSoup object
soup = BeautifulSoup(response.text, 'html.parser')

# Find and extract specific elements from the webpage
title = soup.title.text
paragraphs = soup.find_all('p')

# Print the extracted data
print('Title:', title)
for p in paragraphs:
    print('Paragraph:', p.text)


"""
st.code(code,language="python")
st.markdown("---")
#_________________________________________________________________
st.header("Scraping images from a website using BeautifulSoup 🍜 ")
code = """
import requests
from bs4 import BeautifulSoup
import urllib

# Send a GET request to the webpage
response = requests.get('https://www.example.com')

# Create a BeautifulSoup object
soup = BeautifulSoup(response.text, 'html.parser')

# Find all image tags and extract the source URLs
image_tags = soup.find_all('img')
image_urls = [img['src'] for img in image_tags]

# Download the images
for url in image_urls:
    urllib.request.urlretrieve(url, 'image.jpg')  # Replace 'image.jpg' with desired filename
Scraping data from an API using requests:
python
Copy code
import requests

# Send a GET request to the API endpoint
response = requests.get('https://api.example.com/data')

# Parse the JSON response
data = response.json()

# Extract and print the desired data
for item in data['items']:
    name = item['name']
    price = item['price']
    print('Name:', name)
    print('Price:', price)


"""
st.code(code,language="python")
st.markdown("---")
#____________________________________________________________
st.header("Scraping data from a table using BeautifulSoup: 🍜 ")
code = """
import requests
from bs4 import BeautifulSoup

# Send a GET request to the webpage
response = requests.get('https://www.example.com/table')

# Create a BeautifulSoup object
soup = BeautifulSoup(response.text, 'html.parser')

# Find the table element
table = soup.find('table')

# Extract data from table rows
for row in table.find_all('tr'):
    # Extract data from table cells
    cells = row.find_all('td')
    data = [cell.text.strip() for cell in cells]
    print(data)


"""
st.code(code,language="python")
st.markdown("---")
#_________________________________________________________________
#____________________________________________________________
st.header("Scraping data from multiple pages using BeautifulSoup 🍜 ")
code = """
import requests
from bs4 import BeautifulSoup

# Loop through multiple pages
for page in range(1, 6):
    # Send a GET request to the webpage with pagination
    response = requests.get(f'https://www.example.com?page={page}')

    # Create a BeautifulSoup object
    soup = BeautifulSoup(response.text, 'html.parser')

    # Extract and print the desired data from each page
    data = soup.find('div', class_='data-container')
    print(data.text)


"""
st.code(code,language="python")
st.markdown("---")
#_________________________________________________________________
#____________________________________________________________
st.header("Scraping data from an XML file using BeautifulSoup and requests 🍜 ")
code = """
import requests
from bs4 import BeautifulSoup

# Send a GET request to the XML file
response = requests.get('https://www.example.com/data.xml')

# Create a BeautifulSoup object
soup = BeautifulSoup(response.text, 'xml')

# Extract and print the desired data
data = soup.find_all('item')
for item in data:
    name = item.find('name').text
    price = item.find('price').text
    print(name, price)

"""
st.code(code,language="python")
st.markdown("---")
#_________________________________________________________________
#____________________________________________________________
st.header("Scraping all links from a webpage With BeautifulSoup 🍜 ")
code = """
import requests
from bs4 import BeautifulSoup

# Send a GET request to the webpage
response = requests.get('https://www.example.com')

# Create a BeautifulSoup object
soup = BeautifulSoup(response.text, 'html.parser')

# Find all <a> tags for links
links = soup.find_all('a')

# Extract and print the href attribute of each link
for link in links:
    print(link.get('href'))


"""
st.code(code,language="python")
st.markdown("---")
#_________________________________________________________________
#____________________________________________________________
st.header("Scraping data using CSS selectors , in BeautifulSoup 🍜 ")
code = """
import requests
from bs4 import BeautifulSoup

# Send a GET request to the webpage
response = requests.get('https://www.example.com')

# Create a BeautifulSoup object
soup = BeautifulSoup(response.text, 'html.parser')

# Use CSS selectors to find specific elements
elements = soup.select('.class-name')  # Find elements by class name
# elements = soup.select('#id')  # Find elements by id
# elements = soup.select('tag')  # Find elements by tag name

# Extract and print the text content of the selected elements
for element in elements:
    print(element.text)

"""
st.code(code,language="python")
st.markdown("---")
#_________________________________________________________________
