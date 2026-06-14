import serial
import csv
from datetime import datetime
import time

PORT = "/dev/ttyACM0"
BAUD_RATE = 9600
CSV_FILE = "data/sensor_data.csv"

arduino = serial.Serial(PORT, BAUD_RATE, timeout=2)
time.sleep(3)

with open(CSV_FILE, mode="a", newline="") as file:
    writer = csv.writer(file)

    if file.tell() == 0:
        writer.writerow(["timestamp", "temperature_c", "humidity_percent"])

    while True:
        line = arduino.readline().decode("utf-8", errors="ignore").strip()
        print(line)

        if "Temperature:" in line and "Humidity:" in line:
            temp = line.split("Temperature:")[1].split("C")[0].strip()
            humidity = line.split("Humidity:")[1].split("%")[0].strip()

            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            writer.writerow([timestamp, temp, humidity])
            file.flush()

            print("Saved:", timestamp, temp, humidity)
