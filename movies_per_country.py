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

#Group movies per release_year and nationality
movies_per_c = netflix_movies_nat.groupby(["country"]).value_counts().reset_index(name="count")

#List South American countries and select movies released by year and country
sa_countries=["Argentina", "Bolivia","Brazil","Chile","Colombia","Ecuador","Guyana","Paraguay","Peru","Suriname","Uruguay","Venezuela"]
sa_movies_per_y = movies_per_c[movies_per_c["country"].isin(sa_countries)]

#Calculate total releases per country and sort
total_releases_per_c= sa_movies_per_y.groupby(["release_year","country"])[["release_year","count"]].sum()
total_r_p_country= pd.DataFrame(total_releases_per_c)

#Where there years where no SouthAmerican movies were released?
all_years=range(1985,2020)
years_SA_movies=sa_movies_per_y["release_year"].isin(all_years)
years_no_sa_movies=years_SA_movies[years_SA_movies==False]
#print(years_no_sa_movies)

#Calculate max number of movies released each year and sort by count and country
max_releases_per_y=sa_movies_per_y.groupby("release_year")[["country","count"]].max()

movies_years=list(sa_movies_per_y["release_year"])

print(max_releases_per_y)
#Graph total_releases_per_c from 1985 to 2020
#sns.scatterplot(data=total_r_p_country, x="release_year", y="count", hue="country", palette="deep",markers= time)
#plt.show()
