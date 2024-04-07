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
netflix_movies_nat = netflix_subset[["country", "release_year"]] #-->Change 'release_year' for 'date_added' from here downwards

#Group movies per release_year and nationality
movies_per_c = netflix_movies_nat.groupby(["country"]).value_counts().reset_index(name="count")

#print(movies_per_c)

#List South American countries and select movies released by year and country
sa_countries=["Argentina", "Bolivia","Brazil","Chile","Colombia","Ecuador","Guyana","Paraguay","Peru","Suriname","Uruguay","Venezuela"]
sa_movies_per_y = movies_per_c[movies_per_c["country"].isin(sa_countries)]

#Calculate total releases per country and sort by country
total_releases_per_c= sa_movies_per_y.groupby(["release_year","country"])[["release_year","count"]].sum()
total_r_p_country= pd.DataFrame(total_releases_per_c)

#print(sa_movies_per_y)

#Calculate year where each country released max number of movies 
max_releases_per_y=sa_movies_per_y.groupby("country")[["release_year","count"]].max()

#print(max_releases_per_y)

#Graph total_releases_per_c from 1985 to 2020
#Comparing plots
#Histogram:too much overlap
sns.histplot(data=total_r_p_country, x="release_year", binrange=(1980,2025), hue="country", element="step")
plt.ylim(0,4)
plt.show()

#Scatterplot: still unclear, too many colors
sns.scatterplot(data=total_r_p_country, x="release_year", y="count", hue="country", palette= "deep")
plt.xlim(1980,2025)
plt.ylim(0,12)
plt.show()
