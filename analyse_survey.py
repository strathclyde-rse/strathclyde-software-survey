#!/usr/bin/env python
# encoding: utf-8

import pandas as pd
import matplotlib
# You have to use this library to sidestep a problem with Python not being installed as a framework
# on a Mac
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import numpy as np
import math

# Get details for plots from look up table
from column_name_renaming import col_shortener
from column_name_renaming import sort_no_further_analysis
from column_name_renaming import yes_no_analysis
from column_name_renaming import add_an_other_category


DATAFILELOC = "./data/"
DATAFILENAME = "Cleaning-of-Uni-Soton-Software-Survey-26Jun19.csv"
CSVSTORE = "./output_csv/"


def import_csv_to_df(location, filename):
    """
    Imports a csv file into a Pandas dataframe
    :params: an xls file and a sheetname from that file
    :return: a df
    """
    
    return pd.read_csv(location + filename)


def export_to_csv(df, location, filename, index_write):
    """
    Exports a df to a csv file
    :params: a df and a location in which to save it
    :return: nothing, saves a csv
    """

    return df.to_csv(location + filename + '.csv', index=index_write)


def clean_col_names(df):
    """
    Takes a dict from a look up file and uses it to rename the columns
    to something shorter and tidier
    :param df: the main df
    :return: the main df with new col names
    """

    return df.rename(index=str, columns=col_shortener)


def find_number_responses(df):
    """
    Finds the number of people who responded to each question and save it as a csv
    :param df: the main dataframe
    :return: nothing
    """

    for current_col in df.columns:
        temp_df = df.dropna(axis=0, subset=[current_col])
        print(current_col)
        print(len(temp_df))


    return


def get_counts(df):
    """
    Get summary dataframes. Where needed split up the multiple answer responses so that they fall into simple bins.
    :param df: the main df
    :return: dict of dfs holding summaries on the answers to each question
    """

    # Initiailise a dict into which I shall store the results dfs
    summary_dfs = {}

    # Go through each col, get the counts of each question, calculate a percentage and then store as a result df
    for current_col in df.columns:
        df_counts = pd.DataFrame(data = (df[current_col].value_counts(sort=False)), columns = [current_col])
        # Shift the index into a new column needed for the next bit
        df_counts['answers'] = df_counts.index
        # Multi-choice questions provide multiple answers separated by semicolon. Need to separate these up and count
        # them individually. The method I use (with Stack etc) below fails on answers that are numeric, so I filter them
        # out. Obviously, anything with a semicolon in it is not numeric!
        if df_counts['answers'].dtype == 'object':
            df_counts = (df_counts.set_index(current_col)['answers'].str.split(';', expand=True).stack().reset_index(name='answers').groupby('answers', as_index=False)[current_col].sum())
        df_counts.set_index('answers', inplace=True)
        df_counts['percentage'] = round(100 * df_counts[current_col] / df_counts[current_col].sum(), 0)
        # Save as dict of dfs
        summary_dfs[current_col] = df_counts

    return summary_dfs


def change_lows_to_other(summary_dfs):
    """
    Questions with an "other" response can generate lots of low value responses. Shifting these into an "other"
    category makes it easier to present the data
    :param summary_dfs: dict of dfs holding summaries on the answers to each question
    :return: dict of dfs holding summaries on the answers to each question - but with an other response used to mop up
             ansewrs with low response numbers
    """


    return summary_dfs


def sort_and_save(summary_dfs):
    """
    Takes the summary dfs that merely need sorted and saves them out as csvs
    Uses info from the sort_no_further_analysis var to know which dfs to process
    :param summary_dfs: dict of dfs holding summaries on the answers to each question
    :return: nothing
    """

    for key in sort_no_further_analysis:
        df_temp = summary_dfs[key]
        df_temp.sort_values(by='percentage', inplace=True, ascending=False)
        export_to_csv(df_temp, CSVSTORE, key, True)
    return


def yes_and_no(summary_dfs):
    """
    Takes summary dfs of yes-and-no questions, sorts them yes first, then no, then saves the csv
    Uses the yes_no_analysis var to work out which dfs to process
    :param summary_dfs: dict of dfs holding summaries on the answers to each question
    :return: nothing
    """

    for key in yes_no_analysis:
        df_temp = summary_dfs[key]
        # Sorting an index of 'yes' and 'no' in descending order is the same as ensuring that yes comes first
        # which is what I want
        df_temp.sort_index(inplace=True, ascending=False)
        export_to_csv(df_temp, CSVSTORE, key, True)

    return


def main():
    """
    Main function to run program
    """

    df = import_csv_to_df(DATAFILELOC, DATAFILENAME)

    df = clean_col_names(df)

    find_number_responses(df)

    summary_dfs = get_counts(df)

    summary_dfs = change_lows_to_other(summary_dfs)

    # Prepare data for graphing programs

    sort_and_save(summary_dfs)

    yes_and_no(summary_dfs)


if __name__ == '__main__':
    main()
