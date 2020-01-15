
# Copyright (c) 2020 Alexandre Quenon - UMONS

"""
Get data from files and dump them into a container, and vice-versa.
"""



# Filesystem management
from pathlib import Path

# GUI-access method
from tkinter import Tk
from tkinter.filedialog import askopenfilename

# Pandas to dump data into Dataframe
import pandas as pd


# Mid-level opening file functions
def open_file_gui():
    Tk().withdraw()
    target_file = askopenfilename()
    if target_file:
        target_file = Path(target_file)
        return read_file(target_file)
    else:
        raise FileNotFoundError("No file selected.")


def open_file_shell(path):
    target_file = Path(path)
    if target_file.is_file():
        return read_file(target_file)
    else:
        raise FileNotFoundError(path)


# Low-level file selector
def read_file(path):
    """
    Read a file and load data into a pandas.Dataframe if type is csv (';' separator only), xls or xlsx.
    """

    file_type = path.suffix

    if file_type == '.csv':
        return pd.read_csv(path, sep=';')
    elif file_type in ('.xls', '.xlsx'):
        return pd.read_excel(path)
    else:
        raise ValueError('The file type {} is not supported.'.format(file_type))
