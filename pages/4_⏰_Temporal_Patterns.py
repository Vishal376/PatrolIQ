import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("⏰ Temporal Crime Patterns & Profiles")

df = pd.read_csv("final_crime_clusters2.csv")

fig, ax = plt.subplots(1, 3, figsize=(18,5))

df['hour'].value_counts().sort_index().plot(ax=ax[0], title="Crimes by Hour 0-12am ")
df['month'].value_counts().sort_index().plot(kind='bar', ax=ax[1], title="Crimes by Month")
df['day_name'].value_counts().plot(kind='bar', ax=ax[2], title="Crimes by Day 0-Monday")

st.pyplot(fig)

# Temporal clusters
st.subheader("Temporal Clusters (4 patterns) hour(0=12 a.m) day_name(0=Monday)")
st.dataframe(df[['hour','month','day_name','Temporal_cluster']].head())

