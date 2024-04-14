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

#Select columns of interest. Transform date column into datetype and extract year from dates and re-write cdate_added column to show just years.
movies_col_select=netflix_nat_year.loc[:,('country','date_added')]
movies_col_select.loc[:,('date_added')]=pd.to_datetime(movies_col_select.loc[:,('date_added')])
movies_col_select['year_added']=movies_col_select['date_added'].values  #Ignore warning but read: https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#returning-a-view-versus-a-copy
movies_col_select['year_added']=movies_col_select['year_added'].dt.year

#Add different dfs selecting release_year and country.
movies_country_year=movies_col_select.loc[:,('country','year_added')]

#Group movies by country and year added, and count movies added per year. 
movies_c_y_sum=movies_country_year.groupby(["country","year_added"]).value_counts(ascending=True).reset_index(name='movies_per_countryear')
#print(movies_c_y_sum)

# Select years where the max number of movies were released for each country. Filter out countries with max movies < 50
max_movies_per_c= movies_c_y_sum.groupby("country").max().sort_values("year_added")
max_movies_select= max_movies_per_c[max_movies_per_c["movies_per_countryear"] >= 50] #--> down to 37 countries out of 74

#Visualize distribution of max movies released per year per country --> not very informative: sns.scatterplot(data=max_movies_per_c, x="year_added", y="movies_per_countryear") plt.xlim(2015,2024) plt.ylim(0,6100) plt.show()

#Visualize distribution of max movies released per year per country (after selection). --> TBC
sns.scatterplot(data=max_movies_select, x="movies_per_countryear", y="country",hue="year_added",palette="deep")

plt.show()

#Distribution per year and continent

#netflix_countries=movies_grouped_sum.drop_duplicates(subset="country",keep='first',ignore_index=True)[["country"]]

#Make dictionary using awoc lists of contientns and countries and country column from netflix df
#continents_countries={}



#Visualizing the distributions and finding the most and least represented nationalities in Netflix library.
