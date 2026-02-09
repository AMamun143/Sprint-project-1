"""
Process GDP data from wide format to tidy format.

This script reads the messy GDP CSV file where years are columns with 'Year_' prefix
and transforms it into a tidy format with columns: geo, year, gdpcapita.
"""

import pandas as pd

# Load the messy GDP data (wide format)
print("Loading GDP data...")
gdp_wide = pd.read_csv('./data/gdp_data.csv')

# Transform from wide to long format using pd.melt()
# The 'Geo' column becomes 'geo', Year_* columns become 'year', values become 'gdpcapita'
print("Transforming GDP data from wide to long format...")
gdp_tidy = pd.melt(
    gdp_wide,
    id_vars=['Geo'],
    var_name='year',
    value_name='gdpcapita'
)

# Rename 'Geo' to 'geo' for consistency
gdp_tidy = gdp_tidy.rename(columns={'Geo': 'geo'})

# Extract year from 'Year_2000' format by removing 'Year_' prefix
gdp_tidy['year'] = gdp_tidy['year'].str.replace('Year_', '').astype(int)

# Ensure geo is uppercase (standardize country codes)
gdp_tidy['geo'] = gdp_tidy['geo'].str.upper()

# Sort by geo and year for better readability
gdp_tidy = gdp_tidy.sort_values(['geo', 'year']).reset_index(drop=True)

# Save to preprocessed folder
print("Saving tidy GDP data...")
gdp_tidy.to_csv('./data/preprocessed/tidy_gdp_data.csv', index=False)

print(f"Successfully processed {len(gdp_tidy)} GDP records")
print(f"Countries: {gdp_tidy['geo'].nunique()}")
print(f"Years: {gdp_tidy['year'].min()} - {gdp_tidy['year'].max()}")

