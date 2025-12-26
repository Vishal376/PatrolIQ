import streamlit as st
import pandas as pd
from scipy.cluster.hierarchy import dendrogram, linkage
import matplotlib.pyplot as plt

st.title("🌳 Hierarchical Crime Zone Dendrogram")

df = pd.read_csv("final_crime_clusters2.csv", nrows=2000)

# Features
features = df[['Latitude','Longitude','Crime_Severity_Score']]

# Sample for speed
sample_df = features.sample(50).reset_index(drop=True)

# Leaf labels with Latitude + Longitude
labels = [
    f"{round(row['Latitude'], 4)}, {round(row['Longitude'], 4)}"
    for _, row in sample_df.iterrows()
]

# Linkage
Z = linkage(sample_df, method='ward')

# Plot
fig, ax = plt.subplots(figsize=(20, 50))
dendrogram(Z, labels=labels, leaf_rotation=90)
plt.xlabel("(Latitude,Longitude)",fontsize=22)
plt.ylabel("DIG (Cluster Distance)",fontsize=22)   # Left side label
plt.title("Crime Dendrogram",fontsize=22)

st.pyplot(fig)

st.markdown(
    "<h3 style='text-align: center;'>(Every Color Denotes Each Cluster Branch)</h3>",
    unsafe_allow_html=True
)