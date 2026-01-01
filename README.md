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

By the end of November, the primary focus of the project was data collection, preprocessing, and exploratory data analysis. IMDb datasets were downloaded from datasets.imdbws.com, specifically title.basics.tsv.gz and title.ratings.tsv.gz, in order to obtain movie-level information such as titles, release years, runtimes, genres, IMDb ratings, and vote counts.

In addition to IMDb metadata, production budget and worldwide box office gross revenue data were collected from The Numbers website using Python-based web scraping techniques. These financial variables were then merged with the IMDb datasets using movie titles and release years, resulting in a consolidated dataset that combines both movie characteristics and box office performance indicators.

## Until 2nd of January
In this stage of the project, machine learning techniques were applied to the finalized dataset in order to analyze and predict movie box office performance. The dataset included production budget, IMDb rating, IMDb vote count, release year, and worldwide box office gross revenue. Prior to modeling, the data was cleaned by removing missing and non-positive values, and logarithmic transformations were applied to highly skewed variables such as budget, revenue, and vote count.

## REPORT

A Linear Regression model was first implemented as a baseline approach. The model achieved an R² score of approximately 0.61, indicating a strong linear relationship between the selected predictors and box office revenue. The results suggest that production budget and audience engagement play a significant role in explaining box office success.

To capture potential non-linear relationships, a Random Forest Regression model was also applied. Although the Random Forest model did not outperform the linear model in terms of R², it provided valuable insights through feature importance analysis. The results showed that IMDb vote count (audience engagement) was the most influential predictor, followed by production budget, while IMDb rating and release year contributed smaller but positive effects.
