# Assuming you have already established a connection to your SQLite database
import sqlite3
import folium
import streamlit as st
import streamlit as st
import folium
from streamlit_folium import folium_static
import geopandas as gpd
import sqlite3
import pandas as pd


# Fetch the transaction amount from your SQLite database based on the state's NAME_1
def get_transaction_amount(state_name):
    conn = sqlite3.connect('your_database_name.db')
    cursor = conn.cursor()
    cursor.execute("SELECT Transaction_amount FROM agg_transc WHERE State=?", (state_name,))
    result = cursor.fetchone()
    conn.close()
    return result[0] if result else None

# ...
# In your tooltip section:
choropleth.geojson.add_child(
    folium.features.GeoJsonTooltip(['NAME_1', 'ID_1', 'Transaction_amount'], labels=False,
                                   aliases=['State', 'ID', 'Transaction Amount'],
                                   sticky=True,
                                   lines=True,
                                   style="font-weight: bold;",
                                   localize=True,
                                   ).add_to(m))
