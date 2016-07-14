#summer-reading-data

**THE SUMMER READING DATA SHARED HERE IS EXPERIMENTAL.**

This data was compiled for an OpenPGH civic hack night. [http://www.meetup.com/Open-Pittsburgh-our-Regions-Code-for-America-Brigade/events/232205629/](http://www.meetup.com/Open-Pittsburgh-our-Regions-Code-for-America-Brigade/events/232205629/)

In accordance with Carnegie Library of Pittsburgh privacy policies, all personally identifiable information has been removed.

## What is Summer Reading?

To celebrate the city's 90 neighborhoods, Carnegie Library of Pittsburgh challenges readers to log 90,000 items between May 24 and August 31. Books, audiobooks, magazines - it all counts. Sign up, read, and win prizes!

[https://carnegielibrary.org/summer](https://carnegielibrary.org/summer)

## How are books logged? Where does this data come from? What are the limitations?

Readers can earn prizes and contribute to the shared 90,000 items goal by logging books online. Readers self-report the title, author, the date they read the item, and how many times they read the item (for example, a child might read the same book twice in a row at bedtime or a teacher might read a book to a class of 20 children, counting as 20 "reads.") This data does not represent everything Pittsburgh is reading - only what readers are logging. Additionally, readers may skip fields, capitalize or spell titles and authors differently, etc. This data is also NOT circulation data - a library item might be checked out and never logged, or a book from home might be read and logged.

The best way to get a sense of where the data comes from is to sign up and log a book yourself! You can log any book/audiobook/magazine you have read this summer.

[https://carnegielibrary.org/summer](https://carnegielibrary.org/summer)

Books logged totals may not be the same across datasets for a variety of reasons, including missing data in certain fields and/or reports being run at different times.

**In case you are curious, the current official total as of 7/13/2016 is 53,245 items read. We are well on our way to 90,000!**

## What data is included here?

### log_timestamps.csv

Timestamps showing when books were logged. Book titles are not included in this dataset, since book titles and timestamps combined could theoretically create a "reader fingerprint" as some readers log their books all at once.

- log_timestamp - The time the book was logged in Eastern Time.
- date_read - The date the book was read, if the reader indicated a different date than the timestamp.
- log_value - The number of times the book was read. For example, a child might read a picture book twice before bedtime, or a teacher might read to a group of twenty children at once during a storytime and choose to log that reading all at once.
- library - The library the reader is registered with for summer reading. While many people use multiple libraries, this would be considered their "home base."

### log-books.csv

A list of all the books titles that have been logged.

- book_title - The book title. Note that capitalization and spelling may be inconsistent. Additionally, note that many readers have chosen not to self-report their book title. A missing title appears as "No Title Logged."
- book_author - The book author. A missing author appears as NULL.
- log_value - The number of times the book was read.
- library - The library the reader is registered with for summer reading.

### total-by-library.csv

The total number of items logged aggregated by library.

- library - The library the reader is registered with for summer reading.
- books - The number of books logged.

### total-by-zip.csv

The total number of items logged aggregated by ZIP code.

- zip - The ZIP code the reader lives in. ZIP codes with fewer than 50 books logged were omitted from the list (as well as any invalid ZIP codes.)
- books - The number of books logged.

## What other resources are available?

Besides the experimental summer reading data in this repository, there are a number of datasets and tools that might be useful during this hack night.

- Carnegie Library locations on WPRDC: [https://data.wprdc.org/dataset/libraries](https://data.wprdc.org/dataset/libraries)
- Allegheny County ZIP Code Boundaries on WPRDC: [https://data.wprdc.org/dataset/allegheny-county-zip-code-boundaries](https://data.wprdc.org/dataset/allegheny-county-zip-code-boundaries)
- WPRDC (open data that could be interesting to look at in conjunction with summer reading data or library locations): [http://www.wprdc.org/](http://www.wprdc.org/)
- Twitter discussions related to Summer Reading:
  - Carnegie Library of Pittsburgh: [https://twitter.com/carnegielibrary](https://twitter.com/carnegielibrary)
  - #PGHREADS: [https://twitter.com/search?q=%23PGHREADS&src=typd](https://twitter.com/search?q=%23PGHREADS&src=typd)
  - #MyNextRead (book recommendations): [https://twitter.com/search?q=%23MyNextRead&src=typd](https://twitter.com/search?q=%23MyNextRead&src=typd)
- [CODEX Hackathon](http://codexhackathon.com/) in depth list of reading-related tools, APIs, and datasets: [https://docs.google.com/document/d/1nyN4rn1oFhcXs95N8gixruNc3XiOnSSx12j_p8AP1as/](https://docs.google.com/document/d/1nyN4rn1oFhcXs95N8gixruNc3XiOnSSx12j_p8AP1as/)

## How can we use this data to understand and imagine the future of reading in our community?

This data is experimental and this is a hack night - so have fun and be creative!

To get you started, here are some possible questions to explore - perhaps some of them will lead to more questions:

- What times of day or days of the week does book logging occur? Does this vary across library locations? Are there early birds or night owls?
- Based on the daily log counts, can we predict when we will hit 90,000 books?
- What book titles are the most popular at different libraries? Are there surprising titles or genres that the library should be featuring based on this data?
- Using the list of books read alongside other tools or APIs from the CODEX list, are there #MyNextRead recommendations that would be appropriate for Pittsburgh Summer Readers as a group? (Of course, our librarians can make personalized recommendations for any reader!)
- Carnegie Library of Pittsburgh recently joined the Western Pennsylvania Regional Data Center. Our organization page can be found at [https://data.wprdc.org/organization/carnegie-library-of-pittsburgh](https://data.wprdc.org/organization/carnegie-library-of-pittsburgh). Looking forward, what data would you like to see us open and how would it be useful to you?
