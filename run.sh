#!/bin/bash

# Sprint Project 1 - Complete Pipeline Execution Script
# This script reproduces the entire analysis from raw data to final visualization

set -e  # Exit on any error

echo "=========================================="
echo "Sprint Project 1 - Pipeline Execution"
echo "=========================================="
echo ""

# Step 1: Install dependencies using uv
echo "Step 1: Installing dependencies with uv sync..."
uv sync
echo "✓ Dependencies installed"
echo ""

# Step 2: Process mortality data
echo "Step 2: Processing mortality data..."
uv run python workflow/process_mortality.py
echo "✓ Mortality data processed"
echo ""

# Step 3: Process GDP data
echo "Step 3: Processing GDP data..."
uv run python workflow/process_gdp.py
echo "✓ GDP data processed"
echo ""

# Step 4: Merge datasets
echo "Step 4: Merging mortality and GDP datasets..."
uv run python workflow/merge_data.py
echo "✓ Datasets merged"
echo ""

# Step 5: Create visualization
echo "Step 5: Creating visualization..."
uv run python workflow/create_visualization.py
echo "✓ Visualization created"
echo ""

echo "=========================================="
echo "Pipeline completed successfully!"
echo "=========================================="
echo ""
echo "Generated files:"
echo "  - data/preprocessed/tidy_mortality_data.csv"
echo "  - data/preprocessed/tidy_gdp_data.csv"
echo "  - data/preprocessed/merged_data.csv"
echo "  - paper/figs/mortality_vs_gdp.png"
echo ""

