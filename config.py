import pyrebase

# Firebase configuration details (replace these with your actual Firebase project details)
config = {
    "apiKey": "AIzaSyBP9wFIYsMJo6WRq9BJd4-wsDGJaxgmp-A",
    "authDomain": "driver-drowsiness-detect-26cc0.firebaseapp.com",
    "databaseURL": "https://driver-drowsiness-detect-26cc0-default-rtdb.firebaseio.com",
    "projectId": "driver-drowsiness-detect-26cc0",
    "storageBucket": "driver-drowsiness-detect-26cc0.firebasestorage.app",
    "messagingSenderId": "190572891378",
    "appId": "1:190572891378:web:12952f388bde4e6b59146b",
    "measurementId": "G-3K4J04XBWF"

}

# Initialize Firebase
firebase = pyrebase.initialize_app(config)
db = firebase.database()


#include <ESP8266WiFi.h>          // Use <WiFi.h> for ESP32
#include <FirebaseESP8266.h>       // Use <FirebaseESP32.h> for ESP32
#include <ArduinoJson.h>

// Firebase project credentials
#define FIREBASE_HOST "https://driver-drowsiness-detect-26cc0-default-rtdb.firebaseio.com"
#define FIREBASE_AUTH "IzaSyBP9wFIYsMJo6WRq9BJd4-wsDGJaxgmp-A"

// Wi-Fi credentials
#define WIFI_SSID "YOUR_WIFI_SSID"
#define WIFI_PASSWORD "YOUR_WIFI_PASSWORD"

// Firebase and Wi-Fi objects
FirebaseData firebaseData;

// Motor control pin
const int motorPin = D3;  // Adjust pin for your motor driver
int eyeStatus = 0;

void setup() {
  Serial.begin(115200);
  pinMode(motorPin, OUTPUT);

  // Connect to Wi-Fi
  WiFi.begin(WIFI_SSID, WIFI_PASSWORD);
  Serial.print("Connecting to Wi-Fi...");
  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }
  Serial.println("\nConnected to Wi-Fi");

  // Connect to Firebase
  Firebase.begin(FIREBASE_HOST, FIREBASE_AUTH);
  Firebase.reconnectWiFi(true);
}

void loop() {
  // Fetch the eye_status from Firebase
  if (Firebase.getInt(firebaseData, "/drowsiness/eye_status")) {
    eyeStatus = firebaseData.intData();
    Serial.print("Eye Status: ");
    Serial.println(eyeStatus);

    // Control motor speed based on eye_status
    if (eyeStatus == 1) {
      // Eye closed, slow down the car
      analogWrite(motorPin, 100);  // Set PWM to reduce speed
      Serial.println("Slowing down car");
    } else {
      // Eye open, run at normal speed
      analogWrite(motorPin, 255);  // Full speed
      Serial.println("Car at normal speed");
    }
  } else {
    // Print any error messages
    Serial.println(firebaseData.errorReason());
  }

  delay(1000);  // Check Firebase every second
}
