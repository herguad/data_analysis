
# Have more nationalities been included on netflix in time?
# Importing pandas and matplotlib
import pandas as pd
import matplotlib.pyplot as plt
#import numpy as np
#import seaborn as sns

netflix_df=pd.read_csv('netflix_data.csv')
# Read in the Netflix CSV as a DataFrame
netflix_df = pd.read_csv("netflix_data.csv")

# Subset the DataFrame for type "Movie"
netflix_subset = netflix_df[netflix_df["type"] == "Movie"]

# Select only the columns of interest
netflix_movies_nat = netflix_subset[["country", "release_year"]]
netflix_movies_year=  netflix_subset[["release_year"]]
#Group movies by country and count them
movies_per_c = netflix_movies_nat.groupby(["country"]).value_counts().reset_index(name="count")

#List South American countries and select movies released by year and country
sa_countries=["Argentina", "Bolivia","Brazil","Chile","Colombia","Ecuador","Guyana","Paraguay","Peru","Suriname","Uruguay","Venezuela"]
sa_movies_per_y = movies_per_c[movies_per_c["country"].isin(sa_countries)]

#Calculate max number of movies released each year and sort by county and country

print(sa_movies_per_y)
#Graph release_year agnst nationality with scatterplot: use color for nationality and size for n of movies.