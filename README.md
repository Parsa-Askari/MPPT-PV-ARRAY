# MPPT Using Machine Learning Techniques

## Overview

This project implements Maximum Power Point Tracking (MPPT) for photovoltaic (PV) modules using machine learning techniques in Python. It includes data preprocessing, model training, evaluation, and visualization.

## Dataset

The dataset used for this project is available from the U.S. Department of Energy:

- **Dataset**: Data Validating Models: PV Module Performance
- **Link**: [https://www.osti.gov/dataexplorer/biblio/dataset/1811521-data-validating-models-pv-module-performance](https://www.osti.gov/dataexplorer/biblio/dataset/1811521-data-validating-models-pv-module-performance)

Download the dataset and note its local directory path; you will need it in the configuration step.


## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/Parsa-Askari/MPPT-PV-ARRAY.git
   cd MPPT-PV-ARRAY
   ```
2. Create and activate a virtual environment (optional but recommended):
   ```bash
   python3 -m venv venv
   source venv/bin/activate   # on Windows use venv\Scripts\activate
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Configuration

Before running the code, update the dataset paths in `src/Feature_engineering/ProjectPaths.py`. Open the file and set the following variables to the directory where you downloaded the dataset:

```python
# Example in src/ProjectPaths.py
# Change this to the folder containing the downloaded CSV files
folder_path = "/path/to/your/dataset/folder"

# Optionally, configure where to save trained models and outputs
output_folder_paths = "/path/to/output/folder"
```

Make sure these paths are correct and accessible.

## Usage

After configuration, you can run experiments using the `Indirect Approach.ipynb` script. For example, to train and evaluate models:


## Report

A detailed analysis and results are provided in the `report.pdf` file. Please refer to this report for methodology and results.

