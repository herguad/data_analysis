# Netflix data analysis

#<<DA \and Data Science>>#<br />

This is an analysis of Netflix database including a general analysis of Netflix movie trends in time and specific analysis of data subsets aimed at answering various questions about, e.g. trends in movies from South American countries and more.

This analysis started as an assignment in DataCamp aimed at putting into practice the basics of data exploration. Originally, the main question was 'Are movies getting shorter?' but 'maybe' was a satisfying enough answer to pass the assignment. 

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
A quick look over the shape, bsic info and first row of the df show +7 rows including info on genre, duration, release_year, cast and rating among the ten variables displayed as columns.

![netflix_df_info](https://github.com/user-attachments/assets/19fce985-6aa0-4782-b2a4-61ac544c3ef6)

To get an idea of how much cleaning is needed, I contrasted the length of the df with the counts for rows with NaN values, counted unique values for the variables and determined how to approach the cleaning. <br /> The complete analysis and validation of data types is [here](code/NaN_movies.py).<br />
Subset the df to only include those variables of interest. Here the analysis splits into ((NUMBER)) files corresponding with the main questions:
a. [distribution per duration](code/duration_years.py) 
b. [distribution per release_year](code/movies_release.py)
c. [distribution per country and continent](code/movies_distrib_country.py)
d. [distribution per genre](code/movies_distrib_genre.py)

To assess questions in 1/a, the df was subset by title, genre, release_year and duration. The movies under 60 minutes and over 250, together with the those marked as 'uncategorized' for genre, were filtered out. This dataset was initially visualized as two different scatterplots to get an idea of the distribution of movies duration in general and movies duration by genre.
![dur_rel_y](https://github.com/user-attach![dur_rel](https://github.com/user-attachments/assets/acab307a-ae68-4333-a383-dbb932a9276d)
ments/assets/61e50676-b859-4755-b0d9-63e2f74edd24)

>>> description of duration_time workflow <<<<
#### Visualizing relations between variables

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


