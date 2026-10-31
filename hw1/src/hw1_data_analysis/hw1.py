import pandas as pd
import matplotlib.pyplot as plt

b_data = pd.read_csv("src/hw1_data_analysis/bicycle_data.csv")

#print(b_data.head())
#print(b_data.columns)
#print(b_data.dtypes)

# Date contains the date and hour of each observation and should be datetime. Total contains the total bicycle count and should be numeric.
# West Sidewalk and East Sidewalk contain bicycle counts for each direction and should be numeric. Pandas uses float64 because these columns may have missing values.
b_data["Date"] = pd.to_datetime(b_data["Date"], format="%m/%d/%Y %I:%M:%S %p")
#print(b_data["Date"].head())
#print(b_data["Date"].dtype)

west = ("Fremont Bridge Sidewalks, south of N 34th St Cyclist West Sidewalk")
east = ("Fremont Bridge Sidewalks, south of N 34th St Cyclist East Sidewalk")
b_data["total"] = b_data[west] +b_data[east]
#print(b_data[[west,east,"total"]].head())

b_data["Hour"] = b_data["Date"].dt.hour
b_data["Year"] = b_data["Date"].dt.year
#print( b_data[["Date", "Hour", "Year"]].head())

data_2016 = b_data[b_data["Year"] == 2016].copy()
# print(data_2016.head())
# print(data_2016["Year"].unique())
# print("Number of 2016 rows:", len(data_2016))

miss = data_2016[[west,east,"total"]].isna().any(axis=1)
miss_years = data_2016[miss]
miss_count = miss.sum()
print(miss_years)
print("Numbers of missing time points:",miss_count)
# There is 1 time point with missing bicycle-count data in 2016.

data_2016c = data_2016[~miss].copy()



hour_counts = (data_2016c.groupby("Hour")["total"].sum())
hour_counts.plot( kind="line", marker="o")
plt.title("Fremont Bridge Bicycle Counts by Hour in 2016")
plt.xlabel("Hour of Day")
plt.ylabel("Total Bicycle Count")
plt.xticks(range(24))
plt.tight_layout()
plt.savefig("counts_by_hour.png", dpi=300)
plt.close()

average = (data_2016c.groupby("Hour")["total"].mean())
busyhour = average.idxmax()
print("Busiest hour on average:", busyhour)
print("Average bicycle count:",average.max())
# On average, the busiest hour in 2016 was 17:00.