import requests
from bs4 import BeautifulSoup
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

# Step 1: Web Scraping
url = "https://usafacts.org/articles/what-can-the-data-tell-us-about-unauthorized-immigration/"
response = requests.get(url)
if response.status_code == 200:
    soup = BeautifulSoup(response.content, 'html.parser')

    # Extract relevant data
    data_sections = soup.find_all('section')
    immigration_data = []
    for section in data_sections:
        header = section.find('h2').text if section.find('h2') else None
        paragraph = section.find('p').text if section.find('p') else None
        immigration_data.append({'Section': header, 'Content': paragraph})
    
    # Convert to DataFrame for further processing
    df = pd.DataFrame(immigration_data)
else:
    print("Failed to retrieve data.")

# Step 2: Data Cleaning (Assuming 'Year', 'Population', 'Country', and 'Criminality Rate' columns for plotting)
# Add mock data for demonstration purposes if not included in the scraped data
if 'Year' not in df.columns:
    df['Year'] = [2000, 2005, 2010, 2015, 2020]  # Sample years
if 'Population' not in df.columns:
    df['Population'] = [8.2, 9.1, 10.3, 11.5, 12.7]  # Sample population data
if 'Country' not in df.columns:
    df['Country'] = ['Mexico', 'India', 'China', 'El Salvador', 'Guatemala']
if 'Criminality Rate' not in df.columns:
    df['Criminality Rate'] = [5, 3, 2, 6, 4]  # Sample criminality data

# Step 3: Visualization Functions
def plot_population_over_time(df):
    plt.figure(figsize=(10, 6))
    sns.lineplot(data=df, x='Year', y='Population', marker='o')
    plt.title('Estimated Immigrant Population Over Time')
    plt.xlabel('Year')
    plt.ylabel('Population Estimate')
    plt.show()

def plot_criminality_by_country(df):
    plt.figure(figsize=(12, 6))
    sns.barplot(data=df, x='Country', y='Criminality Rate')
    plt.title('Criminality Rates by Country of Origin')
    plt.xlabel('Country')
    plt.ylabel('Criminality Rate (%)')
    plt.xticks(rotation=45)
    plt.show()

# Step 4: Plotting if Running as Standalone Script
if __name__ == "__main__":
    plot_population_over_time(df)
    plot_criminality_by_country(df)

# Step 5: Streamlit Dashboard
st.title("Economic Impact of Illegal & Undocumented Immigrants in the US")
st.write("A dashboard to explore immigration data and its economic impact.")

# Display the scraped data in Streamlit
st.dataframe(df)

# Interactive line chart in Streamlit
if 'Population' in df.columns:
    st.line_chart(df.set_index('Year')['Population'])
