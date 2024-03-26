
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

#Group movies per release_year and nationality
#grouped_movies_cy = netflix_movies_nat.groupby(["country","release_year"]).agg(['count'])
grouped_movies_c = netflix_movies_nat.groupby(["country"]).count()
print(grouped_movies_c)

#Graph release_year agnst nationality with scatterplot: use color for nationality and size for n of movies.
