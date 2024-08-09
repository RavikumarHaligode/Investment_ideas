import requests
from bs4 import BeautifulSoup
import pandas as pd

# URL of the webpage to scrape
url = "https://www.screener.in/company/RELIANCE/consolidated/"

# Send a GET request to the webpage
response = requests.get(url,verify=False)
if response.status_code == 200:
    # Parse the webpage content
    soup = BeautifulSoup(response.content, 'html.parser')

      # Extract the main profit and loss table
    Balance_Sheet_Table = soup.select_one("#balance-sheet .data-table")

    # Extract headers
    headers = [th.get_text(strip=True) for th in Balance_Sheet_Table.find_all("th")]
    headers[0] = "Metrics"
    # Extract rows
    rows = []
    for tr in Balance_Sheet_Table.find_all("tr")[1:]:  # Skip header row
        row = [td.get_text(strip=True).replace(",", "") for td in tr.find_all("td")]
        rows.append(row)

    # Convert to DataFrame
    df_Balance_Sheet = pd.DataFrame(rows, columns=headers)

    # Print the DataFrame
    print("Balance Sheet DataFrame:")
    df_Balance_Sheet['Metrics'] = df_Balance_Sheet['Metrics'].str.replace('+', ' ')
    print(df_Balance_Sheet)

    # Optional: Save the DataFrame to a CSV file
    df_Balance_Sheet.to_csv('Balance_Sheet_Data.csv', index=False)
else:
    print("Failed to retrieve the webpage")
