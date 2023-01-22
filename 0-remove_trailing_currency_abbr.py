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


def remove_leading_abbr(abbr):
    """remove leading abbr"""
    return [x[3:] for x in df.amount]


def open_csv():
    """open csv"""
    #to do: use pandas to open a csv
    pass


def open_excel:
    """open excel"""
    #to do: use pandas to open an xls*
    pass


def convert_to_original:
    """convert to original"""
    #to do: use pandas to convert a df to original file format
    pass


def handle_doc_input():
    """ handle doc input"""
    if extension == '.csv':
        df = open_csv(file)
    if extension == '.xls' or '.xlsx':
        df = open_excel(file)
        
    df_removed = remove_leading_abbr(abbr)

    clean_doc = convert_to_original(df_removed)

    return clean_doc

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print(f'Usage: ./0-_remove_leading_abbr <PATH/TO/FILE> <ABBR>')
        print(f'Supported file formats: `.csv` `.xls` and `.xlsx`')
        print(f'Example: ./0-_remove_leading_abbr ~/Documents/my_file.csv KES')
        sys.exit(1)

    file = sys.argv[1]
    extension = pathlib.Path(file).suffix
    if extension != '.csv' or '.xlsx' or '.xls':
        print(f'So sorry your file cannot be read. Supported file formats: `.csv` `.xls` and `.xlsx`, for now.')
        sys.exit(1)
    
    abbr = sys.argv[2]
    handle_doc_input()