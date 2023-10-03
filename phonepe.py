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
#create dataframe
columns1 = {'State': [], 'Year': [], 'Quarter': [], 'Transaction_type': [], 'Transaction_count': [],
            'Transaction_amount': []}
#extract data
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
#/////////////////////////////////////////////////////////////////////////////////////////////////////////////////
#path for aggregated user
path2 = "/Users/karthikeyank/Documents/phonepe/pulse/data/aggregated/user/country/india/state/"

agg_user_list = os.listdir(path2)
#create dataframe
columns2 = {'State': [], 'Year': [], 'Quarter': [], 'Brands': [], 'Count': [],
            'Percentage': []}
#extract data
for state in agg_user_list:
    cur_state = path2 + state + "/"
    agg_year_list = os.listdir(cur_state)
    
    for year in agg_year_list:
        cur_year = cur_state + year + "/"
        agg_file_list = os.listdir(cur_year)

        for file in agg_file_list:
            cur_file = cur_year + file
            data = open(cur_file, 'r')
            B = json.load(data)
            try:
                for i in B["data"]["usersByDevice"]:
                    brand_name = i["brand"]
                    counts = i["count"]
                    percents = i["percentage"]
                    columns2["Brands"].append(brand_name)
                    columns2["Count"].append(counts)
                    columns2["Percentage"].append(percents)
                    columns2["State"].append(state)
                    columns2["Year"].append(year)
                    columns2["Quarter"].append(int(file.strip('.json')))
            except:
                pass
df_agg_user = pd.DataFrame(columns2)
df_agg_user.to_csv("agg_user.csv", index=False)
#/////////////////////////////////////////////////////////////////////////////////////////////////////////////////
#path3 for map transaction
path3 = "/Users/karthikeyank/Documents/phonepe/pulse/data/map/transaction/hover/country/india/state/"

map_trans_list = os.listdir(path3)
#create dataframe
columns3 = {'State': [], 'Year': [], 'Quarter': [], 'District': [], 'Count': [],
            'Amount': []}
#extract data
for state in map_trans_list:
    cur_state = path3 + state + "/"
    map_year_list = os.listdir(cur_state)
    
    for year in map_year_list:
        cur_year = cur_state + year + "/"
        map_file_list = os.listdir(cur_year)
        
        for file in map_file_list:
            cur_file = cur_year + file
            data = open(cur_file, 'r')
            C = json.load(data)
            
            for i in C["data"]["hoverDataList"]:
                district = i["name"]
                count = i["metric"][0]["count"]
                amount = i["metric"][0]["amount"]
                columns3["District"].append(district)
                columns3["Count"].append(count)
                columns3["Amount"].append(amount)
                columns3['State'].append(state)
                columns3['Year'].append(year)
                columns3['Quarter'].append(int(file.strip('.json')))
                
df_map_trans = pd.DataFrame(columns3)
df_map_trans.to_csv("map_trans.csv", index=False)
#/////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# Data frame of map user
path4 = "/Users/karthikeyank/Documents/phonepe/pulse/data/map/user/hover/country/india/state/"

map_user_list = os.listdir(path4)
#create dataframe
columns4 = {"State": [], "Year": [], "Quarter": [], "District": [],
            "RegisteredUser": [], "AppOpens": []}
#extract data
for state in map_user_list:
    cur_state = path4 + state + "/"
    map_year_list = os.listdir(cur_state)
    
    for year in map_year_list:
        cur_year = cur_state + year + "/"
        map_file_list = os.listdir(cur_year)
        
        for file in map_file_list:
            cur_file = cur_year + file
            data = open(cur_file, 'r')
            D = json.load(data)
            
            for i in D["data"]["hoverData"].items():
                district = i[0]
                registereduser = i[1]["registeredUsers"]
                appOpens = i[1]['appOpens']
                columns4["District"].append(district)
                columns4["RegisteredUser"].append(registereduser)
                columns4["AppOpens"].append(appOpens)
                columns4['State'].append(state)
                columns4['Year'].append(year)
                columns4['Quarter'].append(int(file.strip('.json')))
                
