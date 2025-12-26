import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

st.title("🌀 t-SNE Crime Pattern Separation")

df = pd.read_csv("final_crime_clusters2.csv")

# Cluster → Time mapping
time_map = {
    0: "Morning (6 AM – 12 PM)",
    1: "Afternoon (12 PM – 6 PM)",
    2: "Evening (6 PM – 12 AM)",
    3: "Night (12 AM – 6 AM)"
}

# Replace numeric cluster with time labels
df['Time_Label'] = df['Temporal_cluster'].map(time_map)

# Create figure for Streamlit
fig, ax = plt.subplots(figsize=(10, 7))

sns.scatterplot(
    x='TSNE_1', y='TSNE_2',
    hue='Time_Label',
    data=df,
    palette='Set1',
    s=30,
    alpha=0.8,
    ax=ax
)

ax.set_title("t-SNE: Crime Type Separation by Time")
ax.set_xlabel("t-SNE Component 1")
ax.set_ylabel("t-SNE Component 2")

ax.legend(title="Crime Time Cluster", bbox_to_anchor=(1.05, 1), loc='upper left')

st.pyplot(fig)

st.write("This clearly shows clustering by:")
st.write("- Time of crime (Morning / Afternoon / Evening / Night)")
st.write("- Crime behavior patterns")
st.write("- Hidden structure in crime activities")
