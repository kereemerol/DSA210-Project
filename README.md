# Movie Box Office Success Analysis


## Project Proposal

The movie industry represents the reflection of social, cultural and economical dynamics of the community across time. In this project, we will aim to analyze how box office statistics changed over the years within enhancing film industry, and what factors (such as title, release year, genres, the total budget invested in the movie, IMDb ratings) influenced the overall success of movies.



## Research Question

How the factors such as budget, runtime, IMDb ratings and genre best determines the movie's box office overall success in terms of total revenue?



## Datas and Sources

For names, id, ratings, genres, runtime, released year --> https://datasets.imdbws.com

For budget + worldwide box office(gross) --> https://www.the-numbers.com/







## Data Collection

From datasets.imdbws.com, we downloaded title.basics.tsv.gz and title.ratings.tsv.gz in order to reach rating, genre, runtime etc..

We scraped The Numbers budget + box office values using Python.

The previous dataset has been enriched with gross and budget stats so as to analyze the factors which are having profound effect on box office revenues.




## FILTERS - Does the data consist of what?

Year = 1995-2024
Only consist of movies.
Movies for adults.
Having 1000 or more vote in IMDb.

## Until 30th of November
Until 30th of November, we have collected datas related to genres, IMDb ratings and budget and merged them into one table. I also did some EDA on the last excel document which has revenues. I applied two hypothesis tests on it. 

## Until 2nd of January

