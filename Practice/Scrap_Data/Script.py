import requests
from bs4 import BeautifulSoup

# Send a GET request to the website
url = "https://guidestarindia.org/Summary.aspx?CCReg=5348"
response = requests.get(url)

# Parse the HTML content
soup = BeautifulSoup(response.text, "html.parser")

# Find all <div> elements with class "CPBData"
div_elements = soup.find_all("div", class_="CPBData")

# Initialize an index for keys
index = 1

# Iterate through <div> elements and extract text from <span> and <a> tags
for div in div_elements:

    # Find all <span> and <a> tags within the <div> element
    spans = div.find_all("span")
    links = div.find_all("a")

    # Print text from <span> tags
    for span in spans:
        text = span.get_text(strip=True)
        text = text.replace(" ", "")  # Remove spaces
        print( text) 
