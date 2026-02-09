"""
Process mortality data from wide format to tidy format.

This script reads the messy mortality CSV file where years are columns
and transforms it into a tidy format with columns: geo, year, mortality_rate.
"""

import pandas as pd

# Load the messy mortality data (wide format)
print("Loading mortality data...")
mortality_wide = pd.read_csv('./data/mortality_data.csv')

# Transform from wide to long format using pd.melt()
# The 'Country' column becomes 'geo', year columns become 'year', values become 'mortality_rate'
print("Transforming mortality data from wide to long format...")
mortality_tidy = pd.melt(
    mortality_wide,
    id_vars=['Country'],
    var_name='year',
    value_name='mortality_rate'
)

# Rename 'Country' to 'geo' for consistency
mortality_tidy = mortality_tidy.rename(columns={'Country': 'geo'})

# Convert year to integer (it's currently a string from column names)
mortality_tidy['year'] = mortality_tidy['year'].astype(int)

# Ensure geo is uppercase (standardize country codes)
mortality_tidy['geo'] = mortality_tidy['geo'].str.upper()

# Sort by geo and year for better readability
mortality_tidy = mortality_tidy.sort_values(['geo', 'year']).reset_index(drop=True)

# Save to preprocessed folder
print("Saving tidy mortality data...")
mortality_tidy.to_csv('./data/preprocessed/tidy_mortality_data.csv', index=False)

print(f"Successfully processed {len(mortality_tidy)} mortality records")
print(f"Countries: {mortality_tidy['geo'].nunique()}")
print(f"Years: {mortality_tidy['year'].min()} - {mortality_tidy['year'].max()}")

