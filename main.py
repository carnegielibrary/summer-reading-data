import nbformat
from nbconvert.preprocessors import ExecutePreprocessor
from constants import *
import os.path

def execute_notebook(name):

    with open(WORKSPACE_PATH + "\\" + name + ".ipynb") as f:
        nb = nbformat.read(f, as_version=4)
    
    ep = ExecutePreprocessor(timeout=TIMEOUT)
    #max number of seconds each cell is allowed to run
    #current timeout is 10 minutes
    #increase for large datasets

    #run notebook
    ep.preprocess(nb, {'metadata': {WORKSPACE_PATH: 'notebooks/'}})
    
    #write reslts to file as "[notebookname]_executed"
    with open(WORKSPACE_PATH + "\\" + name + "_executed.ipynb", 'wt') as f:
        nbformat.write(nb, f)

def file_exists(filename):
    return os.path.isfile(WORKSPACE_PATH + "\\" + filename)


if (file_exists("book_df.csv") and
        file_exists("cluster_df.csv")): 
    print("book_df.csv and cluster_df.csv already exist.  executing no notebooks.")
else:
    if file_exists("matchedbooks.csv"): 
        print("matchedbooks.csv already exists.  executing only clustering_3.")
    else:
        if file_exists("bookslogged_clean.csv"): 
            print("bookslogged_clean already exists.  executing only clustering_2 and clustering_3.")
        else:
            if not file_exists("bookslogged.csv"): raise Exception("bookslogged.csv does not exist in workspace folder!")
            print("executing clustering_1")
            execute_notebook("clustering_1")
            print("clustering_1 complete.")
        print("executing clustering_2")
        execute_notebook("clustering_2")
        print("clustering_2 complete.")
    print("executing clustering_3")
    execute_notebook("clustering_3")
    print("clustering_3 complete.")


