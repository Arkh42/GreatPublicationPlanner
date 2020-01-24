
# Copyright (c) 2020 Alexandre Quenon - UMONS

"""
Process the data (integrity check, sort, filter) so that the drawer has always the same data format.
"""



import pandas as pd


# Data format: low-level functions
def make_lower_case_header(data):
    data.columns = map(str.lower, data.columns)

def convert_date_to_datetime(data):
    """
    Convert date into pandas.Timestamp.

    Initial type is str when dumping data from files into pandas.Dataframe.
    """
    
    data.start = pd.to_datetime(data.start)
    data.end = pd.to_datetime(data.end)
    data.submission = pd.to_datetime(data.submission)


# Data integrity check: low-level functions
def has_name(data):
    return 'name' in data.columns

def has_abbreviation(data):
    return 'abbreviation' in data.columns

def has_start_date(data):
    return 'start' in data.columns

def has_end_date(data):
    return 'end' in data.columns

def has_submission_date(data):
    return 'submission' in data.columns


# Data integrity check: high-level functions
def check_data_integrity(data):
    missing_fields = []

    if not has_name(data):
        missing_fields.append('name')
    if not has_abbreviation(data):
        missing_fields.append('abbreviation')
    if not has_start_date(data):
        missing_fields.append('start')
    if not has_end_date(data):
        missing_fields.append('end')
    if not has_submission_date(data):
        missing_fields.append('submission')
    
    if missing_fields:
        raise KeyError('Mandatory fields are missing in data: {}'.format(missing_fields))


# Sort functions
def sort_on_start_date(data, ascending=True):
    return data.sort_values(by='start', ascending=ascending)

def sort_on_submission_date(data, ascending=True):
    return data.sort_values(by='submission', ascending=ascending)
