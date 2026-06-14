import serial
import time

PORT = "/dev/ttyACM0"
BAUD_RATE = 9600

print("Connecting to Arduino...")
arduino = serial.Serial(PORT, BAUD_RATE, timeout=2)


time.sleep(3)

print("Reading data...")


while True:
	line = arduino.readline().decode("utf-8", errors="ignore").strip()

	if line:
		print(line) 
