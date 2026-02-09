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

# Merge the datasets on geo and year
# Both datasets already have 'name' column, so we'll use the one from mortality
print("Merging mortality and GDP data...")
merged_data = pd.merge(
    tidy_mortality[['geo', 'name', 'year', 'mortality_rate']],
    tidy_gdp[['geo', 'year', 'gdpcapita']],
    on=['geo', 'year'],
    how='inner'  # Inner join to keep only records present in both datasets
)

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

