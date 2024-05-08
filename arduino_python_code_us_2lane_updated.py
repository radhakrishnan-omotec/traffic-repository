#PYTHON CODE:

import socket

import time

# IP address and port of the Arduino Opta WiFi server
arduino_ip = '192.168.0.155'  # Replace with the actual IP address of the Arduino Opta WiFi
port = 80  # Replace with the actual port number the Arduino is listening on

# Create a socket object
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the Arduino server
print(f"Connecting to Arduino at {arduino_ip}:{port}...")
client_socket.connect((arduino_ip, port))
print("Connected!")

# Assuming input_list contains the data to be sent to Arduino
input_list = [
    "Turn on green : Lane number : 0 , for 10 seconds",
    "Turn on green : Lane number : 0 , for 10 seconds",
    "Turn on green : Lane number : 0 , for 10 seconds",
    "Emergency : Turn on green : Lane number : 2 , for 10 seconds",
    "Emergency : Turn on green : Lane number : 1 , for 10 seconds",
    "Emergency : Turn on green : Lane number : 2 , for 10 seconds",
    "Emergency : Turn on green : Lane number : 2 , for 10 seconds",
    "Emergency : Turn on green : Lane number : 1 , for 10 seconds",
    "Turn on green : Lane number : 0 , for 10 seconds",
    "Turn on green : Lane number : 0 , for 10 seconds",
    "Turn on green : Lane number : 0 , for 10 seconds",
    "Emergency : Turn on green : Lane number : 1 , for 10 seconds",
    "Emergency : Turn on green : Lane number : 1 , for 10 seconds",
    "Turn on green : Lane number : 0 , for 10 seconds",
    "Turn on green : Lane number : 0 , for 10 seconds",
    "Turn on green : Lane number : 0 , for 10 seconds",
    "Turn on green : Lane number : 0 , for 10 seconds",
    "Turn on green : Lane number : 0 , for 10 seconds",
    "Turn on green : Lane number : 0 , for 10 seconds"
]

# Loop through the input_list
for data in input_list:
    # Send the data
    print(f"Sending data: {data}")
    client_socket.sendall(data.encode('utf-8'))
    
    # Receive a response from the Arduino (optional)
    response = client_socket.recv(1024).decode('utf-8')
    print(f"Received response: {response}")

    # Add a delay of 5 seconds
    time.sleep(5)

# Close the socket
client_socket.close()
print("Connection closed.")