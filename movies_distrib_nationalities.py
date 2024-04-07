# What's the distribution of nationalities for movies included in Netflix library?

# Importing packages for manipulation and visualization
import pandas as pd
import matplotlib.pyplot as plt
#import numpy as np
import seaborn as sns

#Distribution per continent
#List countries represented in Netflix library.
netflix_df=pd.read_csv('netflix_data.csv')
# Read in the Netflix CSV as a DataFrame
netflix_df = pd.read_csv("netflix_data.csv")

# Subset the DataFrame for type "country". Filter NaNs and eliminate duplicates.
netflix_subset_c = netflix_df["country"]
country_nan=netflix_subset_c.isna()
non_nan_country=pd.DataFrame(country_nan==False)
filter_countries_nan=netflix_subset_c[...]
print(filter_countries_nan)
#Distribution per year and continent

#Visualizing the distributions and finding the most and least represented nationalities in Netflix library.
