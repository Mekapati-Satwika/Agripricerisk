import requests
import json
import random
import time

API_URL = "http://127.0.0.1:8000/predict"  # Change to your server IP if remote

while True:
    # Simulated sensor readings (replace with real sensor data later)
    sensor_data = {
        "crop": "Wheat",
        "temperature": round(random.uniform(20, 40), 2),
        "humidity": round(random.uniform(40, 90), 2),
        "rainfall": round(random.uniform(0, 100), 2),
        "soil_moisture": round(random.uniform(10, 60), 2)
    }

    print(f"📡 Sending data: {sensor_data}")

    try:
        response = requests.post(API_URL, json=sensor_data)
        print("✅ Response:", response.json())
    except Exception as e:
        print("❌ Error sending data:", e)

    # Wait for 10 seconds before sending next reading
    time.sleep(10)
