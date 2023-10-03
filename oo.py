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

# Replace "agg_trans" with the name of your SQLite table
query = "SELECT * FROM agg_transc"

# Use the engine to execute the query and fetch data into a DataFrame
df = pd.read_sql_query(query, engine)

# Create a Plotly scatter plot
st.plotly_chart(px.scatter(df, x='Transaction_type', y='Transaction_amount', title='Plotly Scatter Plot from SQLite Data',hover_name='Quarter'
                           ,animation_group='Year',color='Transaction_type',animation_frame='Quarter' ))

# Create an Altair chart
st.write("Altair Chart:")
c = alt.Chart(df).mark_circle().encode(
    x='Transaction_type',
    y='Transaction_amount',
    tooltip=['Transaction_type', 'Transaction_amount']
)
st.altair_chart(c)

# Optionally, display the DataFrame
st.write("Data from SQLite Table:")
st.write(df)
