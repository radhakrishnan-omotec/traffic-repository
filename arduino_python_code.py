#PYTHON CODE:

import socket

# IP address and port of the Arduino Opta WiFi server
arduino_ip = '192.168.0.164'  # Replace with the actual IP address of the Arduino Opta WiFi
port = 80  # Replace with the actual port number the Arduino is listening on

# Create a socket object
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the Arduino server
print(f"Connecting to Arduino at {arduino_ip}:{port}...")
client_socket.connect((arduino_ip, port))
print("Connected!")

# Data to send to the Arduino (change as needed)
print("enter status")
data = input("")

# Send the data
print(f"Sending data: {data}")
client_socket.sendall(data.encode('utf-8'))

# Receive a response from the Arduino (optional)
response = client_socket.recv(1024).decode('utf-8')
print(f"Received response: {response}")

# Close the socket
# client_socket.close()
# print("Connection closed.")