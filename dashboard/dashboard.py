# Import Library
import streamlit as st
import pandas as pd
import plotly.express as px

# LOAD DATA
@st.cache_resource
def load_data():
    data = pd.read_csv("../data/hour.csv")
    return data

data = load_data()


# TITLE DASHBOARD
# ==============================
# Set page title
st.title("Bike Sharing Dashboard")

# SIDEBAR
st.sidebar.title("Information:")

st.sidebar.markdown("**• Nama: Naufal Iffa Maulana Ramadhan**")

st.sidebar.title("Dataset Bike Share")
# Show the dataset
if st.sidebar.checkbox("Show Dataset"):
    st.subheader("Raw Data")
    st.write(data)

# Display summary statistics
if st.sidebar.checkbox("Show Summary Statistics"):
    st.subheader("Summary Statistics")
    st.write(data.describe())

# VISUALIZATION

st.subheader("Data Visualization")

st.subheader("Total Rental Bikes Over Time")
fig = px.line(data, x='dteday', y='cnt', title='Total Rental Bikes Over Time')
st.plotly_chart(fig, use_container_width=True)

st.subheader("Weather Distribution")
fig_weather = px.histogram(data, x='weathersit', title='Weather Distribution')
st.plotly_chart(fig_weather, use_container_width=True)

st.subheader("Humidity Distribution")
fig_humidity = px.histogram(data, x='hum', title='Humidity Distribution')
st.plotly_chart(fig_humidity, use_container_width=True)

st.subheader("Rental Bikes by Month")
avg_by_month = data.groupby('mnth')['cnt'].mean().reset_index()
fig_avg_by_month = px.bar(avg_by_month, x='mnth', y='cnt', title='Average Rental Bikes by Month')
st.plotly_chart(fig_avg_by_month, use_container_width=True)



st.sidebar.markdown('**Weather:**')
st.sidebar.markdown('1: Clear, Few clouds, Partly cloudy, Partly cloudy')
st.sidebar.markdown('2: Mist + Cloudy, Mist + Broken clouds, Mist + Few clouds, Mist')
st.sidebar.markdown('3: Light Snow, Light Rain + Thunderstorm + Scattered clouds, Light Rain + Scattered clouds')
st.sidebar.markdown('4: Heavy Rain + Ice Pallets + Thunderstorm + Mist, Snow + Fog')





