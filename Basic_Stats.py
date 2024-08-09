import requests
from bs4 import BeautifulSoup

# Fetch the HTML content of the page
url = 'https://www.screener.in/company/RELIANCE/'
response = requests.get(url,verify=False)
html_content = response.content

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(html_content, 'html.parser')

# Find the specific unordered list by its id or class
# For example, finding <ul id="specific-ul"> or <ul class="specific-class">
specific_ul = soup.find('ul', {'id': 'top-ratios'})  # or use {'class': 'specific-class'}

print("Specific UL")

# Define a function to recursively extract list items
def extract_list_items(ul):
    items = []
    for li in ul.find_all('li', recursive=False):
        # Extract text from the current list item
        item_text = li.get_text(strip=True)
        #print(item_text)
        items.append(item_text)

        # Check for nested unordered list
        nested_ul = li.find('ul')
        if nested_ul:
            nested_items = extract_list_items(nested_ul)
            items.extend(nested_items)

    return items


# Extract list items from the specific unordered list
if specific_ul:
    list_items = extract_list_items(specific_ul)
    for item in list_items:
        print(item)
else:
    print("Specified <ul> not found")
