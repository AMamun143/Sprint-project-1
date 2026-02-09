"""
Process GDP data from wide format to tidy format.

This script reads the messy GDP CSV file where years are columns
and transforms it into a tidy format with columns: geo, year, gdpcapita.
"""

import pandas as pd

# Load the messy GDP data (wide format)
print("Loading GDP data...")
gdp_wide = pd.read_csv('./data/raw/gdp-data.csv')

# Transform from wide to long format using pd.melt()
# The 'geo' and 'name' columns are kept as identifiers, year columns become 'year', values become 'gdpcapita'
print("Transforming GDP data from wide to long format...")
gdp_tidy = pd.melt(
    gdp_wide,
    id_vars=['geo', 'name'],
    var_name='year',
    value_name='gdpcapita'
)

# Convert year to integer (it's currently a string from column names)
gdp_tidy['year'] = gdp_tidy['year'].astype(int)

# Filter to years 2000-2010 for analysis
gdp_tidy = gdp_tidy[(gdp_tidy['year'] >= 2000) & (gdp_tidy['year'] <= 2010)]

# Remove rows with missing gdpcapita values
gdp_tidy = gdp_tidy.dropna(subset=['gdpcapita'])

# Ensure geo is lowercase (as in the source data)
gdp_tidy['geo'] = gdp_tidy['geo'].str.lower()

# Sort by geo and year for better readability
gdp_tidy = gdp_tidy.sort_values(['geo', 'year']).reset_index(drop=True)

# Save to preprocessed folder
print("Saving tidy GDP data...")
gdp_tidy.to_csv('./data/preprocessed/tidy_gdp_data.csv', index=False)

print(f"Successfully processed {len(gdp_tidy)} GDP records")
print(f"Countries: {gdp_tidy['geo'].nunique()}")
print(f"Years: {gdp_tidy['year'].min()} - {gdp_tidy['year'].max()}")

