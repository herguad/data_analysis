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

#Add different dfs selecting year_added and country.
movies_country_year=movies_col_select.loc[:,('country','year_added')]

#Group movies by country and year added, and count movies added per year. 
movies_c_y_sum=movies_country_year.groupby(["country","year_added"]).value_counts(ascending=True).reset_index(name='movies_per_countryear')

# Select years where the max number of movies were released for each country. Filter out countries with max movies < 50. Sort by count in descending order.. Few countries in this list are below 50, so increase filter limit to >200.
max_movies_per_c_y= movies_c_y_sum.groupby("country").max().sort_values("year_added")

max_movies_over200= max_movies_per_c_y[max_movies_per_c_y["movies_per_countryear"] >= 200].sort_values("movies_per_countryear", ascending=False) #--> down to 23 countries out of 74
max_movies_over200=max_movies_over200.reset_index()
#print(max_movies_over200)

#Visualize distribution of max movies released per year per country --> not very informative: sns.scatterplot(data=max_movies_per_c, x="year_added", y="movies_per_countryear") plt.xlim(2015,2024) plt.ylim(0,6100) plt.show()
#Visualize distribution of max movies released per year per country (after selection). --> Needs subselection to get good visuals: sns.scatterplot(data=max_movies_select, x="year_added",y="movies_per_countryear"). 
# Most movies were released in 2020 and 2021, so 'year added' should be included as hue categorically, i.e. w/catplot or relplot.
fig1=sns.relplot(data=max_movies_over200,x="country",y= "movies_per_countryear", col="year_added", kind="scatter",hue="year_added",palette=sns.color_palette('colorblind', n_colors=2))
fig1.set(yscale="log")
plt.xlim(-1,25)
plt.ylim(400,1500000)
fig1.set_xticklabels(rotation=90)
fig1.set(xlabel="Country",ylabel="Max number of movies added that year")
plt.show()


## The facetted plot shows a correlation between year_added and nationalities such that in 2020 half the countries were included for releases in 2020 and the other half in 2021. We can check this, manually, by selecting the rows of df  fro each year_added:
added_2020=max_movies_over200[max_movies_over200["year_added"]==2020] #.shape shows 12 distinct countries
added_2021=max_movies_over200[max_movies_over200["year_added"]==2021] #.shape shows 11 distinct countries


#Distribution per year and continent

#Make dictionary using awoc lists of contienents and countries and country column from netflix df (which is the index, so first, reset index)
max_2020_movies=added_2020.reset_index().rename(columns={"movies_per_countryear":"movies_per_country_2020"}).drop(columns=["year_added","index"])
max_2021_movies=added_2021.reset_index().rename(columns={"movies_per_countryear":"movies_per_country_2021"}).drop(columns=["year_added","index"])

keys_set = ['Africa','Asia','Europe','N_America','S_America','Oceania']

continents_country={key : [] for key in keys_set}

for i in max_2020_movies["country"]:
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
        print('Mystery')


for i in max_2021_movies["country"]:
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
        print('Mystery')

#print(max_2020_movies,max_2021_movies)
#Repetir continent adding con estas dfs para hace un recorte lupa de movies_country para los años 2020 y 2021 (años de maximas incorporaciones)

#Visualize movies count per continent with distinct colors for each year.
