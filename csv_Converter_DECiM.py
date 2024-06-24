"""
Created on Mon Jun 24 15:55:00 2024

@author: Scott.Timmermans


Usage:
1. Run this script by executing the run.bat file. 
2. This script will open a file picker dialog that allows you to select a CSV file. 
    1.a The CSV file can contain multiple measurements separated by empty lines.
    1.b The selected file also determines the target directory for the output files.
3. The script will then process the file and create a new text file for each measurement in the CSV file. (these are separated by empty lines in the CSV file, if present).
4. The text files will contain the desired columns from each measurement, separated by tabs ('\t').
5. Each text file will be named 'output_measurement_{measurement_number}-date' where {measurement_number} is a unique number for each measurement.
6. The header row will contain the columns: "Frequency (Hz)", "|Z| (ohms)", "Phase of Z (deg)". as required by the DECiM software.


"""

import csv
import tkinter as tk
from tkinter import filedialog
import chardet
import os



# Function to process a measurement
def process_measurement(measurement, measurement_count,target_directory):
    # Open a new text file for writing
    date = measurement[2][1].replace(":", "_") # Extract the date from the 3rd row and replace the colons with underscores to avoid issues with file names
    
    file_name = f'{target_directory}/output_measurement_{measurement_count+1} - {date}.txt'
    
    with open(file_name, 'w', newline='') as txt_file:
        # Create a CSV writer
        csv_writer = csv.writer(txt_file, delimiter='\t')

        # Write the header row
        csv_writer.writerow(["Frequency (Hz)", "|Z| (ohms)", "Phase of Z (deg)"]) # Required by DECiM software

        # Iterate over each row in the measurement
        for row in measurement[6:]: # Skip the first 6 rows
            # Extract the desired columns
            columns = [row[0], row[4], row[5]]  # only add 1st, 5th, and 6th columns from the measurement

            # Write the columns to the CSV file
            csv_writer.writerow(columns)
    return file_name        
    



def process_file(file_path,target_directory):
    # Open the CSV file for reading
    with open(file_path, 'rb') as csv_file:
        # Detect the encoding of the file
        print("Detecting encoding...")
        raw_data = csv_file.read()
        encoding = chardet.detect(raw_data)['encoding']
        print(f"Encoding detected: {encoding}")

    # Open the CSV file again with the detected encoding
    with open(file_path, 'r', encoding=encoding) as csv_file:
        # Create a CSV reader
        print("Reading CSV file...")
        csv_reader = csv.reader(csv_file)
       
        next(csv_reader) # Skip the first row to remove inconsistent header
        # Initialize variables for tracking measurements
        measurement_count = 0
        current_measurement = []
        created_files = []

        # Iterate over each row in the CSV file
        for row in csv_reader:
            # Check if the row is empty and send collected data to process_measurement
            if not any(row):
                # Check if there is a current measurement
                if current_measurement:
                    # Process the current measurement
                    created_files.append(process_measurement(current_measurement, measurement_count,target_directory))
                    print(f"Processed measurement {measurement_count}")
                    measurement_count += 1
                    current_measurement = []
                continue  # Skip empty lines

            # Check if it's a new measurement
            if len(current_measurement) == 0:
                current_measurement.append(row)
            else:
                # Check if it's the end of the current measurement
                if len(row) == 1 and not row[0].strip():
                    # Process the current measurement
                    created_files.append(process_measurement(current_measurement, measurement_count,target_directory))
                    print(f"Processed measurement {measurement_count}")
                    measurement_count += 1
                    current_measurement = []
                else:
                    current_measurement.append(row)

        # Process the last measurement if there is one
        # print(current_measurement)
        if current_measurement and current_measurement[0] != ["﻿"]:  # check if the last measurement is not empty 
            created_files.append(process_measurement(current_measurement, measurement_count,target_directory))
    
    print(f"Created {len(created_files)} files:")
    for file in created_files:
        print(file)



if __name__ == "__main__":

    # Create a Tkinter root window
    root = tk.Tk()
    root.withdraw()

    # Open the file picker dialog
    csv_file_path = filedialog.askopenfilename(filetypes=[("CSV Files", "*.csv")])

    # Extract the directory path from the selected file
    target_directory = os.path.dirname(csv_file_path)
    print(f"Selected Target Save directory: {target_directory}/")
    # Check if a file was selected
    if csv_file_path:
        print("Start Processing file...")
        process_file(csv_file_path,target_directory)
        print("Done!")

    

# print(f"Selected file: {csv_file_path}")
# # Check if a file was selected
# if csv_file_path:
#     print("Processing file...")
#     # Open the CSV file for reading
#     with open(csv_file_path, 'r') as csv_file:
#         # Create a CSV reader
#         csv_reader = csv.reader(csv_file)

#         # Skip the headers
#         skips = 6  # Skip the first 6 rows
#         for _ in range(skips):
#             next(csv_reader)

#         # Open a new text file for writing
#         with open('output.txt', 'w') as txt_file:
#             # Iterate over each row in the CSV file
#             for row in csv_reader:
#                 # Check if the row is empty
#                 if not any(row):
#                     continue  # Skip empty lines

#                 # Extract the desired columns
#                 columns = [row[0], row[4], row[5]]  # 1st, 5th, and 6th columns

#                 # Write the columns to the text file, separated by tabs
#                 txt_file.write('\t'.join(columns) + '\n')

#     print("Done!")