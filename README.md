# CPU Temperature Analysis

This project analyzes CPU temperature data to identify trends and patterns. It utilizes piecewise linear interpolation to approximate the temperature readings within intervals and calculates a global linear least-squares approximation for the overall trend.

## Project Structure

The project consists of the following files:

- `cpu_temp_analysis.py`: Main script that orchestrates the analysis process.
- `preprocess_temps.py`: Contains functions for preprocessing the raw temperature data.
- `piecewise_linear_parameters.py`: Contains functions for performing piecewise linear interpolation and calculating parameters.
- `parse_temps.py`: Parses the temperature data from the input file line by line.
- `least_squares_approximation.py`: Contains a function for calculating the least squares linear approximation using the normal equations.
- `requirements.txt`: Contains the required modules for the project.

## Usage

1. **Prepare Input Data:**
   - The input data should be a text file containing CPU temperature readings over time.
   - The file should be named in the format `sensors-YYYY.MM.DD-no-labels.txt` or `sensors-YYYY.MM.DD.txt`.
   - Each line in the file represents a set of temperature readings for different cores in 30-second intervals.
   - The values on each line are separated by spaces, and the values may or may not include the `+` symbol.

2. **Run the Script:**
   - Open a terminal or command prompt.
   - Navigate to the project directory.
   - Execute the following command, replacing `input_file.txt` with the actual name of your input file:
     ```bash
     python cpu_temp_analysis.py input_file.txt
     ```

3. **Output:**
   - The script will generate separate output files for each CPU core.
   - The output files will be named `basename_core_number.txt`, where `basename` is the name of the input file without the extension.
   - Each output file will contain:
     - A list of piecewise linear equations for each interval (interpolation).
     - A least-squares linear equation approximating the overall trend.

## Example

**Input File (sensors-2019.01.26.txt):**

```txt
61.0 63.0 50.0 58.0
80.0 81.0 68.0 77.0
62.0 63.0 52.0 60.0
83.0 82.0 70.0 79.0
68.0 69.0 58.0 65.0
82.0 81.0 67.0 77.0
```
or
```txt
+61.0°C +63.0°C +50.0°C +58.0°C
+80.0°C +81.0°C +68.0°C +77.0°C
+62.0°C +63.0°C +52.0°C +60.0°C
+83.0°C +82.0°C +70.0°C +79.0°C
+68.0°C +69.0°C +58.0°C +65.0°C
+82.0°C +81.0°C +67.0°C +77.0°C
```

**Output Files (sensors-2019.01.26_core_number.txt):**

```
0 <= x < 30 ; y =   61.0000 +    0.6333 x ; interpolation
30 <= x < 60 ; y =   98.0000 +   -0.6000 x ; interpolation
60 <= x < 90 ; y =   20.0000 +    0.7000 x ; interpolation
90 <= x < 120 ; y =  128.0000 +   -0.5000 x ; interpolation
120 <= x <= 150 ; y =   12.0000 +    0.4667 x ; interpolation
0 <= x <= 150 ; y =   67.4000 +    0.0567 x ; least-squares
```

## Dependencies

- Python 3.x
- pandas
- numpy



## Installation
- Install Python 3.x if you haven't already.
- Install the required dependencies using pip:
```bash
pip install -r requirements.txt
```
## License

This project is licensed under the MIT License.