import requests
import pandas as pd
from bs4 import BeautifulSoup
import plotly.express as px
import streamlit as st

# Step 1: Scrape the data
url = "https://www.cbp.gov/newsroom/stats/cbp-enforcement-statistics/criminal-noncitizen-statistics"
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

# Find all tables on the webpage
tables = soup.find_all('table')

# Parse each table into a DataFrame
dataframes = []
for table in tables:
    df = pd.read_html(str(table))[0]
    dataframes.append(df)

# Step 2: Load data into DataFrames
all_data = pd.concat(dataframes, ignore_index=True)

# Step 3: Create interactive charts with Plotly
fig = px.line(all_data, x='Date', y='Value', title='Criminal Noncitizen Statistics')

# Step 4: Create a Streamlit app
st.title('Criminal Noncitizen Statistics')

# Display the chart
st.plotly_chart(fig)

# Option to hide/show data
columns = st.multiselect('Select columns to display', all_data.columns, default=all_data.columns)
filtered_data = all_data[columns]

# Display the filtered data
st.write(filtered_data)