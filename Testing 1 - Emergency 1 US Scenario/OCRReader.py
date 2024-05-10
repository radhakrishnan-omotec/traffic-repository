import os
os.environ['OMP_DYNAMIC'] = 'FALSE'  # Set OMP_DYNAMIC environment variable to prevent multiple copies of OpenMP runtime

import cv2
import easyocr

# Load the video
video_path = 'traffic_density_analysis_emergency1.mp4'
cap = cv2.VideoCapture(video_path)

# Initialize EasyOCR reader
reader = easyocr.Reader(['en'])

# Function to find "Emergency" text coordinates in a frame
def find_emergency_text(frame):
    result = reader.readtext(frame)
    for detection in result:
        if 'Emergency' in detection[1]:
            # Extracting bounding box coordinates
            top_left = tuple(detection[0][0])
            bottom_right = tuple(detection[0][2])
            return top_left, bottom_right
    return None, None

# Process frames
while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    # Find "Emergency" text coordinates in the frame
    top_left, bottom_right = find_emergency_text(frame)

    # Draw bounding box around the text
    if top_left and bottom_right:
        cv2.rectangle(frame, top_left, bottom_right, (0, 255, 0), 2)
        print("Emergency text coordinates:", top_left, bottom_right)

    # Display the frame
    cv2.imshow('Frame', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release resources
cap.release()
cv2.destroyAllWindows()