#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 8 14:44:33 2023
Based on: https://www.kaggle.com/datasets/arbazmohammad/world-airports-and-airlines-datasets
Sample input: --AIRLINES="airlines.yaml" --AIRPORTS="airports.yaml" --ROUTES="routes.yaml" --QUESTION="q1" --GRAPH_TYPE="bar"
@author: rivera
@author: V00978012
"""

from sys import argv as program_args
import pandas as pd
from pandas import DataFrame

def main():
    """Main entry point of the program."""

    my_args: dict = {}
    for arg in program_args:             # Argument processing.
        if arg.startswith('--'):
            arg_split: list = arg.split('=')
            key: str = arg_split[0]
            value: str = arg_split[1]
            my_args[key.replace('--', '')] = value

    sort_by = my_args['sortBy']        # Argument variables.
    display = my_args['display']
    files = my_args['files']

    file_list: list = files.split(',')      # Array of file arguments.

    merged_data: DataFrame = merge_files(file_list, sort_by, display)   # Call to Merge data if multiple file arguments.

    file_output = output_file('output.csv')     # Call to write to output file.

    csv_data = merged_data.to_csv(index=False)
    file_output.write(csv_data)

    file_output.close()


def merge_files(file_list: list, sort_by: str, display: str) -> DataFrame:
    """merge_files function merges the data from all file arguments and returns a sorted dataframe."""

    merged_data: DataFrame = pd.DataFrame()
    for file in file_list:
        file_input = input_file(file)
        answer = output_display(file, sort_by, display)
        merged_data = pd.concat([merged_data, answer], ignore_index=True)
        file_input.close()

    merged_data = merged_data.sort_values(by=[sort_by, 'song'], ascending=False).head(int(display))
    return merged_data


def output_display(filename: str, sort_by: str, display: str) -> DataFrame:
    """output_display creates and returns a sorted dataframe according to argument specifications."""

    pd.set_option('display.max_columns', None)  # display all columns and not truncate the dataframe if too many columns

    top_songs_df: pd.DataFrame = pd.read_csv(filename)
    answer: pd.DataFrame = top_songs_df.groupby(['artist', 'song', 'year', sort_by], as_index=False).size().sort_values(
        by=[sort_by, 'song'], ascending=False).head(int(display))
    answer.drop(['size'], inplace=True, axis=1)

    return answer


def input_file(filename: str):
    """input_file reads the file argument"""

    try:
        file_input = open(filename, mode='r')
        return file_input
    except FileNotFoundError:
        print("Error in opening file")
        return None


def output_file(filename: str):
    """output_file writes to the output.csv file."""

    try:
        file_input = open(filename, mode='w', newline='')
        return file_input
    except FileNotFoundError:
        print("Error in opening file")
        return None

if __name__ == '__main__':
    main()
