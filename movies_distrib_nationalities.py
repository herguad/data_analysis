# What's the distribution of nationalities for movies included in Netflix library?

# Importing packages for manipulation and visualization
import pandas as pd
import matplotlib.pyplot as plt
#import numpy as np
import seaborn as sns

# Read in the Netflix CSV as a DataFrame
netflix_df = pd.read_csv("netflix_data.csv")
# Subset the DataFrame for type "Movie"
netflix_subset = netflix_df[netflix_df["type"] == "Movie"]

#Distribution per continent
# Subset the DataFrame for type "country". Filter NaNs.
netflix_subset_c_noNaN = netflix_subset["country"].dropna()
netflix_countries_filtered=pd.DataFrame(netflix_subset_c_noNaN)
netflix_nat_year=netflix_countries_filtered.merge(netflix_subset, on="country",how="left")
print(netflix_nat_year)
#Distribution per year and continent

#Visualizing the distributions and finding the most and least represented nationalities in Netflix library.
