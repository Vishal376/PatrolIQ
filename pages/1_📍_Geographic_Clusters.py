import streamlit as st
import pandas as pd
import folium
from streamlit_folium import st_folium

# st.title("📍 Geographic Crime Clusters (KMeans / DBSCAN / HC)")
st.title("📍 Geographic Crime Clusters ")

df = pd.read_csv("final_crime_clusters2.csv")

# cluster_type = st.selectbox("Select Cluster Type", 
#                             ['KMeans_Cluster','DBSCAN_Cluster','HC_Cluster'])

m = folium.Map(location=[df['Latitude'].mean(), df['Longitude'].mean()], zoom_start=11)

for _, row in df.iterrows():
    folium.CircleMarker(
        location=[row['Latitude'], row['Longitude']],
        radius=2,
        # color=f"#{hex(1000000 + int(row[cluster_type]*35000))[2:]:>06}",
         color=f"#{hex(1000000 + int(row['DBSCAN_Cluster']*35000))[2:]:>06}",
        fill=True
    ).add_to(m)

st_folium(m, width=900)
