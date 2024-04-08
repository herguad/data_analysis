# What's the distribution of nationalities for movies included in Netflix library?

# Importing packages for manipulation and visualization
import pandas as pd
import matplotlib.pyplot as plt
#import numpy as np
import seaborn as sns

# Import the AWOC package.
import awoc
# Initialize the AWOC class.
my_world = awoc.AWOC()
# Let's retrieve the full list of nations of Europe.
countries_of_africa=my_world.get_countries_list_of('Africa')
countries_of_south_america=my_world.get_countries_list_of('South America')
countries_of_north_america=my_world.get_countries_list_of('North America')
countries_of_asia=my_world.get_countries_list_of('Asia')
countries_of_europe = my_world.get_countries_list_of('Europe')
countries_of_oceania=my_world.get_countries_list_of('Oceania')

# Read in the Netflix CSV as a DataFrame
netflix_df = pd.read_csv("netflix_data.csv")
# Subset the DataFrame for type "Movie"
netflix_subset = netflix_df[netflix_df["type"] == "Movie"]

#Distribution per continent
# Subset the DataFrame for type "country". Filter NaNs.
netflix_subset_c_noNaN = netflix_subset["country"].dropna()
netflix_countries_filtered=pd.DataFrame(netflix_subset_c_noNaN)
netflix_nat_year=netflix_countries_filtered.merge(netflix_subset, on="country",how="left")
movies_col_select=netflix_nat_year[['country','date_added','genre']]
movies_col_select['date_added']=pd.to_datetime(movies_col_select['date_added'])
movies_col_select['date_added']=movies_col_select['date_added'].dt.year  #Ignore warning but read: https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#returning-a-view-versus-a-copy
movies_grouped_sum=movies_col_select.groupby(["country","date_added"]).value_counts(ascending=True).reset_index(name='movies_per_countryear')

#Distribution per year and continent

netflix_countries=movies_grouped_sum.drop_duplicates(subset="country",keep='first',ignore_index=True)[["country"]]
#Make dictionary using awoc lists of contientns and countries and country column from netflix df
continents_countries={}

#Visualizing the distributions and finding the most and least represented nationalities in Netflix library.
