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

movies_country_year=movies_col_select.loc[:,('country','year_added')]

#Group movies by country and year added, and count movies added per year. 
#Count total number of movies added by country
tot_movies_country=movies_country_year.groupby("country")[["country"]].count()
movies_country_tot=tot_movies_country.rename(columns={"country":"movies_per_country"})

#What are the max numbers of total movies released and their countries?
movies_country_tot=movies_country_tot.sort_values(by="movies_per_country",ascending=False)
#print(movies_country_tot.head())

keys_set = ['Africa','Asia','Europe','N_America','S_America','Oceania']

continents_country={key : [] for key in keys_set}

for i in movies_country_tot["country"]:
    if i in countries_of_africa:
        continents_country['Africa'].append(i)
    elif i in countries_of_asia:
        continents_country['Asia'].append(i)
    elif i in countries_of_europe:
        continents_country['Europe'].append(i)
    elif i in countries_of_north_america:
        continents_country['N_America'].append(i)
    elif i in countries_of_south_america:
        continents_country['S_America'].append(i)
    elif i in countries_of_oceania:
        continents_country['Oceania'].append(i)
    else:
        print('dunno')

#print(movies_country_tot.head())
countries_cont= pd.DataFrame.from_dict(continents_country,orient='index').reset_index().rename(columns={"index": "continent"}).transpose()
countries_cont.columns=countries_cont.iloc[0]
countries_cont=countries_cont.drop(countries_cont.index[0])
#print(countries_cont.columns)
movies_country_tot['continent']=['' for i in range(0,74)]

for i in movies_country_tot['country'].values:
    for k,v in continents_country.items():
        if i in v:
            index_i= movies_country_tot.loc[movies_country_tot['country'] == i].index
            movies_country_tot.iloc[index_i,2]= k
        else:
            continue
print(movies_country_tot)

#Visualizing the distributions and finding the most and least represented nationalities in Netflix library.



