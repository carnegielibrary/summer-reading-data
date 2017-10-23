#summer-reading-data

###**Please visit [our organization page on WPRDC](https://data.wprdc.org/organization/carnegie-library-of-pittsburgh) to access Carnegie Library of Pittsburgh open data or submit an open data request.**

## What is Summer Reading?

To celebrate the city's 90 neighborhoods, Carnegie Library of Pittsburgh challenges readers to log 90,000 items between May 24 and August 31. Books, audiobooks, magazines - it all counts. Sign up, read, and win prizes!

[https://carnegielibrary.org/summer](https://carnegielibrary.org/summer)

## How are books logged? Where does this data come from? What are the limitations?

Readers can earn prizes and contribute to the shared 180,000 items goal by logging books online. Readers self-report the title, author, the date they read the item, and how many times they read the item (for example, a child might read the same book twice in a row at bedtime or a teacher might read a book to a class of 20 children, counting as 20 "reads.") This data does not represent everything Pittsburgh is reading - only what readers are logging. Additionally, readers may skip fields, capitalize or spell titles and authors differently, etc. This data is also NOT circulation data - a library item might be checked out and never logged, or a book from home might be read and logged.

The best way to get a sense of where the data comes from is to sign up and log a book yourself! You can log any book/audiobook/magazine you have read this summer.

[https://carnegielibrary.org/summer](https://carnegielibrary.org/summer)

Books logged totals may not be the same across datasets for a variety of reasons, including missing data in certain fields and/or reports being run at different times.

**In case you are curious, the current official total as of 10/23/2017 is 184,376 items read. We're beat 180,000!**

## How does book clustering work?

### clustering_1.ipynb

In this jupyter notebook, we will clean the self-reported summer reading data in an attempt to make the titles and authors more comparable and remove unusable entries.

### clustering_2.ipynb

In this jupyter notebook, we will query the openlibrary database in an attempt to match books in the database with cleaned user-entered data from part 1. The openlibrary search function is pretty picky, so there will be a lot of data that won't be matched, but this will provide a good base to build the book clusters on in part 3.

### clustering_3.ipynb

In this jupyter notebook, we use fuzzy matching algorithms to further cluster the match books from the prvious part, and incorporate the unmatched books as well.

### main.py

A wrapper python file that runs all the jupyter notebooks

### constants.py

Contains constants that affect all notebooks.

### bookslogged.csv

A sample dataset of logged books for testing.  Replace with your own book dataset!
