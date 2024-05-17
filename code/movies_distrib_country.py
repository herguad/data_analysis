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
movies_country_tot=movies_country_tot.sort_values(by="movies_per_country",ascending=False)
#print(movies_country_tot.head())

#List continents, make a continents_country dictionary including only countries with movies in Netflix db.
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

#Add an empty 'continent' column to the movies_country_tot df.
movies_country_tot['continent']=['' for i in range(0,74)]

#Loop over the country column, for each country, search within the dictionary items to check for mathes. Where a match is found, consider the rows index for the df value, slice the df for that row and 'country' column. Finally, assign the corresponding continent name to the country as a value for the column 'continent'.
for i in movies_country_tot['country'].values:
    for k,v in continents_country.items():
        if i in v:
            index_i= movies_country_tot.loc[movies_country_tot['country'] == i].index
            movies_country_tot.iloc[index_i,2]= k
        else:
            continue
#print(movies_country_tot)

#Aggregate movies per continent in a new df. Sort df by sum for clearer plot.
movies_counts=movies_country_tot.groupby('continent')['movies_per_country'].agg(['sum','mean']).reset_index()
movies_counts=movies_counts.drop(movies_counts.index[0])
movies_counts['mean']=round(movies_counts['mean'])
movies_counts=movies_counts.sort_values(by='sum',ascending=True)

#Visualizing the distributions and finding the most and least represented nationalities in Netflix library.
#Movies count per continent
fig2=sns.barplot(data=movies_counts,x="continent",y= "sum", hue='sum',palette=sns.color_palette('deep', n_colors=6))
fig2.set(yscale="log")
plt.xlim(-1,6)
plt.ylim(1000,4600000)
fig2.set(xlabel="Continent",ylabel="sum")
fig2.tick_params(labelsize=8)
plt.show()

#Mean movies count per continent
fig3=sns.barplot(data=movies_counts,x="continent",y= "mean", hue='mean',palette=sns.color_palette('colorblind', n_colors=6))
fig3.set(yscale="log")
plt.xlim(-1,6)
plt.ylim(500,950000)
fig3.set(xlabel="Continent",ylabel="Mean")
fig3.tick_params(labelsize=8)
plt.show()


