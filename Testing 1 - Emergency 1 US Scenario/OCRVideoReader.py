import cv2
import easyocr
import time

# Initialize EasyOCR reader with GPU acceleration
reader = easyocr.Reader(['en'], gpu=True)

# Open the input video
cap = cv2.VideoCapture("traffic_density_analysis_emergency1.mp4")

# Check if video opened successfully
if not cap.isOpened():
    print("Error opening video!")
    exit()

# Process video frames
while True:
    start_time = time.time()  # Record start time

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
            # Print text coordinates
            print(f"Text: {text}, Confidence: {confidence}, Coordinates: {bbox}")

    # Display the frame with text overlay (optional)
    # cv2.imshow("Frame", frame)

    # Print frame read status every second
    elapsed_time = time.time() - start_time
    if elapsed_time >= 1:
        print("Frame read status:", ret)
    
    # Exit with 'q' key press
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release video capture and close windows
cap.release()
cv2.destroyAllWindows()

print("Video processing completed!")