import pandas as pd
from constants import WORKSPACE_PATH

"""
def path(subfolder, name):
    return WORKSPACE_PATH + "\\" + subfolder + "\\" + name + ".csv"

def read_csv(subfolder, name):
    return pd.read_csv(
                path(subfolder, name),
                index_col=0,
                 
                #this is necessary because the pandas export to csv function creates a csv of this encoding
                #but this encouding is not the default for pandas import csv
                #which is weird but ok
                encoding = "ISO-8859-1",
                 
                #these last two options are so that it doesn't interpret
                #empty string input as a NaN, so that all elements in
                #the title and author columns are actually strings
                na_values=[],
                keep_default_na=False)
    
def to_csv(df, subfolder, name):
    df.to_csv(path(subfolder, name))
"""    
    
def path(name):
    return WORKSPACE_PATH + "\\" + name + ".csv"

def read_csv(name):
    return pd.read_csv(
                path(name),
                index_col=0,
                 
                #this is necessary because the pandas export to csv function creates a csv of this encoding
                #but this encouding is not the default for pandas import csv
                #which is weird but ok
                encoding = "ISO-8859-1",
                 
                #these last two options are so that it doesn't interpret
                #empty string input as a NaN, so that all elements in
                #the title and author columns are actually strings
                na_values=[],
                keep_default_na=False)
    
def to_csv(df, name):
    df.to_csv(path(name))