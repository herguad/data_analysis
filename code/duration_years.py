# Are movies getting shorter?

# Importing pandas and matplotlib
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Read in the Netflix CSV as a DataFrame
netflix_df = pd.read_csv("netflix_data.csv")

# Subset the DataFrame for type "Movie"
netflix_subset = netflix_df[netflix_df["type"] == "Movie"]
#print(netflix_df.shape)
#print(netflix_df.info())
#print(netflix_df.head(3))

#data about movies (not documentaries, series, or else) and pick only those columns of interest, i.e. title, country, genre, year released and duration.
#- Filter out movies shorter than an hour.
#- Iterate over the rows and assign a color to each member in a subset of genres (perhaps the most popular overall, see movies_distrib_genre) and others. Inspect the list to check.

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
genres=netflix_movies['genre'].unique()
c_olors = ['purple','darkorange','lawngreen','tomato','magenta','lime','red','olive','maroon','royalblue','darkmagenta','brown','orange','yellow','gold','forestgreen','grey','turquoise']
genre_color=dict(zip(genres,c_olors))
print(genre_color) #Check dictionary was built appropriately.

colors=[]

gen_re=netflix_movies[['genre']]
for i in gen_re.values:
    for k,v in genre_color.items():
        if i == k:
            colors.append(v)
        else:
            continue
print(colors[:10]) # Inspect the first 10 values in your list        

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

fig0=sns.scatterplot(data=netflix_movies, x='release_year', y='duration', color='purple')
fig0.set(xlabel="Release year",ylabel="Duration (min)")
fig0.set(title="Movie duration by year of release")
fig0.tick_params(labelsize=8)
plt.show()



#Consider only mean duration per year of release and plot.
movies_duration=netflix_movies[['title','genre','release_year','duration']]
movies_duration=movies_duration.groupby(['release_year'])['duration'].mean().reset_index(name='mean')
movies_duration=movies_duration.drop(movies_duration.index[0])
movies_duration['mean']=round(movies_duration['mean'],2)
#print(movies_duration)

fig11=sns.lineplot(data=netflix_movies,x='release_year',y='duration',estimator='mean', errorbar=('ci',75), n_boot=1000)
fig11.set(xlabel="Release year",ylabel="Mean duration (min)")
fig11.set(title="Mean movie duration by year of release")
fig11.tick_params(labelsize=7)
plt.show()

duration_genre=netflix_movies[(netflix_movies['duration'] >= 60)  & (netflix_movies['duration'] <= 180 )]
duration_genres=duration_genre[['genre','duration']]

#Group subset df by genre and calculate mean duration for all genres. Order by descending mean_duration,i.e. genres with longer movies to shorter.
mean_dur_gen=duration_genres.groupby(['genre'])['duration'].mean('duration').reset_index(name='mean_duration')
mean_dur_gen['mean_duration']=round(mean_dur_gen['mean_duration'],2)
mean_dur_gen=mean_dur_gen.sort_values(by='mean_duration',ascending = False)
#print(mean_dur_gen)

#Select top ten genres according to mean duration.
top_means=mean_dur_gen.iloc[0:10,:]
#print(top_means)
#Plot to look for possible relations.
fig12=sns.barplot(data=mean_dur_gen,x='genre',y='mean_duration',hue='genre')
fig12.set(xlabel="Genre",ylabel="Mean duration (min)")
fig12.set(title="Mean movie duration by genre")
fig12.tick_params(labelsize=8)
plt.show()
#fig12=sns.relplot(data=duration_genre,row='genre', kind='line')
#plt.show()
#heatmap: duration vs decade it was released
#duration_genres=sns.heatmap()

