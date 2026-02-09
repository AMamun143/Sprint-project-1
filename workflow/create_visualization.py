"""
Create scatter plot visualization of child mortality vs GDP per capita.

This script generates a scatter plot showing the relationship between
child mortality rate (Y-axis) and GDP per capita (X-axis), with colors
indicating the year of each observation.
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Set style for better-looking plots
sns.set_style("whitegrid")
plt.rcParams['figure.figsize'] = (12, 8)

# Load the merged dataset
print("Loading merged dataset...")
data = pd.read_csv('./data/preprocessed/merged_data.csv')

# Create the scatter plot
print("Creating scatter plot...")
fig, ax = plt.subplots(figsize=(12, 8))

# Use seaborn scatterplot with year as color
scatter = sns.scatterplot(
    data=data,
    x='gdpcapita',
    y='mortality_rate',
    hue='year',
    palette='viridis',
    s=100,
    alpha=0.7,
    ax=ax
)

# Customize the plot
ax.set_xlabel('GDP per Capita (USD)', fontsize=12, fontweight='bold')
ax.set_ylabel('Child Mortality Rate (per 1000 live births)', fontsize=12, fontweight='bold')
ax.set_title('Child Mortality Rate vs GDP per Capita (2000-2010)', 
             fontsize=14, fontweight='bold', pad=20)

# Add grid for better readability
ax.grid(True, alpha=0.3)

# Customize legend
plt.legend(title='Year', bbox_to_anchor=(1.05, 1), loc='upper left', 
           frameon=True, fancybox=True, shadow=True)

# Adjust layout to prevent label cutoff
plt.tight_layout()

# Save the figure
output_path = './paper/figs/mortality_vs_gdp.png'
print(f"Saving figure to {output_path}...")
plt.savefig(output_path, dpi=300, bbox_inches='tight')
print("Figure saved successfully!")

# Display summary statistics
print("\nSummary Statistics:")
print(f"Total observations: {len(data)}")
print(f"Countries: {data['geo'].nunique()}")
print(f"Years: {data['year'].min()} - {data['year'].max()}")
print(f"\nGDP per capita range: ${data['gdpcapita'].min():,.0f} - ${data['gdpcapita'].max():,.0f}")
print(f"Mortality rate range: {data['mortality_rate'].min():.1f} - {data['mortality_rate'].max():.1f}")

plt.close()

