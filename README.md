# Data Analysis: the Netflix database

This is an analysis of a freely available Netflix database exploring movie trends in time and including a specific analysis of data subsets aimed at answering various questions about, e.g. trends in movies genre, origin, duration and more.

This analysis started as an assignment in DataCamp meant as practice of data exploration. Originally, the main question was 'Are movies getting shorter?'.

Once I began transcribing that project here, many questions came to mind. To the original question, I've added the following.
1. Focusing on movie duration
- Would it be justified to correlate movie duration and year of release? 
- What about duration and genre? Is genre correlated to duration?
2. Focusing on genre
- Which genres got the most movies released in different years?
- Which were the top 3 genres for movies released in different years?
3. Focusing on countries and continents
- Which countries have the most released movies in different years? And which ones have the least?
- What can be said about the gretaer and smaller number of releases per continent?
- How are the different continents represented as proportions of the total movies released each year?
4. 'Historical' analysis
- How are the different genres distributed in time?
- Which genres have gained relevance or lost it?
- Has the distribution of movies changed in relation to continent and countries diversity?

Below, I present the ((basic)) insights derived from observing possible relations between relevant features of the datasaet and the tools and methods I used to that aim.
## 1. Movie duration
### Are movies getting shorter? 
#### Exploring the dataset
After importing the encessary libraries and packages, I loaded the dataset and stored it into a properly named df.

```python
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

#Load netflix_data.csv as a DataFrame
netflix_df = pd.read_csv(r'pathway\netflix_data.csv')
```
A quick look over the shape, basic info and first row of the df show +7 rows including info on genre, duration, release_year, cast and rating among the ten variables displayed as columns.

![netflix_df_info](https://github.com/user-attachments/assets/cb591c1c-9f93-48ee-8649-fff3529309da)

To get an idea of how much cleaning is needed, I contrasted the length of the df with the counts for rows with NaN values, counted unique values for the variables and determined how to approach the cleaning. <br /> The complete analysis and validation of data types is [here](code/NaN_movies.py).<br />
Subset the df to only include those variables of interest. Plot the data to look for possible outliers.

<p align="center">
<img src="https://github.com/user-attachments/assets/c4d5e02e-9f12-4a26-af17-f2d42a5c0f5b">
</p>

Here the analysis splits into ((NUMBER)) files corresponding with the main questions:
a. [distribution per duration](code/duration_years.py) 
b. [distribution per release_year](code/movies_release.py)
c. [distribution per country and continent](code/movies_distrib_country.py)
d. [distribution per genre](code/movies_distrib_genre.py)

To assess questions in 1/a, the df was subset by title, genre, release_year and duration. The movies under 60 minutes and over 180, together with the those marked as 'uncategorized' for genre, were filtered out. This dataset was initially visualized as two different scatterplots to get an idea of the distribution of movies duration in general and movies duration by genre.<br />

<p align="center">
<img src="images/dur_rel_filt.png">
</p>

<p align="center">
<img src="images/dur_rel.png">
</p>

To get a clearer idea of the distribution, the mean for the dataset was plotted using seaborn and specifing the hue argument for 'genre'.
<p align="center">
<img src="images/mean_dur_genre.png">
</p>

While there seems to be a tendency of movies on Netflix to be shorter in time, only a proper statistical analysis taking into account all relevant variables could yield a meaninful answer to the question whether movies overall have been getting shorter. As rergards the question about possible correlations between genres and duration of the movie, the barplot showing mean duration of the movie per genres shows clear differences between all the genres consider in general and specifically between, for example, action movies or dramas, and documentaries or children's movies.

## 2. Movie genre
Moving on with genres in particular, the first cleaning and filtering provides a proper dataset to start analysing the distribution and possible correlations between movie genre and other variables. In this case, apart from the 'uncategorized' genre, the 'International Movies' values are also filtered out to avoid vague categories representing only a small proportion of total values. 


- Which genres got the most movies released in different years?
- Which were the top 3 genres for movies released in different years?

Visualize the results in a scatter plot to show whether duration and release year for these genres are meaningfully* related.
- Create a fig with appropriate style, size, edges, etc.
- Plot duration vs release year. Scatterplot is good to see possible correlations overall.
- Set titles and labels to the plot and show it.
  
### What is the distribution of added movies per genre? What are the top genres for movies added in the library?
- Select and clean the data.
- Count number of movies per genre added to Netflix library.
- Plot total sums per genre and select those with sums over median (pop genres).
- Plot pop genres counts per genre.

### Has Netflix been expanding the range of genres of movies in their library?

- Perform general data analysis to see which years saw the greatest increase in added movies to Netflix library.
- Analyse a subset of the data for those years (2020, 2021) to get idea of trends these past years.
- Analyse the dataset and find out what the general distirbution is for movies of different continents.

## 3. Countries and continents
### Has Netflix been expanding the range of nationalities of movies in their library?

### Are the movies included in Netflix library evenly distributed by nationality?
- Finding the distribution of nationalities for movies included in Netflix library.
- Visualizing the distribution and finding the most and least represented nationalities in Netflix library.
- 
### Are there changes in the distribution of nationalities of SouthA movies in Netflix in time?
- Finding the total number of movies from South American countries included in Netflix library.
- Visualizing the distribution and finding the most and least represented SouthAm countries in Netflix library.


