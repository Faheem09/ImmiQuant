import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
import pandas as pd

# Sample Data (replace this with your actual DataFrame)
# Ensure 'df' has columns 'Year', 'Population', 'Country', and 'Criminality Rate'
data = {
    'Year': [2000, 2005, 2010, 2015, 2020],
    'Population': [8.2, 9.1, 10.3, 11.5, 12.7],
    'Country': ['Mexico', 'India', 'China', 'El Salvador', 'Guatemala'],
    'Criminality Rate': [5, 3, 2, 6, 4]
}
df = pd.DataFrame(data)

# Function to plot immigrant population over time
def plot_population_over_time(df):
    plt.figure(figsize=(10, 6))
    sns.lineplot(data=df, x='Year', y='Population', marker='o')
    plt.title('Estimated Immigrant Population Over Time')
    plt.xlabel('Year')
    plt.ylabel('Population Estimate')
    plt.show()

# Function to plot criminality rates by country
def plot_criminality_by_country(df):
    plt.figure(figsize=(12, 6))
    sns.barplot(data=df, x='Country', y='Criminality Rate')
    plt.title('Criminality Rates by Country of Origin')
    plt.xlabel('Country')
    plt.ylabel('Criminality Rate (%)')
    plt.xticks(rotation=45)
    plt.show()

# Run plots if executing as a standalone script
if __name__ == "__main__":
    plot_population_over_time(df)
    plot_criminality_by_country(df)

# Streamlit app for interactive dashboard
st.title("Economic Impact of Illegal & Undocumented Immigrants in the US")
st.write("A dashboard to explore immigration data and its economic impact.")

# Display data in Streamlit
st.dataframe(df)

# Interactive line chart in Streamlit
if 'Population' in df.columns:
    st.line_chart(df.set_index('Year')['Population'])
