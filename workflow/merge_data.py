"""
Merge mortality and GDP datasets into a single table.

This script combines the cleaned mortality and GDP data on geo and year,
creating a final merged dataset with columns: geo, name, mortality_rate, gdpcapita, year.
"""

import pandas as pd

# Load the tidy datasets
print("Loading tidy datasets...")
tidy_mortality = pd.read_csv('./data/preprocessed/tidy_mortality_data.csv')
tidy_gdp = pd.read_csv('./data/preprocessed/tidy_gdp_data.csv')

# Create a mapping from geo codes to country names
# This will be used to add a 'name' column
country_names = {
    'USA': 'United States',
    'CAN': 'Canada',
    'MEX': 'Mexico',
    'GBR': 'United Kingdom',
    'FRA': 'France',
    'DEU': 'Germany',
    'ITA': 'Italy',
    'ESP': 'Spain',
    'BRA': 'Brazil',
    'IND': 'India',
    'CHN': 'China',
    'JPN': 'Japan',
    'AUS': 'Australia',
    'ZAF': 'South Africa',
    'NGA': 'Nigeria'
}

# Merge the datasets on geo and year
print("Merging mortality and GDP data...")
merged_data = pd.merge(
    tidy_mortality,
    tidy_gdp,
    on=['geo', 'year'],
    how='inner'  # Inner join to keep only records present in both datasets
)

# Add the name column based on geo code
merged_data['name'] = merged_data['geo'].map(country_names)

# Reorder columns: geo, name, mortality_rate, gdpcapita, year
merged_data = merged_data[['geo', 'name', 'mortality_rate', 'gdpcapita', 'year']]

# Sort by geo and year
merged_data = merged_data.sort_values(['geo', 'year']).reset_index(drop=True)

# Save the merged dataset
print("Saving merged dataset...")
merged_data.to_csv('./data/preprocessed/merged_data.csv', index=False)

print(f"Successfully merged {len(merged_data)} records")
print(f"Countries: {merged_data['geo'].nunique()}")
print(f"Years: {merged_data['year'].min()} - {merged_data['year'].max()}")
print("\nFirst few rows:")
print(merged_data.head(10))

