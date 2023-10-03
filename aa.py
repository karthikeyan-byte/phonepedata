import streamlit as st
import geopandas as gpd
import pydeck as pdk

def main():
    st.title("Interactive 3D Map Example")

    # Load GeoJSON data (replace with your GeoJSON file)
    geojson_file = '/Users/karthikeyank/Documents/phonepe/archive (8)/state/india_telengana.geojson'
    gdf = gpd.read_file(geojson_file)

    # Create a pydeck layer for the 3D map
    layer = pdk.Layer(
        "GeoJsonLayer",
        data=gdf,
        get_fill_color=[0, 0, 255, 100],  # Blue color with transparency
        auto_highlight=True,
        extruded=True,  # Enable extrusion for 3D effect
        get_elevation="population",  # Elevation based on a column in the GeoDataFrame
        elevation_scale=50,  # Adjust the elevation scale
        pickable=True,
    )

    # Create a pydeck view
    view_state = pdk.ViewState(
        latitude=20.5937,
        longitude=78.9629,
        zoom=4,
        pitch=45,  # Adjust the pitch for 3D view
        bearing=0,  # Adjust the bearing for orientation
    )

    # Create a pydeck map
    r = pdk.Deck(
        map_style="mapbox://styles/mapbox/light-v9",
        layers=[layer],
        initial_view_state=view_state,
    )

    # Display the 3D map using Streamlit
    st.pydeck_chart(r)

if __name__ == "__main__":
    main()
