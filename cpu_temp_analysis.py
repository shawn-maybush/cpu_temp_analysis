"""
cpu_temp_analysis.py

This script is the main entry point for the CPU temperature analysis project.
It reads raw temperature data from a file, preprocesses it, performs piecewise
linear interpolation to calculate the slope and y-intercept for each interval,
and prints the results in the specified format.
"""
import sys
from preprocess_temps import preprocess_temps
from piecewise_linear_parameters import piecewise_linear_parameters
from least_squares_approximation import least_squares_approximation
import re




def main():
    """Main function to execute the CPU temperature analysis."""
    if len(sys.argv) < 2:  # Check if at least one argument was provided
        print("Usage: python cpu_temp_analysis.py input_file")
        sys.exit(1)  # Exit with an error code if no arguments are provided
    
    input_file = sys.argv[1]  # Get the input file from the command line argument

    # Data Preprocessing
    try:
        df = preprocess_temps(input_file)
    except FileNotFoundError:
        print(f"Error: File not found - {input_file}")
        return  # Exit if file not found
    
    basename = re.match(r"^sensors-\d{4}.\d{2}.\d{2}", input_file).group(0) # Extract the file name without extension
    

    # Piecewise Linear Interpolation
    for column in df.columns:
        if column != 'time':  # Skip the 'time' column
            output_file = f"{basename}_{column}.txt"  # Generate the output file name
            params_df = piecewise_linear_parameters(df, column)
            least_squares_coefficients = least_squares_approximation(df, column)
            

            # Print and Write results to file
            with open(output_file, "w") as f:
                for _, row in params_df.iterrows():
                    col_interpol = f"{row['x_start']:6.0f} <= x <= {row['x_end']:6.0f} ; y = {row['y_intercept']:12.4f} + {row['slope']:12.4f} x ; interpolation"
                    print(col_interpol)
                    f.write(col_interpol + "\n")
                col_least_squares = f"{params_df['x_start'].min():6.0f} <= x <= {params_df['x_end'].max():6.0f} ; y = {least_squares_coefficients[0]:12.4f} + {least_squares_coefficients[1]:12.4f} x ; least-squares"
                print(col_least_squares)
                f.write(col_least_squares + "\n")
            
            print(f"Results saved to {output_file}\n")


if __name__ == "__main__":
    main()
