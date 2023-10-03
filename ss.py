import streamlit as st
import folium
from streamlit_folium import folium_static
import geopandas as gpd
import sqlite3
import pandas as pd

def tw(desired_year,desired_quarter):
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
        feature['properties']['count']='count:'+str(df.loc[feature['properties']['NAME_1'], 'Transaction_count'].sum() if statename in list(df.index) else 0)
    
    
    choropleth.geojson.add_child(
        folium.features.GeoJsonTooltip(['NAME_1','count'], labels=False)
        )
    # Display the map
    folium_static(m, width=700, height=450)
    return df 
# Assuming you have already established a connection to your SQLite databasẻ̉






# Example usage of the map function in Streamlit
if __name__ == "__main__":
    st.title("Interactive Choropleth Map Example")
    tw(desired_year=2022, desired_quarter='2')