df_map_user = pd.DataFrame(columns4)
df_map_user.to_csv("map_user.csv", index=False)
#/////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# Data frame of top transactions
path5 = "/Users/karthikeyank/Documents/phonepe/pulse/data/top/transaction/country/india/state/"
top_trans_list = os.listdir(path5)
#create dataframe
columns5 = {'State': [], 'Year': [], 'Quarter': [], 'Pincode': [], 'Transaction_count': [],
            'Transaction_amount': []}
#extract data
for state in top_trans_list:
    cur_state = path5 + state + "/"
    top_year_list = os.listdir(cur_state)
    
    for year in top_year_list:
        cur_year = cur_state + year + "/"
        top_file_list = os.listdir(cur_year)
        
        for file in top_file_list:
            cur_file = cur_year + file
            data = open(cur_file, 'r')
            E = json.load(data)
            
            for i in E['data']['pincodes']:
                name = i['entityName']
                count = i['metric']['count']
                amount = i['metric']['amount']
                columns5['Pincode'].append(name)
                columns5['Transaction_count'].append(count)
                columns5['Transaction_amount'].append(amount)
                columns5['State'].append(state)
                columns5['Year'].append(year)
                columns5['Quarter'].append(int(file.strip('.json')))
df_top_trans = pd.DataFrame(columns5)
df_top_trans.to_csv("top_trans.csv", index=False)
#/////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# Data frame of top users
path6 = "/Users/karthikeyank/Documents/phonepe/pulse/data/top/user/country/india/state/"
top_user_list = os.listdir(path6)
columns6 = {'State': [], 'Year': [], 'Quarter': [], 'Pincode': [],
            'RegisteredUsers': []}
#extract data
for state in top_user_list:
    cur_state = path6 + state + "/"
    top_year_list = os.listdir(cur_state)
    
    for year in top_year_list:
        cur_year = cur_state + year + "/"
        top_file_list = os.listdir(cur_year)
        
        for file in top_file_list:
            cur_file = cur_year + file
            data = open(cur_file, 'r')
            F = json.load(data)
            
            for i in F['data']['pincodes']:
                name = i['name']
                registeredUsers = i['registeredUsers']
                columns6['Pincode'].append(name)
                columns6['RegisteredUsers'].append(registeredUsers)
                columns6['State'].append(state)
                columns6['Year'].append(year)
                columns6['Quarter'].append(int(file.strip('.json')))
df_top_user = pd.DataFrame(columns6)
df_top_user.to_csv("top_user.csv", index=False)


#////////////////////////////////////////////////////////////////////////////////////////////////////////////////
#create map in the app 
def inmap(desired_year,desired_quarter):
    conn = sqlite3.connect("phonepe.db")
    query = "SELECT * FROM agg_transc WHERE year = ? AND Quarter = ?"
    df = pd.read_sql_query(query, conn, params=(desired_year, desired_quarter))

    # Load the GeoJSON file with state boundaries
    geojson_file = '/Users/karthikeyank/Documents/phonepe/archive (8)/state/india_telengana.geojson'
    
    # Create a map centered on India
    m = folium.Map(location=[20.5937, 78.9629], zoom_start=4, scrollWheelZoom=False, tiles='CartoDB positron')

    # Add the GeoPandas GeoDataFrame to the map as a choropleth layer
    choropleth=folium.Choropleth(
        geo_data=geojson_file,
        data=df,
        columns=['State', 'Transaction_count','Transaction_amount','Transaction_type'],
        key_on='feature.properties.NAME_1',  # Specify the property name in your GeoJSON
        line_opacity=0.8,  # Set the opacity of the lines
        highlight=True,
        fill_color='YlOrRd',
        fill_opacity=0.7,
        legend_name='Transaction_type',
        name='Transaction_type',
    
    ).add_to(m)
    choropleth.geojson.add_to(m)
    
    df=df.set_index('State')
    statename='Tamil Nadu'
   
    
    for feature in choropleth.geojson.data['features']:
        statename=feature['properties']['NAME_1']
        feature['properties']['count']='amount:'+str(df.loc[feature['properties']['NAME_1'], 'Transaction_amount'].sum() if statename in list(df.index) else 0)
    
    
    choropleth.geojson.add_child(
        folium.features.GeoJsonTooltip(['NAME_1','count'], labels=False)
        )
    # Display the map
    folium_static(m, width=700, height=450)
    return df 
#**********************************************************************************************************************************
#****************************************************************************************************************************

