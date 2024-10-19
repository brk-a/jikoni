#!/usr/bin/env python3

'''
Remove leading currency abbreviations
or symbols from a `.csv` or `.xls*`

return: a `.csv` or `.xls*` object or 0 -> success,
else, 1
'''

import os
import sys
import pathlib
import pandas as pd
import mimetypes


def remove_leading_abbr(df, abbr):
    """remove leading abbr"""
    return [x[3:] for x in df.amount]


def open_csv(file_path: str) -> pd.DataFrame:

    """
    Opens a CSV file using pandas.

    Args:
    file_path (str): The path to the CSV file.

    Returns:
    pd.DataFrame: A pandas DataFrame containing the data from the CSV file.

    Raises:
    TypeError: If the file path is not a string.
    FileNotFoundError: If the file does not exist.
    PermissionError: If the file cannot be opened due to permissions issues.
    ValueError: If the file is not a CSV file.
    pd.errors.EmptyDataError: If the CSV file is empty.
    pd.errors.ParserError: If the CSV file is corrupted or malformed.
    Exception: For any unexpected errors during file reading.
    """

    # Check if the file path is a string
    if not isinstance(file_path, str):
        raise TypeError("File path must be a string.")


    # Check if the file exists
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"The file '{file_path}' does not exist.")


    # Check if the file can be opened for reading
    if not os.access(file_path, os.R_OK):
        raise PermissionError(f"The file '{file_path}' cannot be opened due to permissions issues.")

    # Check if the file is a CSV file using MIME type
    mime_type, _ = mimetypes.guess_type(file_path)
    if mime_type != 'text/csv':
        raise ValueError("The file is not a valid CSV file.")

    # Open the CSV file using pandas
    try:
        df = pd.read_csv(file_path)
        return df
    except pd.errors.EmptyDataError:
        raise pd.errors.EmptyDataError("The CSV file is empty.")
    except pd.errors.ParserError:
        raise pd.errors.ParserError("The CSV file is corrupted or malformed.")
    except Exception as e:
        raise Exception(f"An unexpected error occurred: {e}")


def open_excel(file_path: str) -> pd.DataFrame:

    """
    Opens an Excel file (.xls or .xlsx) using pandas.

    Args:
    file_path (str): The path to the Excel file.


    Returns:
    pd.DataFrame: A pandas DataFrame containing the data from the Excel file.

    Raises:
    TypeError: If the file path is not a string.
    FileNotFoundError: If the file does not exist.
    PermissionError: If the file cannot be opened due to permissions issues.
    ValueError: If the file is not an Excel file.
    pd.errors.EmptyDataError: If the Excel file is empty.
    pd.errors.ParserError: If the Excel file is corrupted or malformed.
    Exception: For any unexpected errors during file reading.
    """

    # Check if the file path is a string
    if not isinstance(file_path, str):
        raise TypeError("File path must be a string.")

    # Check if the file exists
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"The file '{file_path}' does not exist.")

    # Check if the file can be opened for reading
    if not os.access(file_path, os.R_OK):
        raise PermissionError(f"The file '{file_path}' cannot be opened due to permissions issues.")

    # Check if the file is an Excel file using MIME type
    mime_type, _ = mimetypes.guess_type(file_path)
    if mime_type not in ['application/vnd.ms-excel', 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet']:
        raise ValueError("The file is not a valid Excel file.")

    # Open the Excel file using pandas
    try:
        df = pd.read_excel(file_path)
        return df
    except ValueError as ve:
        raise ValueError("The Excel file is empty or not formatted correctly.") from ve
    except Exception as e:
        raise Exception(f"An unexpected error occurred: {e}")


def convert_to_original(df: pd.DataFrame, file_path: str) -> None:

    """
    Saves a pandas DataFrame to a specified file format (CSV, XLS, or XLSX).
    Creates the file if it does not exist.

    Args:
    df (pd.DataFrame): The pandas DataFrame to save.
    file_path (str): The path to save the file.

    Raises:
    TypeError: If the DataFrame is not a pandas DataFrame or if the file path is not a string.
    ValueError: If the file extension is not supported.
    PermissionError: If the file cannot be created or written to due to permissions issues.
    Exception: For any unexpected errors during file saving.
    """

    # Check if df is a pandas DataFrame
    if not isinstance(df, pd.DataFrame):
        raise TypeError("The input must be a pandas DataFrame.")

    # Check if the file path is a string
    if not isinstance(file_path, str):
        raise TypeError("File path must be a string.")

    # Ensure the directory exists, create if it doesn't
    directory = os.path.dirname(file_path)
    if directory and not os.path.exists(directory):
        os.makedirs(directory)

    # Check if the file can be opened for writing
    if not os.access(directory, os.W_OK):
        raise PermissionError(f"The directory '{directory}' cannot be written to.")

    # Determine the file extension and save the DataFrame accordingly
    try:
        if file_path.endswith('.csv'):
            df.to_csv(file_path, index=False)
        elif file_path.endswith('.xls') or file_path.endswith('.xlsx'):
            df.to_excel(file_path, index=False)
        else:
            raise ValueError("The file extension must be .csv, .xls, or .xlsx.")
    except Exception as e:
        raise Exception(f"An unexpected error occurred while saving the DataFrame: {e}")


def handle_doc_input(file, extension, abbr):
    """ handle doc input"""
    if extension == '.csv':
        df = open_csv(file)
    if extension == '.xls' or '.xlsx':
        df = open_excel(file)
        
    df_removed = remove_leading_abbr(df, abbr)

    clean_doc = convert_to_original(df_removed, extension)

    return clean_doc

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print(f'Usage: ./0-remove_leading_abbr <PATH/TO/FILE> <ABBR>')
        print(f'Supported file formats: `.csv` `.xls` and `.xlsx`')
        print(f'Example: ./0-remove_leading_abbr ~/Documents/my_file.csv KES')
        sys.exit(1)

    file = sys.argv[1]
    extension = pathlib.Path(file).suffix
    if extension != '.csv' or '.xlsx' or '.xls':
        print(f'So sorry your file cannot be read. Supported file formats: `.csv` `.xls` and `.xlsx`, for now.')
        sys.exit(1)
    
    abbr = sys.argv[2]
    handle_doc_input(file, extension, abbr)