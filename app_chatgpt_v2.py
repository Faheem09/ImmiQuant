import requests
from bs4 import BeautifulSoup
import pandas as pd
import plotly.express as px
import streamlit as st

# Step 1: Scrape the Webpage for Table Data
url = "https://www.cbp.gov/newsroom/stats/cbp-enforcement-statistics/criminal-noncitizen-statistics"
response = requests.get(url)
soup = BeautifulSoup(response.content, "html.parser")

# Extract all tables from the webpage
tables = soup.find_all("table")
dataframes = {}

# Extract titles and descriptions
titles = [title.text.strip() for title in soup.find_all("h2")]
descriptions = [desc.text.strip() for desc in soup.find_all("p")]

# Step 2: Convert each table to a DataFrame
for idx, table in enumerate(tables):
    headers = [header.text.strip() for header in table.find_all("th")]
    rows = []
    for row in table.find_all("tr")[1:]:  # Skip header row
        cells = [cell.text.strip() for cell in row.find_all(["td", "th"])]
        # Ensure the row has the same number of columns as headers
        while len(cells) < len(headers):
            cells.append("")
        rows.append(cells)
    df = pd.DataFrame(rows, columns=headers)
    dataframes[f"Table {idx + 1}"] = df

# Display data in Streamlit
st.title("Criminal Noncitizen Statistics")
st.write("Data sourced from CBP website.")

# Step 3: Interactive Plotly Visualizations in Streamlit
for idx, (name, df) in enumerate(dataframes.items()):
    st.header(titles[idx] if idx < len(titles) else name)
    st.write(descriptions[idx] if idx < len(descriptions) else "")
    st.dataframe(df)  # Display the table for reference

    # Convert columns to numeric if possible
    for col in df.columns:
        try:
            df[col] = pd.to_numeric(df[col])
        except ValueError:
            pass

    # Create a Plotly line chart
    if 'Date' in df.columns:
        fig = px.line(df, x='Date', y=df.columns[1:], title=f"{titles[idx] if idx < len(titles) else name} - Trends Over Time")
        st.plotly_chart(fig)
    else:
        st.write("No 'Date' column found for plotting.")