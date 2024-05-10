import cv2
import easyocr
import time
import os

# Initialize EasyOCR reader with GPU acceleration
reader = easyocr.Reader(['en'], gpu=True)

# Open the input video
cap = cv2.VideoCapture("traffic_density_analysis_emergency1.mp4")

# Check if video opened successfully
if not cap.isOpened():
    print("Error opening video!")
    exit()

# Create the output directory if it doesn't exist
output_dir = "OUTPUT"
os.makedirs(output_dir, exist_ok=True)

# Initialize variables for time-based frame reading
start_time = time.time()
cumulative_time = 0

# Process video frames
while True:
    # Read a frame
    ret, frame = cap.read()

    # Check if frame is read correctly
    if not ret:
        print("No more frames to process!")
        break

    # Convert frame to RGB format (EasyOCR expects RGB)
    rgb_frame = frame[:, :, ::-1]

    # Use EasyOCR to detect text in the frame
    results = reader.readtext(rgb_frame)

    # Loop through detected text
    for result in results:
        text = result[0]
        confidence = result[1]
        bbox = result[2]  # Bounding box coordinates (x1, y1, x2, y2)

        # Check if the text is "Emergency" and confidence is high
        if text == "Emergency" and confidence > 0.5:
            # Save the frame with bounding box as an image in the output folder
            filename = f"frame_{int(cap.get(cv2.CAP_PROP_POS_FRAMES))}_emergency.jpg"
            output_path = os.path.join(output_dir, filename)
            cv2.imwrite(output_path, frame)
            print(f"Saved frame {filename} with Emergency text at coordinates: {bbox}")

    # Calculate elapsed time and reset if exceeds 5 seconds
    elapsed_time = time.time() - start_time
    if elapsed_time >= 5:
        start_time = time.time()  # Reset start time
        cumulative_time += elapsed_time  # Add to cumulative time
        cap.set(cv2.CAP_PROP_POS_FRAMES, 0)  # Reset video to start
        print(f"Cumulative elapsed time: {cumulative_time} seconds")

    # Exit with 'q' key press
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release video capture and close windows
cap.release()
cv2.destroyAllWindows()

print("Video processing completed!")