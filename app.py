from flask import Flask, request, jsonify
import pandas as pd
from datetime import datetime

app = Flask(__name__)

# Data storage
data = []

@app.route('/api', methods=['POST'])
def api_post():
    try:
        # Retrieve the form data from the request
        temperature = request.form.get('temperature')
        humidity = request.form.get('humidity')
        mq4 = request.form.get('mq4')
        mq3 = request.form.get('mq3')

        # Check if required data was provided
        if temperature is None or humidity is None or mq4 is None or mq3 is None:
            return jsonify({'error': 'Missing data: temperature, humidity, mq4, or mq3'}), 400

        # Append data with a timestamp
        data.append({
            'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            'temperature': temperature,
            'humidity': humidity,
            'mq4': mq4,
            'mq3': mq3
        })

        # Convert the list to a DataFrame and save to CSV (append mode)
        df = pd.DataFrame(data)
        df.to_csv('sensor_data.csv', index=False)

        return jsonify({'message': 'Data received successfully'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api', methods=['GET'])
def api_get():
    try:
        # Load data from the CSV file
        df = pd.read_csv('sensor_data.csv')

        # Convert the DataFrame to a list of dictionaries
        data_list = df.to_dict(orient='records')

        return jsonify({'data': data_list}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(host='192.168.60.30', port=5000)  # Replace with your IP and an open port
