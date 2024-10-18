import requests

# Replace with your actual server IP address and port
server_url = "http://192.168.56.1:5000/api"

def test_post():
    # Define the data to send (temperature, humidity, mq4, and mq3)
    post_data = {
        'temperature': 25.5,
        'humidity': 60.0,
        'mq4': 300.0,  # Example value for MQ-4 sensor
        'mq3': 200.0   # Example value for MQ-3 sensor
    }

    # Send a POST request
    response = requests.post(server_url, data=post_data)

    # Print the response
    print(f"POST Response ({response.status_code}): {response.json()}")

def test_get():
    # Send a GET request
    response = requests.get(server_url)

    # Print the response
    print(f"GET Response ({response.status_code}): {response.json()}")

if __name__ == "__main__":

    print("Testing POST request...")
    test_post()

    print("\nTesting GET request...")
    test_get()
