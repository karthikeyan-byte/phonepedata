import pandas as pd
import plotly.express as px
import altair as alt
from sqlalchemy import create_engine
import streamlit as st

# Title for your Streamlit app
st.title("Data Visualization with Streamlit")

# Replace "phonepe.db" with the path to your SQLite database file
database_url = 'sqlite:///phonepe.db'

# Connect to the SQLite database
engine = create_engine(database_url)


desired_year = 2018

# Define the quarter you want to retrieve (e.g., 1)
desired_quarter = 1


# Replace "agg_trans" with the name of your SQLite table
query = "SELECT * FROM agg_transc WHERE year = ? AND Quarter = ?", (desired_year, desired_quarter)

# Use the engine to execute the query and fetch data into a DataFrame
df = pd.read_sql_query(query, engine)

# Create a Plotly scatter plot
plotly_chart = px.scatter(df, x='Transaction_type', y='Transaction_amount', title='Plotly Scatter Plot from SQLite Data',hover_name='Quarter' )

# Create an Altair chart
altair_chart = alt.Chart(df).mark_circle().encode(
    x='Transaction_type',
    y='Transaction_amount',
    tooltip=['Transaction_type', 'Transaction_amount']
)

# Create a Streamlit layout to display both charts side by side
col1, col2 = st.beta_columns(2)
with col1:
    st.plotly_chart(plotly_chart)

with col2:
    st.write("Altair Chart:")
    st.altair_chart(altair_chart)

# Optionally, display the DataFrame
st.write("Data from SQLite Table:")
st.write(df)
