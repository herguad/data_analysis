#What's the distribution of movie genres in Netflix library?

# Importing packages for manipulation and visualization
import pandas as pd
import matplotlib.pyplot as plt
#import numpy as np
import seaborn as sns

# Read in the Netflix CSV as a DataFrame
netflix_df = pd.read_csv("netflix_data.csv")
# Subset the DataFrame for type "Movie"
netflix_subset = netflix_df[netflix_df["type"] == "Movie"]

#Select columns of interest. Transform date column into datetype and extract year from dates and re-write cdate_added column to show just years.
movies_col_select=netflix_nat_year.loc[:,('country','date_added','genre')]
movies_col_select.loc[:,('date_added')]=pd.to_datetime(movies_col_select.loc[:,('date_added')])
movies_col_select['year_added']=movies_col_select['date_added'].values  #Ignore warning but read: https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#returning-a-view-versus-a-copy
movies_col_select['year_added']=movies_col_select['year_added'].dt.year

#Add different dfs selecting release_year and genre and genre and country separately
movies_country_genre_year=movies_col_select.loc[:,('country','genre','year_added')]
movies_genre_year=movies_col_select.loc[:,('genre','year_added')]
movies_country_genre=movies_col_select.loc[:,('country','genre')]

#Group movies by genre and year added, and count genres movies added per year. 
movies_g_y_sum=movies_genre_year.groupby(["genre","year_added"]).value_counts(ascending=True).reset_index(name='movies_per_genreyear')
print(movies_g_y_sum)
#Group movies by country andgenre, and count genres movies added per country. 
movies_g_c_sum=movies_country_genre.groupby(["country","genre"]).value_counts(ascending=True).reset_index(name='movies_per_countrygenre')
print(movies_g_c_sum)

#Find whether there's a correlation between genre and number of movies released each year . --> sns. heatmap
#Find whether there's a correlation between genre and country . --> sns. heatmap

