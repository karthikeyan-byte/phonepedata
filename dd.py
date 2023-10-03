import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import json
import os
import plotly.express as px
import streamlit as st
import plotly.graph_objects as go
import sqlite3
from streamlit_folium import folium_static
import folium

# Path for aggregated transaction
path1 = "/Users/karthikeyank/Documents/phonepe/pulse/data/aggregated/transaction/country/india/state/"
agg_trans_list = os.listdir(path1)

columns1 = {'State': [], 'Year': [], 'Quarter': [], 'Transaction_type': [], 'Transaction_count': [],
            'Transaction_amount': []}

for state in agg_trans_list:
    cur_state = path1 + state + "/"
    agg_year_list = os.listdir(cur_state)

    for year in agg_year_list:
        cur_year = cur_state + year + "/"
        agg_file_list = os.listdir(cur_year)

        for file in agg_file_list:
            cur_file = cur_year + file
            data = open(cur_file, 'r')
            A = json.load(data)

            for i in A['data']['transactionData']:
                name = i['name']
                count = i['paymentInstruments'][0]['count']
                amount = i['paymentInstruments'][0]['amount']
                columns1['Transaction_type'].append(name)
                columns1['Transaction_count'].append(count)
                columns1['Transaction_amount'].append(amount)
                columns1['State'].append(state)
                columns1['Year'].append(year)
                columns1['Quarter'].append(int(file.strip('.json')))

df_agg_trans = pd.DataFrame(columns1)
df_agg_trans.to_csv("agg_trans.csv")

def map():
    india_geojson = "/Users/karthikeyank/Documents/phonepe/archive (4)/district/india_district.geojson"
    map = px.choropleth_mapbox(df_agg_trans, geojson=india_geojson, locations=df_agg_trans.index, color="Transaction_type")
    return st.plotly_chart(map)

def tw(desired_year, desired_quarter):
    conn = sqlite3.connect("phonepe.db")
    desired_year = desired_year
    desired_quarter = desired_quarter
    query = "SELECT * FROM agg_transc WHERE year = ? AND Quarter = ?"
    df = pd.read_sql_query(query, conn, params=(desired_year, desired_quarter))
    st.plotly_chart(px.bar(df, x="Transaction_type", y="Transaction_amount", hover_name="Quarter", color="State"))
    st.dataframe(df)

    return df

def one():
    conn = sqlite3.connect("phonepe.db")
    query = "SELECT * FROM agg_trans"
    df = pd.read_sql_query(query, conn)
    return df

def kk():
    fig = px.bar(df_agg_trans, x="State", y="Transaction_amount", color="Transaction_type", hover_name="Quarter")
    fig1 = px.pie(df_agg_trans, values="Transaction_count", names="Transaction_type")
    return st.plotly_chart(fig), st.plotly_chart(fig1)

def main():
    st.title("phonepe pulse")
    options = st.sidebar.selectbox("Select an option", ('Transactions', 'Users'))

    years = ['2018', '2019', '2020', '2021', '2022', '2023']
    quarters = ['Q1', 'Q2', 'Q3', 'Q4']

    selected_year = st.sidebar.selectbox("Select a Year", years)
    selected_quarter = st.sidebar.selectbox("Select a Quarter", quarters)

    if options == 'Transactions':
        if selected_year == '2023' and (selected_quarter == 'Q3' or selected_quarter == 'Q4'):
            st.write("DATA NOT AVAILABLE")
        else:
            year = int(selected_year)
            quarter = int(selected_quarter[1])
            tw(desired_year=year, desired_quarter=quarter)
            

    elif options == 'Users':
        pass  # Add logic for Users option here

if __name__ == "__main__":
    main()
