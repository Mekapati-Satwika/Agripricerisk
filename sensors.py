import random
import time

def read_sensor_data():
    # Simulate sensor readings
    return {
        "temperature": round(random.uniform(20, 40), 2),
        "humidity": round(random.uniform(30, 80), 2),
        "soil_moisture": round(random.uniform(10, 60), 2)
    }

if __name__ == "__main__":
    while True:
        data = read_sensor_data()
        print(data)
        time.sleep(3)
