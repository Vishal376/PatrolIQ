import streamlit as st
import pandas as pd

st.set_page_config(page_title="Chicago Crime Analysis", layout="wide")

st.title("🚔 Chicago Crime Analysis Dashboard")
st.markdown("""
This multipage dashboard shows:

### ✅ Geographic Crime Hotspots  
### ✅ DBSCAN, KMeans, Hierarchical Clustering  
### ✅ Crime Dendrogram  
### ✅ Temporal Crime Patterns  
### ✅ Top Influential Features (PCA)  
### ✅ t-SNE Crime Type Separation  

Select a page from the left sidebar to begin.
""")

df = pd.read_csv("final_crime_clusters2.csv")
st.dataframe(df.head())
