# Movie Box Office Success Analysis

The movie industry represents the reflection of social, cultural and economical dynamics of the community across time. In this project of mine, I will aim to analyze how box office statistics changed over the years within enhancing film industry, and what factors (such as title, release year, genres, the total budget invested in the movie, IMDb ratings, the cast of the movie) influenced the overall success of movies.



## Research Question

How the factors such as budget, cast of the movie, IMDb ratings and genre best determines the movie's box office overall success in terms of total revenue?



Datas and Sources

For ratings, genres, cast, crew --> https://datasets.imdbws.com

For budget + worldwide box office --> https://www.the-numbers.com/

For revenue statistics --> https://www.boxofficemojo.com



For enrichment source - cast popularity --> https://developers.themoviedb.org/3



Data Collection

Download IMDb TSV datasets

Scrape The Numbers budget + box office values using Python

Query TMDb API to obtain cast popularity features for each film.


FILTERS - Does the data consist of what?

Year = 1995-2024
Only consist of movies.
Movies for adults.
Having 1000 or more vote in IMDb.


Until 30th of November, i have collected datas related to genres, IMDb ratings and budget and merged them into one table. I also did some EDA on the last excel document which has revenues.I applied two hypothesis tests on it. After the deadline i will complete the table with cast popularity features and see how does that affect the box office revenues.
