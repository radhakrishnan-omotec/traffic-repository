import time

# Define the file path
file_path = "adruino_input.csv"

# Initialize an empty list to store the last values
arduino_list = []

# Read the CSV file, split tokens by "|" symbol, and extract the last value
with open(file_path, 'r') as file:
    for line in file:
        tokens = line.strip().split("|")
        # Assuming the last value is at index -1
        last_value = tokens[-1]
        arduino_list.append(last_value)

# Display the list
print("Arduino last values:")
print(arduino_list)

# Loop through the arduino_list to identify consecutive entries
consecutive_count = 1
previous_value = arduino_list[0]
lane_open_duration ="10 seconds"

for i in range(1, len(arduino_list)):
    current_value = arduino_list[i]
    
    if current_value == previous_value:
        consecutive_count += 1
    else:
        if consecutive_count >= 5:
            print(f"Turn on green : Lane number : {previous_value} , for {lane_open_duration}" )
        consecutive_count = 1
    
    previous_value = current_value

    # # Wait for 1 second before next iteration
    # time.sleep(1)
    # Wait for 1 millisecond before next iteration
    time.sleep(0.001)
    
# # Check for the last consecutive entries
# if consecutive_count >= 5:
#     print(f"Last Turn on green : Lane number : {previous_value} , for {lane_open_duration}" )