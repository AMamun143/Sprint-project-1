# Sprint Project 1: Data Cleaning and Visualization

This project demonstrates a complete data science workflow: cleaning messy CSV data into tidy format, merging datasets, creating visualizations, and ensuring full reproducibility.

## 📋 Project Overview

This project analyzes the relationship between child mortality rates and GDP per capita across 193 countries from 2000 to 2010. The analysis involves:

1. **Data Cleaning**: Transforming wide-format CSV files into tidy format
2. **Data Merging**: Combining mortality and GDP datasets
3. **Visualization**: Creating scatter plots to reveal relationships
4. **Reproducibility**: Complete pipeline automation with `run.sh`

### Key Results

- **193 countries** analyzed
- **2,119 records** (country-year observations)
- **Time period**: 2000-2010
- **GDP range**: $666 - $336,887 per capita
- **Mortality range**: 2.6 - 224.9 per 1000 live births

## 🚀 Quick Start

### Prerequisites

- **Python 3.8+** (Python 3.12.3 recommended)
- **uv** package manager ([Installation instructions](#installing-uv))
- **Git** (for cloning the repository)

### Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/AMamun143/Sprint-project-1.git
   cd Sprint-project-1
   ```

2. **Install uv** (if not already installed):
   ```bash
   # On Linux/macOS
   curl -LsSf https://astral.sh/uv/install.sh | sh
   
   # Or using pip (if available)
   pip install uv
   ```

3. **Make the run script executable:**
   ```bash
   chmod +x run.sh
   ```

4. **Run the complete pipeline:**
   ```bash
   bash run.sh
   ```

That's it! The script will automatically:
- Install all dependencies
- Process the raw data
- Create visualizations
- Generate all output files

## 📁 Project Structure

```
Sprint-project-1/
├── data/
│   ├── raw/                          # Raw data files (messy format)
│   │   ├── child-motality.csv        # Child mortality data (wide format)
│   │   └── gdp-data.csv              # GDP per capita data (wide format)
│   └── preprocessed/                  # Cleaned, tidy data
│       ├── tidy_mortality_data.csv   # Processed mortality data
│       ├── tidy_gdp_data.csv         # Processed GDP data
│       └── merged_data.csv           # Final merged dataset
├── workflow/                          # Data processing scripts
│   ├── process_mortality.py          # Clean mortality data
│   ├── process_gdp.py                # Clean GDP data
│   ├── merge_data.py                 # Merge datasets
│   └── create_visualization.py       # Generate scatter plot
├── paper/
│   ├── NOTE.md                       # Comprehensive documentation
│   └── figs/
│       └── mortality_vs_gdp.png     # Final visualization
├── run.sh                            # Complete pipeline script
├── pyproject.toml                    # Project dependencies
├── uv.lock                           # Locked dependency versions
└── README.md                         # This file
```

## 🔧 The `run.sh` Script

The `run.sh` script is the heart of reproducibility in this project. It automates the entire data pipeline from raw data to final visualization.

### What it does:

1. **Installs Dependencies** (`uv sync`)
   - Creates a virtual environment (`.venv`)
   - Installs exact package versions from `uv.lock`
   - Ensures reproducible environment

2. **Processes Mortality Data** (`workflow/process_mortality.py`)
   - Reads `data/raw/child-motality.csv`
   - Transforms from wide to long format
   - Filters to years 2000-2010
   - Saves to `data/preprocessed/tidy_mortality_data.csv`

3. **Processes GDP Data** (`workflow/process_gdp.py`)
   - Reads `data/raw/gdp-data.csv`
   - Transforms from wide to long format
   - Filters to years 2000-2010
   - Saves to `data/preprocessed/tidy_gdp_data.csv`

4. **Merges Datasets** (`workflow/merge_data.py`)
   - Combines mortality and GDP data
   - Joins on `geo` and `year`
   - Creates final dataset with columns: `geo`, `name`, `mortality_rate`, `gdpcapita`, `year`
   - Saves to `data/preprocessed/merged_data.csv`

5. **Creates Visualization** (`workflow/create_visualization.py`)
   - Generates scatter plot: mortality rate vs GDP per capita
   - Colors indicate year (2000-2010)
   - Saves to `paper/figs/mortality_vs_gdp.png`

### How to Use `run.sh`

#### Basic Usage:
```bash
bash run.sh
```

#### Make it Executable (One-time):
```bash
chmod +x run.sh
./run.sh
```

#### Test Reproducibility:
```bash
# Delete all generated files
rm -rf data/preprocessed/* paper/figs/*

# Run the script - it will recreate everything
bash run.sh
```

### Script Features

- **Error Handling**: Uses `set -e` to exit on any error
- **Progress Messages**: Clear output showing each step
- **Automatic Dependency Management**: No manual package installation needed
- **Reproducible**: Always produces identical results

## 📊 Data Processing Workflow

### Phase 1: Data Formatting

**Input**: Messy CSV files with years as columns (wide format)
```
geo, name, 2000, 2001, 2002, ...
afg, Afghanistan, 129.18, 125.19, 121.06, ...
```

**Output**: Tidy CSV files with one row per observation
```
geo, name, year, mortality_rate
afg, Afghanistan, 2000, 129.18
afg, Afghanistan, 2001, 125.19
```

**Scripts**:
- `workflow/process_mortality.py`: Uses `pd.melt()` to reshape data
- `workflow/process_gdp.py`: Same transformation for GDP data

### Phase 2: Data Merging

**Input**: Two tidy datasets (mortality and GDP)
**Output**: Single merged dataset with all variables
**Script**: `workflow/merge_data.py`

### Phase 3: Visualization

**Input**: Merged dataset
**Output**: Scatter plot showing relationship between variables
**Script**: `workflow/create_visualization.py`

## 🛠️ Manual Setup (Alternative to `run.sh`)

If you prefer to run steps manually:

1. **Install dependencies:**
   ```bash
   uv sync
   ```

2. **Process data:**
   ```bash
   uv run python workflow/process_mortality.py
   uv run python workflow/process_gdp.py
   uv run python workflow/merge_data.py
   ```

3. **Create visualization:**
   ```bash
   uv run python workflow/create_visualization.py
   ```

## 📦 Dependencies

All dependencies are managed through `uv` and specified in `pyproject.toml`:

- **pandas**: Data manipulation and analysis
- **matplotlib**: Plotting and visualization
- **seaborn**: Statistical data visualization

Exact versions are locked in `uv.lock` for reproducibility.

## 🔍 Installing uv

### Option 1: Official Installer (Recommended)
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

After installation, restart your terminal or run:
```bash
source $HOME/.cargo/env  # If installed via cargo
```

### Option 2: Using pip
```bash
pip install uv
```

### Option 3: Using Homebrew (macOS)
```bash
brew install uv
```

### Verify Installation
```bash
uv --version
```

## 📝 Output Files

After running `run.sh`, you'll find:

1. **`data/preprocessed/tidy_mortality_data.csv`**
   - Columns: `geo`, `name`, `year`, `mortality_rate`
   - 2,130 records (194 countries × 11 years, some missing)

2. **`data/preprocessed/tidy_gdp_data.csv`**
   - Columns: `geo`, `name`, `year`, `gdpcapita`
   - 2,123 records (193 countries × 11 years, some missing)

3. **`data/preprocessed/merged_data.csv`**
   - Columns: `geo`, `name`, `mortality_rate`, `gdpcapita`, `year`
   - 2,119 records (complete cases only)

4. **`paper/figs/mortality_vs_gdp.png`**
   - High-resolution scatter plot (300 DPI)
   - Shows relationship between mortality and GDP
   - Colors indicate year

## 🧪 Testing Reproducibility

To verify the pipeline is fully reproducible:

```bash
# 1. Delete all generated files
rm -rf data/preprocessed/* paper/figs/* .venv/

# 2. Run the script
bash run.sh

# 3. Verify all files are recreated
ls -lh data/preprocessed/
ls -lh paper/figs/
```

## 📚 Documentation

For detailed information about:
- **Data cleaning strategy**: See `paper/NOTE.md`
- **Visualization choices**: See `paper/NOTE.md`
- **Key insights**: See `paper/NOTE.md`

## 🌿 Git Workflow

This project follows a structured Git workflow with feature branches:

- **`main`**: Production-ready code
- **`data-formatting`**: Phase 1 (data cleaning)
- **`visualization`**: Phase 2 (visualization)
- **`documentation`**: Phase 3 (documentation)
- **`update-with-real-data`**: Real data integration

## 🐛 Troubleshooting

### Issue: `uv: command not found`
**Solution**: Install uv (see [Installing uv](#installing-uv) section)

### Issue: Permission denied when running `run.sh`
**Solution**: Make the script executable:
```bash
chmod +x run.sh
```

### Issue: Python version error
**Solution**: Ensure Python 3.8+ is installed:
```bash
python3 --version
```

### Issue: Missing data files
**Solution**: Ensure `data/raw/` directory contains:
- `child-motality.csv`
- `gdp-data.csv`

### Issue: Virtual environment conflicts
**Solution**: Delete and recreate:
```bash
rm -rf .venv/
uv sync
```

## 📄 License

This project is part of a sprint assignment for data science coursework.

## 👤 Author

AMamun143

## 🔗 Repository

GitHub: https://github.com/AMamun143/Sprint-project-1.git

---

**Note**: This project demonstrates best practices in data science including tidy data principles, reproducible research, and clear documentation.

