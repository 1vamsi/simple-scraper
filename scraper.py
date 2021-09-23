from bs4 import BeautifulSoup
import requests
import pandas as pd

COLUMNS = ['Team', 'Medal']

urls = ['https://crida.in/india-medals-in-olympics-winners-medal-count-table-by-country/']
dataframes = []
for url in urls:
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    
    table = soup.find("table") # Find the "table" tag in the page
    rows = table.find_all("tr") # Find all the "tr" tags in the table
    cy_data = []
    
    for row in rows:
        cells = row.find_all("td") #  Find all the "td" tags in each row
        cells = cells[0:2] # Select the correct columns
        cy_data.append([cell.text for cell in cells]) # For each "td" tag, get the text inside it

    dataframes.append(pd.DataFrame(cy_data, columns=COLUMNS).drop(0, axis=0))

data = pd.concat(dataframes)
