#Analyse total number of movies released per country and continent
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
#Count total number of movies added by country
tot_movies_country=movies_country_year.groupby("country")[["country"]].count()
movies_country_tot=tot_movies_country.rename(columns={"country":"movies_per_country"})

print(movies_country_tot.head())


