import os
import cv2
import easyocr
import time
import matplotlib.pyplot as plt
import matplotlib.patches as patches

# Initialize EasyOCR reader
reader = easyocr.Reader(['en'])
output_data_list = []

# Start timer
start_time = time.time()

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
                audrino_plc_input = ""

                print(f"Text: {text}")

                # Check if text is "Emergency"
                if "Emergency" in text:
                    print("*********************")
                    print("EMERGENCY text found!")
                    print(f"Text: {text}, Bounding Box: {bbox}")
                    audrino_plc_input = "Emergency"
                    print(f"Audrino PLC Input: {audrino_plc_input}")
                    print("*********************")
                    current_time = time.time() - start_time
                    output_data_list.append(("EMERGENCY", current_time))
                    # Plot the image with bounding box
                    # plot_image_with_bounding_box(image, bbox)

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

# Folder path containing images
folder_path = "OUTPUT_FRAMES"

# Process images in the folder
process_images_in_folder(folder_path)
print(f" OUTPUT ::: {output_data_list}")