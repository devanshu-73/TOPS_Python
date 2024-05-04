# # import requests
# # from bs4 import BeautifulSoup

# # # Send a GET request to the website
# # url = "https://guidestarindia.org/Summary.aspx?CCReg=5348"
# # response = requests.get(url)

# # # Parse the HTML content
# # soup = BeautifulSoup(response.text, "html.parser")

# # # Find all <div> elements with class "CPBData"
# # div_elements = soup.find_all("div", class_="CPBData")

# # # Initialize an index for keys
# # index = 1

# # # Iterate through <div> elements and extract text from <span> and <a> tags
# # for div in div_elements:
# #     # print(f"{index}:")
# #     # Find all <span> and <a> tags within the <div> element
# #     spans = div.find_all("span")
# #     links = div.find_all("a")

# #     # Print text from <span> tags
# #     for span in spans:
# #         print( span.get_text(strip=True))

# #     # Print text from <a> tags
# #     for link in links:
# #         print(link.get_text(strip=True))

# #      # Increment index for the next div


# import requests
# from bs4 import BeautifulSoup

# # Send a GET request to the website
# url = "https://guidestarindia.org/Summary.aspx?CCReg=5348"
# response = requests.get(url)

# # Parse the HTML content
# soup = BeautifulSoup(response.text, "html.parser")

# # Find all <div> elements with class "CPBData"
# div_elements = soup.find_all("div", class_="CPBData")

# # Initialize an index for keys
# index = 1

# # Iterate through <div> elements and extract text from <span> and <a> tags
# for div in div_elements:
#     # print("{index}:")
#     # Find all <span> and <a> tags within the <div> element
#     spans = div.find_all("span")
#     links = div.find_all("a")

#     # Print text from <span> tags
#     for span in spans:
#         if "Mobile" in span.get_text(strip=True):  # Check if the text contains "Mobile"
#             mobile_number = span.get_text(strip=True)
#             # Insert "-" after the second digit
#             mobile_number_with_dash = mobile_number[:3] + "-" + mobile_number[3:]
#             print("Mobile:", mobile_number_with_dash)
#         else:
#             print( span.get_text(strip=True))

#     # Print text from <a> tags
#     for link in links:
#         print("Link:", link.get_text(strip=True))

#     index += 1  # Increment index for the next div



# ====================================================================================================================================================
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


# =============================================printing in proper way  but not key vakles format ==================================

# import requests
# from bs4 import BeautifulSoup

# # Send a GET request to the website
# url = "https://guidestarindia.org/Summary.aspx?CCReg=5348"
# response = requests.get(url)

# # Check if the request was successful
# if response.status_code == 200:
#     # Parse the HTML content
#     soup = BeautifulSoup(response.text, "html.parser")

#     # Find all <div> elements with class "CPBData"
#     div_elements = soup.find_all("div", class_="CPBData")

#     # Initialize an index for keys and a dictionary for data
#     index = 1
#     data = {}

#     # Iterate through <div> elements and extract text from <span> and <a> tags
#     for div in div_elements:
#         # Find all <span> and <a> tags within the <div> element
#         spans = div.find_all("span")
#         links = div.find_all("a")

#         # Store text from <span> tags
#         span_values = [span.get_text(strip=True).replace(" ", "") for span in spans]
#         data[index] = span_values

#         # Store text from <a> tags
#         link_values = [link.get_text(strip=True) for link in links]
#         data[index].extend(link_values)

#         index += 1

#     # Print the data in key-value pairs
#     for key, value in data.items():
#         print(f"{key}: {value}")
# else:
#     print(f"Failed to retrieve the webpage. Status code: {response.status_code}")