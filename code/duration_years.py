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
netflix_movies=netflix_movies[netflix_movies.duration >= 60 and netflix_movies.duration < 250]
#print(netflix_movies.info)

# Define an empty list
colors = []

# Iterate over rows of netflix_movies
for label, row in netflix_movies.iterrows() :
    if row["genre"] == "Children" :
        colors.append("red")
    elif row["genre"] == "Documentaries" :
        colors.append("orange")
    elif row["genre"] == "Stand-Up":
        colors.append("green")
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
palette=sns.set_palette('colorblind',n_colors=11)
fig0=sns.scatterplot(data=netflix_movies, x='release_year', y='duration', hue='release_year', palette=palette)
fig0.set(xlabel="Release year",ylabel="Duration (min)")
fig0.set(title="Movie duration by year of release")
fig0.tick_params(labelsize=8)
plt.show()
