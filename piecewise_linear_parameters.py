"""
piecewise_linear_parameters.py

This module provides a function for calculating the parameters of piecewise
linear segments within a Pandas DataFrame column.

Functions:
    piecewise_linear_parameters(df: pd.DataFrame, column: str) -> pd.DataFrame:
        Calculates slope and y-intercept for each linear segment.
"""

import numpy as np
import pandas as pd


def piecewise_linear_parameters(df: pd.DataFrame, column: str) -> pd.DataFrame:
    """
    Calculates the slope and y-intercept for each linear segment in a DataFrame column.

    This function calculates the slope and y-intercept for each
    consecutive pair of points, representing a linear segment.

    Args:
        df (pd.DataFrame): The DataFrame containing the data.
            It must have a 'time' column for x-values and the specified column for y-values.
        column (str): The name of the column in the DataFrame to calculate parameters for.

    Returns:
        pd.DataFrame: A DataFrame with the following columns:
            - 'x_start': The starting x-value (time) of each segment.
            - 'x_end': The ending x-value (time) of each segment.
            - 'slope': The slope of each segment.
            - 'y_intercept': The y-intercept of each segment.
    """

    x_values = df['time'].values
    y_values = df[column].values
    
    #while we know the data is sorted, let's ensure.
    indices = np.argsort(x_values)
    x_values = x_values[indices]
    y_values = y_values[indices]


    slopes = []
    intercepts = []
    x_starts = []
    x_ends = []

    for i in range(len(df) - 1):
        x_k, y_k = x_values[i], y_values[i]
        x_k1, y_k1 = x_values[i + 1], y_values[i + 1]

        # Calculate slope and intercept
        m_k = (y_k1 - y_k) / (x_k1 - x_k)
        b_k = y_k - m_k * x_k

        slopes.append(m_k)
        intercepts.append(b_k)
        x_starts.append(x_k)
        x_ends.append(x_k1)

    # Create and return the results DataFrame
    return pd.DataFrame({
        'x_start': np.array(x_starts, dtype=int),
        'x_end': np.array(x_ends, dtype=int),
        'slope': slopes,
        'y_intercept': intercepts
    })