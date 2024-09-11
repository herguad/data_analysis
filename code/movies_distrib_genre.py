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
movies_col_select=netflix_subset.loc[:,('country','date_added','genre')]
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

#Group movies by country and genre, and count genres movies added per country. 
movies_g_c_sum=movies_country_genre.groupby(["country","genre"]).value_counts(ascending=True).reset_index(name='movies_per_countrygenre')
print(movies_g_c_sum)

#Count uncategorized movies and remove/display on their own (by country and by year). Add to NaN Movies file.
#Stats based on years when movies were added
uncategorized_s=movies_g_y_sum[movies_g_y_sum['genre']=='Uncategorized']['movies_per_genreyear'].sum()
uncategorized=movies_g_y_sum[movies_g_y_sum['genre']=='Uncategorized']
#print(len(uncategorized))
#Separate international movies into a different df and remove from main.
international_movies_g= movies_genre_year[movies_genre_year['genre']=='International Movies']
#print(international_movies_g.index)
movies_genre_year=movies_g_y_sum.drop(index=[74, 75, 76, 77, 78, 79,107,108,109,110,111,112,113]).reset_index(drop=True)

#print(movies_genre_year) #--> check n of rows is 13 down.

#print(movies_genre_year['genre'].unique()) # <- 18 distinct genres after cleaning

#Visualize movies_per_genreyear.
palette=sns.set_palette('bright',n_colors=18)
fig7=sns.scatterplot(movies_genre_year,x='year_added',y='movies_per_genreyear',size='movies_per_genreyear',palette=palette,hue='genre',legend=False)
fig7.set(xlabel="Year",ylabel="Total movie count per year")
fig7.set(title="Movies of different genres added per year")
fig7.tick_params(labelsize=9)
plt.show()

#Filter years with over 8 movies added, which is the 2nd quartile as shown by describe(). Remove rows with genre 'International Movies'.
#print(round(movies_genre_year['movies_per_genreyear'].describe(),2))
filtered_genre_year=movies_genre_year[movies_genre_year['movies_per_genreyear']<8]
filtered_gindex=filtered_genre_year.index
#print(filtered_gindex)
filtered_genre_year=movies_genre_year.drop(index=[0,   1,   8,   9,  10,  11,  13,  14,  15,  16,  24,  26,  29,  30,
        31,  38,  39,  40,  41,  42,  43,  52,  53,  62,  63,  64,  69,  70,
        71,  72,  73,  74,  75,  76,  77,  78,  79,  80,  81,  82,  83,  84,
        85,  86,  87,  94,  95,  96, 100])
#print(filtered_genre_year['genre'].unique()) #<--- 9 distinct genres with over 8 movies released.

filtered_genre_year=movies_genre_year[(movies_genre_year['year_added'] >= 2014) & (movies_genre_year['year_added'] < 2021)]
#print(len(filtered_genre_year['genre'].unique())) # <- 17 distinct genres after cleaning

#Visualize number of movies released per genre each year.
palette1=sns.set_palette('colorblind',n_colors=17)
fig8=sns.barplot(filtered_genre_year,x='year_added',y='movies_per_genreyear',hue='genre',palette=palette1)
fig8.set(xlabel="Year",ylabel="Total movie count per year")
fig8.set(title="Total movies added per year and genre")
fig8.tick_params(labelsize=8)
plt.show()

#Find whether there's a correlation between genre and number of movies released each year . 
genres_sum=filtered_genre_year.groupby(['genre'])['movies_per_genreyear'].sum().reset_index(name='sum').sort_values(by='sum',ascending=False)
#print(genres_sum)
#print(filtered_genre_year)

#Which genre was the most popular each year? Considering only years with over 8 movies added.
pop_genre_year=filtered_genre_year.groupby(['year_added'])[['genre','movies_per_genreyear']].max()
#print(pop_genre_year)
#print(pop_genre_year['genre'].unique()) #<--- 2 genres

#Visualize max number of movies released per genre each year. For those years with over 8 movies added per genre.
palette2=sns.set_palette('deep')
fig9=sns.barplot(pop_genre_year,x='year_added',y='movies_per_genreyear',hue='genre',palette=palette2)
fig9.set(yscale="log")
fig9.set(xlabel="Year",ylabel="Genre with most added movies per year")
fig9.set(title="Max movies added per year")
fig9.tick_params(labelsize=8)
plt.show()

