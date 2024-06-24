# CSV Converter DECiM Script

The CSV Converter DECiM script is designed to process large CSV files, extracting specific columns from segmented measurements within the file, and writing these extracted columns to new CSV files. This script is particularly useful for datasets where measurements are detailed in segments and need individual processing.

## Getting Started

This guide will help you set up and run the CSV Converter DECiM script on your local machine.

### Prerequisites
You can use the included `.venv` file, which already has the necessary dependencies installed. 

This way you can use the run.bat file to run the script.

### Installation

1. **Clone the Repository**

   Clone the project repository to your local machine using:

   ```bash
   git clone https://yourrepository.com/path/to/csv_converter_DECiM
   ```

   Alternatively, download the script directly if it's available as a standalone file.

2. **Prepare Your CSV Files**

   Ensure your CSV files are in a known directory. The script expects CSV files to follow a specific format where measurements are segmented within the file.

### Running the Script

The script can be executed directly using Python or through a provided `run.bat` file for Windows users, which simplifies the process.

1. **Using Python Command**

   Open a terminal or command prompt, navigate to the directory containing the `csv_Converter_DECiM.py` script, and execute:

   ```bash
   python csv_Converter_DECiM.py
   ```
   If you have a valid python version installed localy.  
   
   Or:
   ```bash
   .venv\Scripts\python csv_Converter_DECiM.py
   ```

   
   The script will open a filepicker dialog to select the source CSV file which also becomes the target directory where the output files will be saved.


2. **Using run.bat File**

   For Windows users, a [`run.bat`](run.bat) file is provided to simplify execution. 

   - Double-click [`run.bat`](run.bat) to execute the script.

### Script Workflow

- The script reads the source CSV file, detecting its encoding to ensure correct processing.
- It skips the first row to remove any inconsistent header.
- The script then iterates over each row, grouping rows into individual measurements based on the file's structure.
- For each measurement, it extracts the 1st, 5th, and 6th columns and writes these to a new CSV file in the specified target directory.
- The process repeats for each measurement found in the source file.

### Output

- For each processed measurement, a new CSV file is created in the target directory.
- The script outputs the detected encoding of the source file, the number of processed measurements, and the total number of files created.

### Troubleshooting

- **Encoding Errors**: Ensure the `chardet` library is installed and the script correctly detects the encoding of your source CSV file.
- **File Not Found**: Verify the paths to the source CSV file and the target directory are correct.

## Contributing

Contributions to improve the script or address issues are welcome. Please contact the repository owner.

## License

Specify the license under which the script is released, if applicable.

