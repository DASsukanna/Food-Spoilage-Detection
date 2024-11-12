# Food Spoilage Detection System

## Table of Contents
- [Introduction](#introduction)
- [Project Overview](#project-overview)
- [Hardware Requirements](#hardware-requirements)
- [Software Requirements](#software-requirements)
- [Project Setup](#project-setup)
- [How It Works](#how-it-works)
- [Data Visualization](#data-visualization)
- [Future Enhancements](#future-enhancements)
- [Conclusion](#conclusion)

## Introduction
Spoilage of food is a common issue that leads to waste and potential health hazards. This IoT-based project aims to detect the conditions that accelerate food spoilage by monitoring emitted gases and environmental factors. The system alerts users by saving real-time data to a CSV file and provides a web interface for data visualization.

## Project Overview
This Food Spoilage Detection System uses several sensors to monitor conditions that indicate food spoilage. The main components include:
- **MQ3 Sensor**: Detects alcohol levels in the environment.
- **MQ4 Sensor**: Detects methane gas.
- **DHT11 Sensor**: Measures temperature and humidity.
- **ESP32**: Wi-Fi module used for transmitting data to the server.

The system saves sensor readings to a CSV file and visualizes them through a web application created using Streamlit, displaying charts and data tables for better interpretation.

## Hardware Requirements
- **ESP32**: Wi-Fi module for data transmission.
- **MQ3 Gas Sensor**: Alcohol and ethanol detection.
- **MQ4 Gas Sensor**: Methane detection.
- **DHT11 Sensor**: Measures temperature and humidity.
- **Connecting Wires**: For circuit connections.
- **Breadboard**: For assembling components.
- **Power Supply**: For powering the circuit.

## Software Requirements
- **Arduino IDE**: For programming the ESP32 and setting up sensors.
- **Python**: For creating the API, storing data, and generating the web interface.
- **Flask**: To create a local server for saving data to CSV.
- **Streamlit**: For creating an interactive web app to display the sensor data.
- **Pandas**: For data processing and handling CSV files.
- **Plotly**: For advanced data visualization in the Streamlit app.

## Project Setup

### Sensor and Circuit Setup
1. Connect the MQ3, MQ4, and DHT11 sensors to the ESP32 module.
2. Use a breadboard for easy assembly.
3. Power the sensors and ESP32 with an appropriate power source.

### ESP32 Programming
1. Install and configure the Arduino IDE.
2. Use the Arduino IDE to program the ESP32 to read data from the sensors and send it via HTTP requests.

### Python API for Data Storage
1. Create an API using Python (Flask) to receive sensor data.
2. Save the incoming data to a CSV file.

### Data Visualization Web Interface (`ui.py`)
1. Use `ui.py` to set up the web interface using Streamlit.
2. Load the CSV data using Pandas.
3. Display data tables and real-time visualizations using Plotly charts for temperature, humidity, and gas concentration levels.

## How It Works

### Data Collection
1. The MQ3, MQ4, and DHT11 sensors read temperature, humidity, and gas levels.
2. The ESP32 sends this data to a Python API, which stores it in a CSV file for further analysis.

### Data Processing
- The CSV file records each sensor reading with a timestamp, allowing users to monitor changes over time.

### Visualization
- The `ui.py` Streamlit application reads data from the CSV file.
- Streamlit, using Pandas and Plotly, displays real-time trends in charts, enabling users to monitor temperature, humidity, and gas emissions.

## Data Visualization
The Streamlit app displays sensor data with Plotly line charts, allowing users to track:
- **Temperature**: Recorded by the DHT11 sensor.
- **Humidity**: Also recorded by the DHT11 sensor.
- **Gas Concentration**:
  - **Alcohol/Ethanol (MQ3)**: Indicates spoilage processes in some foods.
  - **Methane/Natural Gas (MQ4)**: Detected as a byproduct of spoilage.

Each parameter updates periodically, providing a clear view of environmental changes in the storage area.

## Future Enhancements
- **Notification System**: Integrate a notification system to alert users when sensor values exceed safe limits.
- **Machine Learning Analysis**: Predict spoilage trends by analyzing historical data.
- **Mobile App Integration**: Extend functionality to a mobile app for easier access.

## Conclusion
The Food Spoilage Detection System provides an effective solution for monitoring environmental factors contributing to food spoilage. By combining IoT sensors with real-time data visualization, it offers valuable insights into food safety, aiding in the prevention of waste and promoting better storage practices.

## Workflow Diagram

```mermaid
graph TD
    A[MQ3, MQ4, DHT11 Sensors] --> B[ESP32 Module]
    B -->|HTTP Request| C[Python Flask API]
    C -->|Save Data| D[CSV File]
    D -->|Load Data| E[Streamlit Web App]
    E --> F[Pandas & Plotly for Visualization]
    F --> G[User Monitors Conditions on Web Interface]
