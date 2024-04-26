import csv

import time

# Function to process text file and write to CSV
def process_text_to_csv(input_file, output_file):
    with open(input_file, 'r') as file:
        lines = file.readlines()

    with open(output_file, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter='|')
        
        pattern_lines = []
        line_count = 0
        for line in lines:
            line = line.strip()
            if line:  # Non-empty line
                pattern_lines.append(line)
                if len(pattern_lines) == 4:   # Reached end of pattern
                    writer.writerow(pattern_lines)
                    pattern_lines = []
                    #writer.writerow(['\n'])
                elif len(pattern_lines) == 5:  
                    # Add newline for the fifth line
                    writer.writerow(['\n'])



def adrunio_input_process(output_file):
    # Define the file path
    file_path = output_file

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

# Example usage
input_file = 'yolo_model_output.txt'  # Update with your input file name
output_file = 'adruino_input.csv'  # Update with your desired output file name


print ( " Started task :: process_text_to_csv ")
process_text_to_csv(input_file, output_file)
print ( " Completed task :: process_text_to_csv ")
print ( " Started task :: adrunio_input_process ")
adrunio_input_process(output_file)
print ( " Completed task :: adrunio_input_process ")