import requests
from bs4 import BeautifulSoup
import pandas as pd

#driver = webdriver.Chrome()
# URL of the webpage to scrape
url = "https://www.screener.in/company/RELIANCE/consolidated/"

# Send a GET request to the webpage
response = requests.get(url,verify=False)
if response.status_code == 200:
  # Parse the webpage content
  soup = BeautifulSoup(response.content, 'html.parser')

  Sales_CAGR=[]
  Profit_CAGR=[]
  Price_CAGR=[]
  ROE_CAGR=[]
  # Use the selector to find the desired element
  element = soup.select_one("#profit-loss > div:nth-child(4) > table:nth-child(1)")

  if element:
    # Extract and print the text content of the element
    print(element.get_text())
    Sales_CAGR.append(element.get_text())
  else:
    print("Element not found")
  element = soup.select_one("#profit-loss > div:nth-child(4) > table:nth-child(2)")

  if element:
    # Extract and print the text content of the element
    print(element.get_text())
    Profit_CAGR.append(element.get_text())
  else:
    print("Element not found")

  element = soup.select_one("#profit-loss > div:nth-child(4) > table:nth-child(3)")

  if element:
    # Extract and print the text content of the element
    print(element.get_text())
    Price_CAGR.append(element.get_text())
  else:
    print("Element not found")

  element = soup.select_one("#profit-loss > div:nth-child(4) > table:nth-child(4)")

  if element:
    # Extract and print the text content of the element
    print(element.get_text())
    ROE_CAGR.append(element.get_text())
  else:
    print("Element not found")
else:
  print("Failed to retrieve the webpage")

print(Sales_CAGR)
print(Profit_CAGR)
print(Price_CAGR)
print(ROE_CAGR)

periods = ["10 Years", "5 Years", "3 Years", "TTM"]
sales_cagr = [10.5, 12.3, 15.0, 18.7]  # Replace with actual values
profit_cagr = [8.0, 9.5, 11.2, 14.1]  # Replace with actual values
price_cagr = [7.5, 8.7, 10.3, 13.0]  # Replace with actual values
roe_cagr = [6.5, 7.8, 9.0, 12.5]  # Replace with actual values

# Create a dictionary with the data
data = {
    "Period": periods,
    "Sales_CAGR": sales_cagr,
    "Profit_CAGR": profit_cagr,
    "Price_CAGR": price_cagr,
    "ROE_CAGR": roe_cagr
}

# Convert the dictionary to a pandas DataFrame
df = pd.DataFrame(data)
print(df)
df.to_csv('CAGR.csv', index=False)
