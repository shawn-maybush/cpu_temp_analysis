"""
preprocess_temps.py

This module preprocesses temperature data from a raw input file.
It reads the data and parses it into a Pandas DataFrame.

Functions:
    preprocess_temps(input_file_path: str) -> pd.DataFrame:
        Preprocesses the raw temperature data from the input file.

"""

import pandas as pd
import numpy as np
from parse_temps import parse_raw_temps 


def preprocess_temps(input_file_path: str) -> pd.DataFrame:
    """
    Preprocesses raw temperature data from the input file.

    Args:
        input_file_path (str): The path to the raw temperature data file.

    Returns:
        pd.DataFrame: A DataFrame containing the time and temperature data.
    """
    with open(input_file_path, 'r') as temps_file:
        data = np.fromiter(
            parse_raw_temps(temps_file), dtype=np.dtype((float, 5))
        )

    df = pd.DataFrame(
        data, columns=['time', 'core_0', 'core_1', 'core_2', 'core_3']
    )
    df['time'] = df['time'].astype(int)  # Convert time to integer

    return df  # Return the DataFrame