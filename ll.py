import pandas as pd
import streamlit as st
import plotly.express as px

# Load your aggregated transaction data
df_agg_trans = pd.read_csv("agg_trans.csv")

# Create a function to filter data by quarter
def filter_data(df, year, quarter):
    filtered_df = df[(df['Year'] == int(year)) & (df['Quarter'] == int(quarter))]
    return filtered_df

# Streamlit UI
def ma():
    st.title("PhonePe Pulse")
    
    # Sidebar options
    options = st.sidebar.selectbox(
        "Select an option",
        ('Transactions', 'Users',)
    )
    
    year = st.sidebar.selectbox(
        "Select an Year",
        ('2018', '2019', '2020', '2021', '2022', '2023')
    )
    
    quarter = st.sidebar.selectbox(
        "Select a Quarter",
        ('1', '2', '3', '4')
    )
    
    # Filter data based on user selection
    filtered_df = filter_data(df_agg_trans, year, quarter)
    
    if options == 'Transactions':
        st.write(f"Transaction Data for Q{quarter} {year}:")
        fig = px.bar(filtered_df, x="State", y="Transaction_amount", color="Transaction_type", hover_name="Quarter")
        st.plotly_chart(fig)
    
    if options == 'Users':
        st.write(f"User Data for Q{quarter} {year}:")
        # Add your code for user data visualization here (if available)

# Run the Streamlit app
if __name__ == '__main__':
    ma()



