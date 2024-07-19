import pandas as pd
import numpy as np

def least_squares_approximation(df: pd.DataFrame, column: str) -> np.ndarray:
    """
    Calculates the coefficients for the least-squares linear approximation of the specified column's data over time.

    This function implements the direct calculation of the least squares method using the following formulas for a linear model (y = c0 + c1*x):

    c1 = (k * ∑(x_i * y_i) - ∑x_i * ∑y_i) / (k * ∑(x_i^2) - (∑x_i)^2)
    c0 = (∑y_i - c1 * ∑x_i) / k

    where:
        - k is the number of data points
        - x_i are the time values
        - y_i are the values in the specified column

    Args:
        df (pd.DataFrame): The input DataFrame containing the data. Must have a 'time' column for the x-values.
        column (str): The name of the column in the DataFrame for which to calculate the least squares approximation.

    Returns:
        np.ndarray: A NumPy array containing the coefficients of the least squares line, in the order [y-intercept (c0), slope (c1)].

    Raises:
        ZeroDivisionError: If the denominator in the slope calculation becomes zero, indicating that the data has no variation in x.
    """

    x_values = df['time'].values
    y_values = df[column].values

    # Ensure x_values are sorted
    indices = np.argsort(x_values)
    x_values = x_values[indices]
    y_values = y_values[indices]
    
    k = len(x_values)
    
    c1_denominator = (k * np.sum(x_values ** 2) - np.sum(x_values) ** 2)
    
    if c1_denominator == 0:
        raise ZeroDivisionError("Division by zero: Unable to calculate least squares coefficients.")
    
    c1 = (k * np.sum(x_values * y_values) - np.sum(x_values) * np.sum(y_values)) / c1_denominator
    c0 = (np.sum(y_values) - c1 * np.sum(x_values)) / k

    return np.array([c0, c1])