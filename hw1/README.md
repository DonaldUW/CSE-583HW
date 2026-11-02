# CSE 583 Homework 1: Bicycle Data Analysis

## Dataset

This homework uses hourly bicycle counts recorded at the Fremont Bridge beginning in 2012.

- Dataset description: <https://data.seattle.gov/Transportation/Fremont-Bridge-Hourly-Bicycle-Counts-by-Month-Octo/65db-xm6k>
- CSV download: <https://data.seattle.gov/api/views/65db-xm6k/rows.csv>

## Required Folder Structure

```text
hw1/
├── pyproject.toml
├── README.md
└── src/
    └── hw1_data_analysis/
        ├── __init__.py
        ├── hw1.py
        └── bicycle_data.csv
```

The project name in `pyproject.toml` uses hyphens (`hw1-data-analysis`), while the Python package directory uses underscores (`hw1_data_analysis`).


## Important Notes

The downloaded CSV contains these columns:

- `Date`
- `Fremont Bridge Sidewalks, south of N 34th St Total`
- `Fremont Bridge Sidewalks, south of N 34th St Cyclist West Sidewalk`
- `Fremont Bridge Sidewalks, south of N 34th St Cyclist East Sidewalk`

The date field contains the year, month, day, and hour. The analysis converts it to a Pandas datetime column and extracts the year and hour.

## Bonus: Datetime Formats

The complete `Date` column was converted to Pandas datetime format.

Python's `datetime.datetime` represents one date-time object and is useful for general date operations in Python programs.

NumPy's `datetime64` is designed for efficiently storing and calculating arrays of date-time values.

Pandas datetime columns build on NumPy date-time types and provide convenient tabular operations such as `.dt.year` and `.dt.hour`.

## Process Description

I first used Pandas to read the CSV file into a DataFrame and inspected the column names and data types. The bicycle-count columns were `float64` because they could contain missing values, and I converted the `Date` column to Pandas datetime.

Next, I added the East and West bicycle counts to create the `total` column and extracted `Hour` and `Year` from `Date`. I filtered the 8,784 observations from 2016, found one time point with missing bicycle counts, and excluded that row before the remaining analysis.

I grouped and summed the 2016 bicycle counts by hour, used Matplotlib to create a line plot with a title and axis labels, and saved it as `counts_by_hour.png`. I also calculated the average bicycle count for each hour and used `idxmax()` to determine that the busiest hour on average was 17:00.

Finally, I reran the complete script, confirmed that the missing-data count was 1 and the busiest hour was 17, and visually inspected the generated plot's title, axes, and curve.

## AI Assistance Disclosure

AI was used to explains different functions, and checked grammers. AI also using for write down the README files and checked the progress of hw1. All coding and solving part are finished by myself.
