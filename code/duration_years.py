# Are movies getting shorter?

# Importing pandas and matplotlib
import pandas as pd
import matplotlib.pyplot as plt

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

# Define an empty list
colors = []

# Iterate over rows of netflix_movies
for label, row in netflix_movies.iterrows() :
    if row["genre"] == "Children" :
        colors.append("green")
    elif row["genre"] == "Documentaries" :
        colors.append("black")
    elif row["genre"] == "Stand-Up":
        colors.append("red")
    else:
        colors.append("purple")
        
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
# Iterate over rows of release_year in netflix_movies:
decades=[1940,1950,1960,1970,1980,1990,2000,2010,2020]
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
distinct_colors= list(set([decade for decade in colors_decades]))
#print(distinct_colors)
color_dict=dict(zip(decades,distinct_colors))
#print(color_dict)

#Group df by decade (add column first or loop it to group). 
#hue='decade'
palette=sns.color_palette('colorblind', n_colors=n_decades)
fig0=sns.scatterplot(data=netflix_movies, x='release_year', y='duration', hue=colors_decades, palette=palette)
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

#Plot mean duration per release_year
#fig11=sns.lineplot(data=movies_duration,x='release_year',y='mean', estimator='mean', errorbar=('ci',95), n_boot=1000,err_style="band")
fig11=sns.lineplot(data=movies_duration,x='release_year',y='mean')
fig11.set(xlabel="Release year",ylabel="Mean duration (min)")
fig11.set(title="Mean movie duration by year of release")
fig11.tick_params(labelsize=8)
plt.show()

