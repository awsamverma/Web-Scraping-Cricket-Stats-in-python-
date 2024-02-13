import pandas as pd
import requests
from bs4 import BeautifulSoup

# URL of the page containing cricket stats
url = 'https://www.espncricinfo.com/records/tournament/averages-batting-bowling-by-team/icc-cricket-world-cup-2023-24-15338?team=6'

# Send a GET request to the URL
r = requests.get(url)

# Parse the HTML content
soup = BeautifulSoup(r.text, 'html.parser')
# print(soup)


# # Find the table header (thead) and table body (tbody) elements
table_head = soup.find('thead')
table_body = soup.find('tbody')
#
# # Extract column names from the table header
column_names = [th.text.strip() for th in table_head.find_all('span', class_='ds-cursor-pointer')]
#
# print(column_names)
# # Extract rows from the table body
rows = []
for tr in table_body.find_all('tr'):
    row = [td.text.strip() for td in tr.find_all('td')]
    rows.append(row)
# print(rows)
# # Create a DataFrame from the extracted data
df = pd.DataFrame(rows, columns=column_names)
#
print(df)
# Save the DataFrame to a CSV file
df.to_csv('cricket_stat.csv', index=False)
#
print("DataFrame saved to cricket_stat.csv")

