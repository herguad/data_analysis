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
duration_decade=netflix_movies[['release_year','duration']]
list_years=duration_decade['release_year'].to_list()
forties=[]
fifties=[]
sixties=[]
seventies=eighties=[]
nineties=[]
noughties=[]
tens=[]
for v in list_years:
    if int(v) < 1950 :
        forties.append(v)
    elif int(v) < 1960 :
        fifties.append(v)
    elif int(v) < 1970 :
        sixties.append(v)
    elif int(v) < 1980 :
        seventies.append(v)
    elif int(v) < 1990 :
        eighties.append(v)
    elif int(v) < 2000 :
        nineties.append(v)
    elif int(v) < 2010:
        noughties.append(v)
    else:
        tens.append(v)

print(tens[:20])

#Group df by decade (add column first or loop it to group). 
#hue='decade'

#Plot means in decades for different genres.
