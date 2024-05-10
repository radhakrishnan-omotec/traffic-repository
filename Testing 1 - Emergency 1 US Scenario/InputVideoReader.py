import cv2
import os

# Open the input video
video_path = "traffic_density_analysis_emergency1.mp4"
cap = cv2.VideoCapture(video_path)

# Check if video opened successfully
if not cap.isOpened():
    print("Error opening video!")
    exit()

# Create the output directory if it doesn't exist
output_dir = "OUTPUT_FRAMES"
os.makedirs(output_dir, exist_ok=True)

# Initialize variables
frame_count = 0
frame_interval = 30  # Write a frame every 30 frames
section_duration = 5  # Duration of each section in seconds
section_frames = 0  # Count of frames in the current section
section_start_time = None  # Start time of the current section

# Process video frames
while True:
    # Read a frame
    ret, frame = cap.read()

    # Check if frame is read correctly
    if not ret:
        print("No more frames to process!")
        break

    # Increment frame count and section frame count
    frame_count += 1
    section_frames += 1

    # Check if it's time to start a new section
    if section_start_time is None:
        section_start_time = cap.get(cv2.CAP_PROP_POS_MSEC) / 1000  # Convert milliseconds to seconds

    # Check if the duration of the current section exceeds the specified duration
    if cap.get(cv2.CAP_PROP_POS_MSEC) / 1000 - section_start_time >= section_duration:
        # Reset section frame count and start time
        section_frames = 0
        section_start_time = None

    # Check if the current frame should be written
    if frame_count % frame_interval == 0:
        # Write the frame as a PNG image
        frame_filename = f"frame_{frame_count}.png"
        output_path = os.path.join(output_dir, frame_filename)
        cv2.imwrite(output_path, frame)
        print(f"Frame {frame_count} saved as {frame_filename}")

# Release video capture
cap.release()

print("Frame extraction completed!")