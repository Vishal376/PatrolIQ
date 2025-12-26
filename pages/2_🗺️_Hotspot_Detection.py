import streamlit as st
import pandas as pd
import folium
from streamlit_folium import st_folium

# st.title("🔥 Crime Hotspot Detection (DBSCAN)")
st.title("🔥 Crime Hotspot Detection")

df = pd.read_csv("final_crime_clusters2.csv")

hot = df[df['DBSCAN_Cluster'] != -1]   # noise removed
noise = df[df['DBSCAN_Cluster'] == -1]

m = folium.Map(location=[df['Latitude'].mean(), df['Longitude'].mean()], zoom_start=11)

# High density = hotspots
for _, row in hot.iterrows():
    folium.CircleMarker(
        [row['Latitude'], row['Longitude']],
        radius=3,
        color="red",
        fill=True
    ).add_to(m)

# Grey = noise/outliers
for _, row in noise.iterrows():
    folium.CircleMarker(
        [row['Latitude'], row['Longitude']],
        radius=2,
        color="gray",
        fill=True
    ).add_to(m)

st_folium(m, width=900)
