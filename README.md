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
   git clone https://github.com/KingPungy/csvToTab_DECiM.git
   ```

   Alternatively, download the script directly if it's available as a standalone file.

2. **Initialize the Virtual Environment**

   Run the `setup.bat` file to initialize the virtual environment and install the required dependencies. This step is necessary if you are not using the included `.venv` file.

3. **Prepare Your CSV Files**

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


### Script Workflow Detailed Explanation

The script's operation is streamlined for ease of use and efficiency, detailed in the following steps:

1. **Initiation via [`run.bat`](run.bat")**:
   - Users start the script by executing the [`run.bat`](run.bat") file. This method is designed for simplicity, allowing even those with minimal technical expertise to run the script without navigating command line interfaces.

2. **CSV File Selection**:
   - Upon execution, the script presents a file picker dialog. This interface is intuitive, guiding users to select the CSV file they wish to process. The selected CSV file:
     - May contain multiple measurements, delineated by empty lines, enabling batch processing in one go.
     - Serves as the basis for determining the target directory where the output files will be stored, ensuring that the outputs are easily locatable and organized relative to the source file.

3. **Processing and Output File Creation**:
   - The script meticulously processes the selected CSV file, identifying each measurement by the empty lines that separate them. For every measurement found:
     - It extracts the relevant data, focusing on the columns that contain the essential information for subsequent analysis 
         - The 1st, 5th, and 6th columns. (Can be changed in the script if needed)
     - It generates a new text file, formatting the extracted data with tab ('\t') separators for clarity and compatibility with further processing or analysis tools.

4. **Output File Naming and Structure**:
   - Each output file is thoughtfully named following the pattern `output_measurement_{measurement_number}-date`, where `{measurement_number}` is a sequentially assigned unique identifier for each measurement. This naming convention ensures easy identification and organization of the output files.
   - The header row of each output file is precisely defined to include "Frequency (Hz)", "|Z| (ohms)", and "Phase of Z (deg)" columns. This specific arrangement caters to the requirements of the DECiM software, facilitating seamless integration and use of the output files in subsequent analyses.


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

