# Are movies getting shorter?

# Importing pandas and matplotlib
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Read in the Netflix CSV as a DataFrame
netflix_df = pd.read_csv("netflix_data.csv")

# Subset the DataFrame for type "Movie"
netflix_subset = netflix_df[netflix_df["type"] == "Movie"]

# Select only the columns of interest
netflix_movies = netflix_subset[["title", "country", "genre", "release_year", "duration"]]

# Filter for durations shorter than 60 minutes
short_movies = netflix_movies[netflix_movies.duration < 60]
#print(short_movies.info)
# Filter also for durations longer than 250 minutes to exclude outliers.
netflix_movies=netflix_movies[(netflix_movies.duration >= 60) & (netflix_movies.duration < 250)]
#print(netflix_movies.info)

#Filter out uncategorized movies.
uncategorized=netflix_movies[netflix_movies['genre'] == 'Uncategorized']
#print(uncategorized.index)
netflix_movies=netflix_movies.drop(index=[1318, 1320, 1570, 1709, 2177, 2178, 3253, 3736, 3737, 3738, 4187, 5576, 5577, 6735, 7170, 7171])
#Identify unique genres, make a dictionary of unique genres and colors and build palette that includes all unique genres.

# Inspect the first 10 values in your list        
colors[:10]

# Set the figure style and initalize a new figure
fig = plt.figure(figsize=(12,8))

# Create a scatter plot of duration versus release_year
plt.scatter(netflix_movies.release_year, netflix_movies.duration, c=colors)

# Create a title and axis labels
plt.title("Movie Duration by Year of Release")
plt.xlabel("Release year")
plt.ylabel("Duration (min)")

# Show the plot
plt.show()

# Are movies getting shorter?
#firstanswer = "maybe"

#Try seaborn replot to check for accuracy.
#palette=sns.color_palette('colorblind', n_colors=n_decades)
fig0=sns.scatterplot(data=netflix_movies, x='release_year', y='duration')
fig0.set(xlabel="Release year",ylabel="Duration (min)")
fig0.set(title="Movie duration by year of release")
fig0.tick_params(labelsize=8)
plt.show()

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
        colors.append("grey")

#print(colors_decades[:10])

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
    if int(v) <= 1950 :
        forties.append(v)
    elif int(v) <= 1960 :
        fifties.append(v)
    elif int(v) <= 1970 :
        sixties.append(v)
    elif int(v) <= 1980 :
        seventies.append(v)
    elif int(v) <= 1990 :
        eighties.append(v)
    elif int(v) <= 2000 :
        nineties.append(v)
    elif int(v) <= 2010:
        noughties.append(v)
    else:
        tens.append(v)

###TBC

#Group df by decade (add column first or loop it to group). 
#hue='decade'


#Plot means in decades for different genres.

#Consider only mean duration per year of release and plot.
movies_duration=netflix_movies[['title','genre','release_year','duration']]
movies_duration=movies_duration.groupby(['release_year'])['duration'].mean().reset_index(name='mean')
movies_duration=movies_duration.drop(movies_duration.index[0])
movies_duration['mean']=round(movies_duration['mean'],2)
#print(movies_duration)

#Plot mean duration per release_year
#fig11=sns.lineplot(data=movies_duration,x='release_year',y='mean', estimator='mean', errorbar=('ci',95), n_boot=1000,err_style="band")
fig11=sns.lineplot(data=movies_duration,x='release_year',y='mean')
fig11.set(xlabel="Release year",ylabel="Mean duration (min)")
fig11.set(title="Mean movie duration by year of release")
fig11.tick_params(labelsize=8)
plt.show()

#Subset df for genre and duration and drop rows with 'Uncategorized' genre.
duration_genre=netflix_movies[(netflix_movies['duration'] >= 60)  & (netflix_movies['duration'] <= 180 )]
duration_genres=duration_genre[['genre','duration']]
uncateg=duration_genres[duration_genres['genre'] == 'Uncategorized']
#print(uncateg.index)
duration_genres=duration_genres.drop(index=[1318, 1320, 1570, 1709, 2177, 2178, 3253, 3736, 3737, 3738, 4187, 5576, 5577, 6735, 7170, 7171])
#print(duration_genres.head())

#Group subset df by genre and calculate mean duration for all genres. Order by descending mean_duration,i.e. genres with longer movies to shorter.
mean_dur_gen=duration_genres.groupby(['genre'])['duration'].mean('duration').reset_index(name='mean_duration')
mean_dur_gen['mean_duration']=round(mean_dur_gen['mean_duration'],2)
mean_dur_gen=mean_dur_gen.sort_values(by='mean_duration',ascending = False)
#print(mean_dur_gen)

#Select top ten genres according to mean duration.
top_means=mean_dur_gen.iloc[0:10,:]
#print(top_means)

#Plot to look for possible relations.
fig12=sns.barplot(data=top_means,x='genre',y='mean_duration',hue='genre')
fig12.set(xlabel="Genre",ylabel="Mean duration (min)")
fig12.set(title="Mean movie duration by genre")
fig12.tick_params(labelsize=8)
plt.show()

#heatmap: duration vs decade it was released
#duration_genres=sns.heatmap()
