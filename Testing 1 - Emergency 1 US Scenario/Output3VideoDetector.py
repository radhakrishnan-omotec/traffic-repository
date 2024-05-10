import os
import cv2
import easyocr
import matplotlib.pyplot as plt
import matplotlib.patches as patches

import socket


# Initialize EasyOCR reader
reader = easyocr.Reader(['en'])
output_data_list = []

# Function to process images in a folder
def process_images_in_folder(folder_path):
    # List all files in the folder
    image_files = os.listdir(folder_path)

    # Process each image in the folder
    for image_file in image_files:
        # Read the image
        image_path = os.path.join(folder_path, image_file)
        image = cv2.imread(image_path)

        # Convert image to RGB (EasyOCR expects RGB)
        rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

        # Use EasyOCR to detect text in the image
        results = reader.readtext(rgb_image)

        # Check if any text is detected
        if results:
            print(f"Text detected in {image_file}:")
            for result in results:
                text = result[1]
                bbox = result[0]
                
                
                
                print(f"Text: {text}")

                # Check if text is "Emergency"
                if "Emergency" in text:
                    print("*********************")
                    print("EMERGENCY text found!")
                    print(f"Text: {text}, Bounding Box: {bbox}")
                    print("*********************")
                    output_data_list.append("EMERGENCY")
                    
                    # Plot the image with bounding box
                    #plot_image_with_bounding_box(image, bbox)
                    
                    # Send the last element of output_data_list to Arduino
                    if output_data_list:
                        last_element_arduino_data = output_data_list[-1]
                        send_data_to_arduino(last_element_arduino_data)

        else:
            print(f"No EMERGENCY text detected in {image_file}")

# Function to plot image with bounding box
def plot_image_with_bounding_box(image, bbox):
    fig, ax = plt.subplots(1)
    ax.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))

    # Add bounding box to the plot
    x, y, w, h = bbox
    rect = patches.Rectangle((x, y), w, h, linewidth=1, edgecolor='r', facecolor='none')
    ax.add_patch(rect)

    plt.show()


# Function to send data to Arduino
def send_data_to_arduino(data):
    # Code to send data to Arduino goes here
    print("********* Arduino *********")
    print("Sending data to Arduino:", data)
    client_call_to_ardunio_server(data)
    print("********* Arduino *********")
    
    
# Function to call Arduino Server  
def client_call_to_ardunio_server(input):
    # IP address and port of the Arduino Opta WiFi server
    arduino_ip = '192.168.0.155'  # Replace with the actual IP address of the Arduino Opta WiFi
    port = 80  # Replace with the actual port number the Arduino is listening on

    # Create a socket object
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Connect to the Arduino server
    print(f"Connecting to Arduino at {arduino_ip}:{port}...")
    client_socket.connect((arduino_ip, port))
    print("Connected!")
    
    # Send the data
    print(f"Sending Arduino data: {input}")
    client_socket.sendall(input.encode('utf-8'))
    
    # Receive a response from the Arduino (optional)
    response = client_socket.recv(1024).decode('utf-8')
    print(f"Received Arduino response: {response}")
    
    # Close the socket
    client_socket.close()
    print("Connection closed.")

    
    
# Folder path containing images
folder_path = "OUTPUT_FRAMES"

# Process images in the folder
process_images_in_folder(folder_path)
print(f" OUTPUT ::: {output_data_list}")