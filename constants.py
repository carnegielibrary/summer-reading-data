
WORKSPACE_PATH = "C:\\Users\\kowaleskim\\Desktop\\Workspace\\test_workspace"

TIMEOUT = 600
#max number of seconds each cell is allowed to run
#current timeout is 10 minutes
#increase for large datasets

DEBUG_FUZZY_MATCHING = True
#if true, this won't print anything to the terminal when you run main.py
#but if you open clustering_3_executed.ipynb you can see the printed deubgging messages

ORDER_BOOKS_BY_READERS = True
#if True, orders both books within clusters and lists of clusters by number of "readers"
#(i.e. # entries for book in that cluster)
#if False, orders but number of times read instead
#(some entries have multiple reading couts in them)

AUTH_CONF_CUT = 70
FULL_TITLE_CONF_CUT = 60
PARTIAL_TITLE_CONF_CUT = 70
FULL_TITLE_CONF_CUT_NO_AUTHOR = 85
PARTIAL_TITLE_CONF_CUT_NO_AUTHOR = 90
#cutoffs for book matching
#higher <-> more restrictive
#see clustering_3.ipynb