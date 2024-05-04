import requests
from bs4 import BeautifulSoup

# Send a GET request to the website
url = "https://guidestarindia.org/Summary.aspx?CCReg=5348"
response = requests.get(url)

# Parse the HTML content
soup = BeautifulSoup(response.text, "html.parser")

# Find all <div> elements with class "CPBData"
div_elements = soup.find_all("div", class_="CPBData")

# Initialize an empty dictionary to store data
data = {}

# Extract text from <span> tags and set the value without spaces
for div in div_elements:
  for span in div.find_all("span"):
    text = span.get_text(strip=True)
    next_sibling = span.find_next_sibling()
    next_text = next_sibling.get_text(strip=True) if next_sibling else None

    if not data.get('name'):
      data['name'] = text
    elif text:
      data[text] = next_text.strip() if next_text else ""  # Remove leading/trailing spaces and set empty string if next_text is None

# Print the data dictionary with space-removed values
print(data)
