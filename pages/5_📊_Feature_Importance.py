import streamlit as st
import pandas as pd
import pydeck as pdk

st.title("📍 Crime Severity Map with Clickable Points")

# Load data
df = pd.read_csv("final_crime_clusters2.csv")

# Rename for pydeck
df = df.rename(columns={'Latitude': 'lat', 'Longitude': 'lon'})

# Dropdown
severity_list = sorted(df["Crime_Severity_Score"].unique())
selected_severity = st.selectbox("Select Crime Severity Score", severity_list)

# Filter
filtered_df = df[df["Crime_Severity_Score"] == selected_severity]

st.write("Filtered Points:", len(filtered_df))

# 🔥 Pydeck Layer for clickable markers
layer = pdk.Layer(
    "ScatterplotLayer",
    data=filtered_df,
    get_position='[lon, lat]',
    get_radius=40,
    pickable=True,
    get_color=[255, 0, 0],
)

# 🔥 Tooltip — shows on hover/click
tooltip = {
    "html": """
    <b>Crime Details</b><br>
    Latitude: {lat}<br>
    Longitude: {lon}<br>
    Hour: {hour}<br>
    Crime Type Code: {Crime_Type_Code}
    """,
    "style": {"backgroundColor": "steelblue", "color": "white"}
}

# Set view
view_state = pdk.ViewState(
    latitude=filtered_df["lat"].mean(),
    longitude=filtered_df["lon"].mean(),
    zoom=10,
    pitch=45,
)

# Render map
st.pydeck_chart(
    pdk.Deck(
        layers=[layer],
        initial_view_state=view_state,
        tooltip=tooltip,
    )
)

# Show table
st.write("📄 Selected Crime Data")
st.dataframe(filtered_df[['lat', 'lon', 'hour', 'Crime_Type_Code']])
