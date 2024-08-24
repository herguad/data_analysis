# Netflix data analysis
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

## Movies in general

### Are movies getting shorter? 
#### Explore a Netflix dataset to show how specific genres (documentaries, children movies and stand up specials) relate to movies release years and their duration. 
- After importing pandas and matplotlib.pyplot, read the .csv with the data and store it into a properly named df.
- Subset the df to only see data about movies (not documentaries, series, or else) and pick only those columns of interest, i.e. title, country, genre, year released and duration.
- Filter out movies shorter than an hour.
- Iterate over the rows and assign a color to each member in a subset of genres (perhaps the most popular overall, see movies_distrib_genre) and others. Inspect the list to check.
#### Visualize the results in a scatter plot to show whether duration and release year for these genres are correlated.
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

### Has Netflix been expanding the range of nationalities of movies in their library?

### Are the movies included in Netflix library evenly distributed by nationality?
- Finding the distribution of nationalities for movies included in Netflix library.
- Visualizing the distribution and finding the most and least represented nationalities in Netflix library.

## South American movies
### Are there changes in the distribution of nationalities of SouthA movies in Netflix in time?
- Finding the total number of movies from South American countries included in Netflix library.
- Visualizing the distribution and finding the most and least represented SouthAm countries in Netflix library.