#barchart and sunburst unction for transcation
def tw(desired_year, desired_quarter):
    conn = sqlite3.connect("phonepe.db")
    desired_year = desired_year
    desired_quarter = desired_quarter
    query = "SELECT * FROM agg_transc WHERE year = ? AND Quarter = ?"
    df = pd.read_sql_query(query, conn, params=(desired_year, desired_quarter))
    st.plotly_chart(px.bar(df, x="State", y="Transaction_amount", hover_name="Quarter", color="Transaction_type" ))
    #st.dataframe(df)
    fig=px.sunburst(df,path=["Transaction_type","State","Transaction_count"],values='Transaction_amount')
    fig1=px.scatter_3d(df,x='State',y='Transaction_count',color='Transaction_type',z='Transaction_amount')
    
    st.write(fig,fig1)

    return df
#////////////////////////////////////////////////////////////////////////////////////////////////////////////////
#bar chart and sunburst for user
def three(desired_year, desired_quarter):
    conn = sqlite3.connect("phonepe.db")
    desired_year = desired_year
    desired_quarter = desired_quarter
    query =" SELECT * FROM agg_user WHERE year = ? AND Quarter = ?"
    df = pd.read_sql_query(query, conn, params=(desired_year, desired_quarter))
    #st.dataframe(df)
    st.plotly_chart(px.bar(df, x="State", y="Count", hover_name="Quarter", color="Brands"))
    fig=px.sunburst(df,path=["Brands","State","Count"],values='Percentage')
    fig1=px.scatter_3d(df,x='State',y='Count',color='Brands',z='Percentage')
    
    st.write(fig,fig1)
    return df
#////////////////////////////////////////////////////////////////////////////////////////////////////////////////
#for users 
#bar chart and sunburst for transaction
def ii():
    conn=sqlite3.connect("phonepe.db")
    query="SELECT State,Year,Quarter,Pincode,Transaction_count,Transaction_amount FROM top_trans GROUP BY State ORDER BY Transaction_amount DESC LIMIT 10" 
    df=pd.read_sql_query(query,conn)
    st.subheader("Top 10 Transactions States in India")
    st.plotly_chart(px.bar(df, x="State", y="Transaction_amount", hover_name="Quarter",color="Transaction_count"))
    fig=px.sunburst(df,path=["State","Transaction_count"],values='Transaction_amount')
    st.write(fig)
    return df
#bar chart and sunburst for user
def ll():
    conn=sqlite3.connect("phonepe.db")
    query="SELECT Year,Quarter,District,Count,Amount FROM map_trans GROUP BY District ORDER BY Amount DESC LIMIT 10" 
    df=pd.read_sql_query(query,conn)
    st.subheader("Top 10 Transactions Districts in India")
    st.plotly_chart(px.bar(df, x="District", y="Amount", hover_name="Quarter",color="Count"))
    fig=px.sunburst(df,path=["District","Count"],values='Amount')
    st.write(fig)
    



def one():
    conn = sqlite3.connect("phonepe.db")
    query = "SELECT * FROM agg_trans"
    df = pd.read_sql_query(query, conn)
    return df

def kk():
    fig = px.bar(df_agg_trans, x="State", y="Transaction_amount", color="Transaction_type", hover_name="Quarter")
    fig1 = px.pie(df_agg_trans, values="Transaction_count", names="Transaction_type")
    return st.plotly_chart(fig), st.plotly_chart(fig1)
#streamlit app
def main():

    options = st.sidebar.selectbox("Select an option", ('HOME','Transactions', 'Users'))
    
    if options == 'HOME':
        st.title("phonepe pulse")
        ii()
        ll()
    
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
            inmap(desired_year=year, desired_quarter=quarter)
            
            
            

    elif options == 'Users':
        if selected_year=='2023' and (selected_quarter=='Q1','Q2' or selected_quarter=='Q2'):
            st.write("DATA NOT AVAILABLE")
        if selected_year == '2022' and (selected_quarter == 'Q2' or selected_quarter == 'Q4' or selected_quarter == 'Q3'):
            st.write("DATA NOT AVAILABLE")
        else:
            year = int(selected_year)
            quarter = int(selected_quarter[1])
            three(desired_year=year, desired_quarter=quarter)

if __name__ == "__main__":
    main()
