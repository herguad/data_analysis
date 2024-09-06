import pandas as pd
import matplotlib.pyplot as plt
#import seaborn as sns

netflix_df = pd.read_csv(r'C:\Users\Guadalupe\Documents\IT\py\netflix DA\netflix DA code\netflix_data.csv')

# Subset the DataFrame for type "Movie"
netflix_subset = netflix_df[netflix_df["type"] == "Movie"]

# Select only the columns of interest
netflix_movies = netflix_subset[["title", "country", "genre", "release_year", "duration"]]

# Filter for durations shorter than 60 minutes
short_movies = netflix_movies[netflix_movies.duration < 60]
#print(short_movies.info)
# Filter also for durations longer than 250 minutes to exclude outliers.
netflix_movies=netflix_movies[(netflix_movies['duration'] >= 60) & (netflix_movies['duration'] < 250 )]
#print(netflix_movies.info)

# Iterate over rows of release_year in netflix_movies:
colors_decades=[]
release_year=netflix_movies[['release_year']]
for label, row in release_year.iterrows() :
    if row["release_year"] <= 1950 :
        colors_decades.append("blue")
    elif  row["release_year"] <= 1960 :
        colors_decades.append("orange")
    elif  row["release_year"] <= 1970 :
        colors_decades.append("green")
    elif  row["release_year"] <= 1980 :
        colors_decades.append("red")
    elif  row["release_year"] <= 1990 :
        colors_decades.append("violet")
    elif  row["release_year"] <= 2000 :
        colors_decades.append("brown")
    elif row["release_year"] <= 2010:
        colors_decades.append("lilac")
    else:
        colors_decades.append("grey")

print(colors_decades[:10])

#List of distinct colors.
distinct_colors= list(set([decade for decade in colors_decades]))
#print(distinct_colors)
decades=[1940,1950,1960,1970,1980,1990,2000,2010,2020]

#Dictionary of distict colors and decades
color_dict=dict(zip(decades,distinct_colors))
#print(color_dict)

#Add an empty 'decade' column to the df.
netflix_movies['decade']=['' for i in range(len(netflix_movies))]
print(range(len(netflix_movies)))

netflix_movies=netflix_movies.reset_index(drop=True)

#index_= netflix_movies.loc[netflix_movies['release_year'] == 2003].index
#print(index_)
print(type(netflix_movies.loc[3,'release_year'])
      
#Loop over year column, identify row index, assign corresponding decade value to decade column for that row index.
for i in netflix_movies['release_year']:
    index_i= netflix_movies.loc[netflix_movies['release_year'] == i].index
    if i < 1950 :
        netflix_movies.iloc[index_i,5] = 1940
    elif i < 1960 :
        netflix_movies.iloc[index_i,5] = 1950
    elif i < 1970 :
        netflix_movies.iloc[index_i,5] = 1960
    elif i < 1980 :
        netflix_movies.iloc[index_i,5] = 1970
    elif i < 1990 :
        netflix_movies.iloc[index_i,5] = 1980
    elif i < 2000 :
        netflix_movies.iloc[index_i,5] = 1990
    elif i < 2010:
        netflix_movies.iloc[index_i,5] = 2000
    else:
        netflix_movies.iloc[index_i,5] = 2010

print(netflix_movies.head(50))


#Subset columns and plot duration vs decade.
netflix_decades=netflix_movies[['genre','release_year','duration','decade']]
#hue='decade'

#Plot means in decades for different genres.
