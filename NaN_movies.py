# Have more nationalities been included on netflix in time?
# Importing pandas and matplotlib
import pandas as pd
import matplotlib.pyplot as plt
#import numpy as np
import seaborn as sns

netflix_df=pd.read_csv('netflix_data.csv')
# Read in the Netflix CSV as a DataFrame
netflix_df = pd.read_csv("netflix_data.csv")

# Subset the DataFrame for type "Movie"
netflix_subset = netflix_df[netflix_df["type"] == "Movie"]

# Select only the columns of interest
netflix_movies_nat = netflix_subset[["country", "release_year"]]

#Where there years where no SouthAmerican movies were released?
all_years=range(1985,2020)
years_movies=netflix_movies_nat["release_year"].isin(all_years)
no_movies_y=years_movies[years_movies==False]

print(netflix_movies_nat)

#Movies with NaN countries
# Subset the DataFrame for type "country". Filter NaNs and eliminate duplicates.
netflix_subset_c = netflix_df["country"]
country_nan=netflix_subset_c[netflix_subset_c.isnull()]
