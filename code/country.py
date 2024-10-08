#Analyse total number of movies released per country and continent
import pandas as pd
import matplotlib.pyplot as plt
#import numpy as np
import seaborn as sns

# Import the AWOC package.
import awoc
# Initialize the AWOC class.
my_world = awoc.AWOC()
# Retrieve the full list of nations of Europe.
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
movies_country_tot=tot_movies_country.rename(columns={"country":"movie_count"})

#What are the max numbers of total movies released and their countries?
movies_country_tot=movies_country_tot.sort_values(by="movie_count",ascending=False).reset_index()
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
        print(i)
        index_= movies_country_tot.loc[movies_country_tot['country'] == i].index
        print(index_) #Clean miscategorized <---<---<---<--- United Arab West Germany Soviet Union

#print(movies_country_tot.head())

#Add an empty 'continent' column to the movies_country_tot df.
movies_country_tot['continent']=['' for i in range(0,74)]

#Loop over the country column, for each country, search within the dictionary items to check for matches. Where a match is found, consider the rows index for the df value, slice the df for that row and 'country' column. Finally, assign the corresponding continent name to the country as a value for the column 'continent'.
for i in movies_country_tot['country'].values:
    for k,v in continents_country.items():
        if i in v:
            index_i= movies_country_tot.loc[movies_country_tot['country'] == i].index
            movies_country_tot.iloc[index_i,2]= k
        else:
            continue

#print(movies_country_tot)

###DROP currently inexistent countries.
movies_country_tot=movies_country_tot.drop(index=[28,63,67])
#print(movies_country_tot)

movies_counts=movies_country_tot.groupby('continent')['movie_count'].agg(['sum','mean']).reset_index()
#print(movies_counts)

movies_counts['mean']=round(movies_counts['mean'])
movies_counts=movies_counts.sort_values(by='sum',ascending=True)
print(movies_counts.head(4))

sns.set(font_scale=1)

palette1=sns.color_palette('deep', n_colors=6)
fig2=sns.barplot(data=movies_counts,x="continent",y= "sum", hue='sum',palette=palette1)
fig2.set(yscale="log")
plt.xlim(-1,6)
plt.ylim(1000,4600000)
fig2.set(xlabel="Continent",ylabel="Total sum of movies added per continent")
fig2.tick_params(labelsize=8)
plt.show()

#Mean movies count per continent
palette2=sns.color_palette('colorblind', n_colors=6)
fig3=sns.barplot(data=movies_counts,x="continent",y= "mean", hue='mean',palette=palette2)
fig3.set(yscale="log")
plt.xlim(-1,6)
plt.ylim(500,950000)
fig3.set(xlabel="Continent",ylabel="Mean movies added per continent")
fig3.tick_params(labelsize=8)
plt.show()

#Drop USA row to get better scales plots fro all the rest of the countries.
movies_country_tot=movies_country_tot.drop([0,])

sns.set(font_scale=0.85)
palette3=sns.color_palette('muted', n_colors=6)
fig4=sns.catplot(data=movies_country_tot,x='movie_count',y='country',kind='bar',errorbar='ci',col='continent',col_wrap=2,hue='continent',palette=palette3)
fig4.set(xscale="log")
plt.ylim(-1,75)
fig4.set(ylabel="Country",xlabel="Total movies added")
fig4.tick_params(labelsize=6,rotation=75)
plt.show()
