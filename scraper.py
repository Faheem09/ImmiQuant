import requests
from bs4 import BeautifulSoup
import pandas as pd

# URL of the data source
url = "https://usafacts.org/articles/what-can-the-data-tell-us-about-unauthorized-immigration/"

# Get the page content
response = requests.get(url)
if response.status_code == 200:
    soup = BeautifulSoup(response.content, 'html.parser')

    # Extract relevant data
    data_sections = soup.find_all('section')  # Adjust based on site structure
    immigration_data = []
    for section in data_sections:
        header = section.find('h2').text if section.find('h2') else None
        paragraph = section.find('p').text if section.find('p') else None
        immigration_data.append({'Section': header, 'Content': paragraph})
    
    # Convert to DataFrame for better handling
    df = pd.DataFrame(immigration_data)
    print(df.head())  # Display first few rows
else:
    print("Failed to retrieve the data.")