# What prop of the total movies from a certain genre was released each year?
genre_year_sum=filtered_genre_year.merge(genres_sum,on='genre',how='outer')
genre_year_sum['prop_per_genre']=((genre_year_sum['movies_per_genreyear']/genre_year_sum['sum'])*100).round(decimals=2)
genre_year_sum=genre_year_sum.rename(columns={'prop_per_genre':'proportion'})
genre_year_prop=genre_year_sum.drop(['sum','movies_per_genreyear'],axis=1)
#print(genre_year_prop)

fig10=sns.relplot(genre_year_prop,x='year_added',y='proportion',hue='genre',size='proportion',sizes=(10, 150),palette=sns.set_palette('deep',n_colors=9))
fig10.set(xlabel="Year",ylabel="Proportion of genre relative to all movies added that year")
plt.ylim(0,50)
fig10.set(title="Genre representation per year")
fig10.tick_params(labelsize=9)
plt.show()

#Stats based on countries of origin for mvoies added each year.
uncategorized_c=movies_g_c_sum[movies_g_c_sum['genre']=='Uncategorized']['movies_per_countrygenre'].sum()
u_ncategorized=movies_g_c_sum[movies_g_c_sum['genre']=='Uncategorized']
movies_genre_country=movies_g_c_sum.drop(index=[19,51,97,167,192,287,333,349])
#print(movies_genre_country[movies_genre_country['genre']=='International Movies'].describe()) --> 31 rows from various countries

#Separate international movies into a different df and remove from main.
international_movies_c= movies_genre_country[movies_genre_country['genre']=='International Movies']
#print(international_movies_c.index)
movies_genre_country=movies_genre_country.drop(index=[ 16,  22,  35,  45,  55,  63,  77,  84,  95, 106, 116, 132, 152, 166, 170, 173, 190, 199, 212, 224, 234, 241, 246, 259, 268, 275, 285, 300, 307, 318, 327])
#print(movies_genre_country) --> check n of rows is 31 down.

#Add total movies per country and genre.
tot_per_genre=movies_genre_country.groupby(['genre'])['genre'].value_counts().reset_index(name='count')
tot_per_genre=tot_per_genre.sort_values(by='count',ascending=False)
#print(tot_per_genre)

#Visualize genre count by genre for all countries.
fig4=sns.barplot(tot_per_genre,x='count',y='genre', hue='genre',palette=sns.color_palette('colorblind', n_colors=17))
fig4.set(xlabel="Number of countries",ylabel="Genre")
plt.show()

#Choose only genres with over half the total movies (30). Plot genre distribution by country for those genres.
pop_genres=tot_per_genre[tot_per_genre['count'] >= 30]
#print(pop_genres)

#Visualize filtered popular movie genres.
fig5=sns.barplot(pop_genres,x='count',y='genre', hue='genre',palette=sns.color_palette('colorblind', n_colors=6))
fig5.set(xlabel="Number of countries",ylabel="Genre")
plt.show()

pop_genre_country=movies_genre_country.merge(pop_genres,on='genre',how='right').drop(columns='count')
pop_genre_sort=pop_genre_country.sort_values(by='genre',ascending= False)
#print(pop_genre_sort)

less_than_avg_movies=pop_genre_sort[pop_genre_sort['movies_per_countrygenre'] < 7]
list_less_than_avg_movies=less_than_avg_movies.index
pop_genre_sort=pop_genre_sort.drop(index=list_less_than_avg_movies)
#print(list_less_than_avg_movies) #--> 176 country/genre pairs!

pop_genre_sum=pop_genre_sort.groupby(['genre'])[['movies_per_countrygenre']].sum().sort_values(by='movies_per_countrygenre',ascending=True)

fig6=sns.barplot(pop_genre_sum,x='genre',y='movies_per_countrygenre',hue='genre',palette=sns.color_palette('colorblind', n_colors=6))
fig6.set(xlabel="Most popular genres",ylabel="Total number of movies")
plt.show()

#Find whether there's a correlation between genre and country .
#Find whether there's a correlation between genre and continent . 
