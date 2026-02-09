# Data Analysis: Child Mortality vs GDP per Capita

## Overview

This project analyzes the relationship between child mortality rates and GDP per capita across 15 countries from 2000 to 2010. The analysis involves cleaning messy CSV data, transforming it into a tidy format, and creating visualizations to reveal key insights.

## Data Cleaning Strategy

### Initial Data Structure

The raw data arrived in a "wide" format that is not suitable for analysis:

1. **Mortality Data** (`data/mortality_data.csv`):
   - Countries as rows, years (2000-2010) as columns
   - Column names: `Country`, `2000`, `2001`, ..., `2010`
   - Each cell contains mortality rate values

2. **GDP Data** (`data/gdp_data.csv`):
   - Similar wide format but with inconsistent naming
   - Column names: `Geo`, `Year_2000`, `Year_2001`, ..., `Year_2010`
   - Each cell contains GDP per capita values

### Cleaning Approach

#### 1. Mortality Data Processing (`workflow/process_mortality.py`)

**Problem**: Wide format with years as columns makes it difficult to:
- Filter by year
- Group by year
- Merge with other datasets
- Perform time-series analysis

**Solution**: Used `pd.melt()` to transform from wide to long format:
- **id_vars**: `['Country']` - kept as identifier
- **var_name**: `'year'` - column names (2000, 2001, etc.) become year values
- **value_name**: `'mortality_rate'` - cell values become mortality_rate column

**Additional transformations**:
- Renamed `Country` to `geo` for consistency
- Converted year from string to integer
- Standardized geo codes to uppercase
- Sorted by geo and year for readability

**Result**: Tidy dataset with columns: `geo`, `year`, `mortality_rate`

#### 2. GDP Data Processing (`workflow/process_gdp.py`)

**Problem**: Similar wide format but with additional complexity:
- Column names have `Year_` prefix (e.g., `Year_2000`)
- Column name is `Geo` instead of `Country`

**Solution**: Applied same `pd.melt()` approach with additional step:
- Extracted year by removing `'Year_'` prefix using string replacement
- Renamed `Geo` to `geo` for consistency
- Standardized geo codes to uppercase

**Result**: Tidy dataset with columns: `geo`, `year`, `gdpcapita`

#### 3. Data Merging (`workflow/merge_data.py`)

**Strategy**: Inner join on `geo` and `year` to ensure:
- Only complete records (both mortality and GDP data present)
- No missing values in key variables
- Consistent country-year pairs

**Enhancements**:
- Added `name` column mapping geo codes to full country names for readability
- Reordered columns to match requirements: `geo`, `name`, `mortality_rate`, `gdpcapita`, `year`
- Ensured `geo` is the first column as specified

**Result**: Final merged dataset with 165 complete records (15 countries × 11 years)

### Why This Approach?

1. **Tidy Data Principles**: Each row represents one observation (country-year), each column represents one variable
2. **Reproducibility**: Clear, documented transformations make the process repeatable
3. **Extensibility**: Tidy format makes it easy to add more countries, years, or variables
4. **Analysis-Ready**: Standard format works seamlessly with pandas, matplotlib, and seaborn

## Visualization Choices

### Scatter Plot Design

**Chart Type**: Scatter plot
- **X-axis**: GDP per capita (USD)
- **Y-axis**: Child mortality rate (per 1000 live births)
- **Color**: Year (2000-2010)

### Design Rationale

1. **Scatter Plot Selection**:
   - Best for exploring relationships between two continuous variables
   - Allows identification of patterns, outliers, and correlations
   - Each point represents one country-year observation

2. **Color Coding by Year**:
   - Enables temporal analysis within the same plot
   - Reveals trends over time (e.g., do countries move along a trajectory?)
   - Uses `viridis` palette: perceptually uniform, colorblind-friendly, works in grayscale

3. **Visual Enhancements**:
   - **Grid**: Added for easier value reading
   - **Transparency (alpha=0.7)**: Prevents overplotting when points overlap
   - **Point size (s=100)**: Large enough to see but not overwhelming
   - **High resolution (300 dpi)**: Ensures publication-quality output
   - **Legend placement**: Outside plot area to avoid obscuring data

4. **Labeling**:
   - Clear, descriptive axis labels with units
   - Informative title
   - Legend clearly indicates year values

### Alternative Considerations

- **Line plots**: Would show trends per country but harder to see overall relationship
- **Faceted plots**: Could separate by year but loses temporal continuity
- **Log scales**: Considered but kept linear for interpretability (though log might reveal more for wide GDP range)

## Key Insights

### 1. Strong Negative Correlation

The scatter plot reveals a **clear negative relationship** between GDP per capita and child mortality rate:
- Countries with higher GDP per capita tend to have lower child mortality rates
- This relationship is consistent across all years (2000-2010)

### 2. Economic Development and Health Outcomes

The data demonstrates that economic prosperity is associated with better child health outcomes:
- **High-income countries** (USA, Canada, Japan, Australia, Western Europe): Mortality rates below 10 per 1000
- **Middle-income countries** (Mexico, Brazil, South Africa, China): Mortality rates 15-40 per 1000
- **Lower-income countries** (India, Nigeria): Mortality rates above 50 per 1000

### 3. Temporal Trends

While not the primary focus, the color coding suggests:
- Most countries show gradual improvements over time (moving down and/or right)
- The relationship between GDP and mortality appears stable across the decade
- No dramatic shifts in the overall pattern

### 4. Outliers and Variations

- **Nigeria**: Highest mortality rates despite some GDP growth, suggesting other factors (healthcare access, infrastructure) play crucial roles
- **China**: Shows rapid improvement in both GDP and mortality reduction
- **India**: Lower GDP but better mortality outcomes than Nigeria, indicating GDP alone doesn't determine health

### 5. Policy Implications

The analysis suggests:
- Economic development alone is not sufficient; effective healthcare systems matter
- Countries at similar GDP levels can have different mortality rates
- Investment in public health infrastructure is critical, especially in developing economies

## Data Quality Assessment

### Strengths
- **Complete data**: No missing values in final merged dataset
- **Consistent format**: All countries have data for all years (2000-2010)
- **Correct data types**: Years as integers, rates and GDP as floats
- **Standardized codes**: Consistent geo code format (uppercase)

### Limitations
- **Sample size**: Only 15 countries, not globally representative
- **Time period**: Limited to 2000-2010, may not reflect current trends
- **Data source**: No metadata about data collection methods or definitions
- **Missing context**: No information about healthcare systems, policies, or other confounding factors

## Reproducibility

All scripts are designed for reproducibility:
- Clear, documented code
- Standardized file paths
- No hardcoded assumptions
- Complete dependency management via `pyproject.toml`

The `run.sh` script executes the entire pipeline from raw data to final visualization, ensuring anyone can reproduce the analysis.

## Future Work

Potential extensions:
1. Add more countries for global perspective
2. Extend time series to present day
3. Include additional variables (healthcare spending, education, etc.)
4. Statistical modeling (regression analysis)
5. Interactive visualizations
6. Regional comparisons

---

*This analysis demonstrates the importance of data cleaning, thoughtful visualization design, and clear documentation in data science workflows.*

