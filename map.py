import pandas as pd 
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import datetime as dt

# Read the initial CSV file
file_name = 'sensor_data.csv'

def update_plot(frame):
    # Read the CSV file again in case new data is added
    data = pd.read_csv(file_name, parse_dates=['timestamp'])
    
    # Clear the current plot to redraw
    plt.cla()
    
    # Plot temperature and humidity
    plt.subplot(2, 1, 1)  # 2 rows, 1 column, first plot
    plt.plot(data['timestamp'], data['temperature'],  color='red')
    plt.plot(data['timestamp'], data['humidity'],  color='blue')
    plt.xlabel('Timestamp')
    plt.ylabel('Value')
    plt.xticks(rotation=45)
    plt.legend(loc='upper left')
    
    # Plot MQ-4 and MQ-3 values
    plt.subplot(2, 1, 2)  # 2 rows, 1 column, second plot
    plt.plot(data['timestamp'], data['mq4'],  color='green')
    plt.plot(data['timestamp'], data['mq3'],  color='purple')
    plt.xlabel('Timestamp')
    plt.ylabel('Sensor Value')
    plt.xticks(rotation=45)
    plt.legend(loc='upper left')

    plt.tight_layout()

# Set up the plot figure
plt.figure(figsize=(10, 6))

# Use FuncAnimation to update the plot every second
ani = FuncAnimation(plt.gcf(), update_plot, interval=1000)

# Show the plot
plt.show()
