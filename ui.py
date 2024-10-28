# app.py

import streamlit as st
import requests
import pandas as pd
import plotly.express as px
from datetime import datetime
import time

# Streamlit dashboard setup
st.title("Real-time Sensor Data Dashboard")
st.sidebar.header("API Server Configuration")

# User input for API server host IP and port
host_ip = st.sidebar.text_input("API Server Host IP", value="192.168.60.30")
host_port = st.sidebar.text_input("API Server Port", value="5000")
api_url = f"http://{host_ip}:{host_port}/api"

# Placeholder for the live data
data_placeholder = st.empty()

# Function to fetch data from the API
def fetch_data(api_url):
    try:
        response = requests.get(api_url)
        if response.status_code == 200:
            return response.json()['data']
        else:
            st.error("Error fetching data from API")
            return []
    except requests.exceptions.RequestException as e:
        st.error(f"An error occurred: {e}")
        return []

# Function to display the data as real-time charts
def display_realtime_data(data):
    if data:
        df = pd.DataFrame(data)
        df['timestamp'] = pd.to_datetime(df['timestamp'])
        
        # Temperature Line Chart
        fig_temp = px.line(df, x='timestamp', y='temperature', title="Temperature Over Time")
        st.plotly_chart(fig_temp, use_container_width=True)

        # Humidity Line Chart
        fig_humidity = px.line(df, x='timestamp', y='humidity', title="Humidity Over Time")
        st.plotly_chart(fig_humidity, use_container_width=True)

        # MQ4 Gas Sensor Line Chart
        fig_mq4 = px.line(df, x='timestamp', y='mq4', title="MQ4 Sensor Over Time")
        st.plotly_chart(fig_mq4, use_container_width=True)

        # MQ3 Gas Sensor Line Chart
        fig_mq3 = px.line(df, x='timestamp', y='mq3', title="MQ3 Sensor Over Time")
        st.plotly_chart(fig_mq3, use_container_width=True)
    else:
        st.write("No data available to display.")

# Initial fetch and display
data = fetch_data(api_url)
display_realtime_data(data)

# Refresh interval setup
refresh_interval = 5  # Refresh interval in seconds
last_refresh = st.empty()
data_placeholder = st.empty()
# Update loop
# Update loop
while True:
    time.sleep(refresh_interval)
    last_refresh.text(f"Last refreshed at {datetime.now().strftime('%H:%M:%S')}")
    data = fetch_data(api_url)  # Fetch updated data
    with data_placeholder:
        display_realtime_data(data)  # Pass 'data' to the function


