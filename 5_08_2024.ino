#include <WiFi.h>
#include <HTTPClient.h>
#include <DHT.h>

#define DHTPIN 4        // Pin connected to the DHT11 data pin
#define DHTTYPE DHT11   // DHT 11 sensor
#define MQ4_PIN 34      // Pin connected to MQ-4 sensor
#define MQ3_PIN 35      // Pin connected to MQ-3 sensor

const char* ssid = "****";        // Replace with your Wi-Fi SSID
const char* password = "**********"; // Replace with your Wi-Fi password
const char* serverName = "http://192.168.0.102:5000/api"; // Replace with your Flask server's actual IP

DHT dht(DHTPIN, DHTTYPE);

void setup() {
  Serial.begin(115200);
  dht.begin();

  // Connect to Wi-Fi
  WiFi.begin(ssid, password);
  Serial.print("Connecting to Wi-Fi");
  while (WiFi.status() != WL_CONNECTED) {
    delay(1000);
    Serial.print(".");
  }
  Serial.println("Connected to Wi-Fi");
}

void loop() {
  // Reading temperature and humidity data from DHT11
  float temperature = dht.readTemperature();
  float humidity = dht.readHumidity();

  // Reading gas sensor data (MQ-4 and MQ-3)
  int mq4Value = analogRead(MQ4_PIN);
  int mq3Value = analogRead(MQ3_PIN);


  // Check if any reads failed and exit early
  if (isnan(temperature) || isnan(humidity)) {
    Serial.println("Failed to read from DHT sensor!");
    return;
  }

  // If Wi-Fi is connected, send data to the server
  if (WiFi.status() == WL_CONNECTED) {
    sendDataToServer(temperature, humidity, mq4Value, mq3Value);
  } else {
    Serial.println("WiFi Disconnected");
  }

  delay(5000);  // Wait 5 seconds before reading again
}

void sendDataToServer(float temperature, float humidity, int mq4, int mq3) {
  HTTPClient http;
  http.begin(serverName);   // Initialize HTTP connection
  Serial.println(serverName);
  http.addHeader("Content-Type", "application/x-www-form-urlencoded");  // Send as form data

  // Construct POST data
  String postData = "temperature=" + String(temperature) + "&humidity=" + String(humidity) + "&mq4=" + String(mq4) + "&mq3=" + String(mq3);
  
  int httpResponseCode = http.POST(postData);  // Send HTTP POST request

  // Check response
  if (httpResponseCode > 0) {
    String response = http.getString();
    Serial.println(httpResponseCode);  // HTTP response code
    Serial.println(response);          // Server response
  } else {
    Serial.print("Error on sending request: ");
    Serial.println(httpResponseCode);
  }
  
  http.end();  // Close HTTP connection
}
