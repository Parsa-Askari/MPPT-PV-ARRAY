# MPPT Using Machine Learning Techniques

## Overview

This project implements Maximum Power Point Tracking (MPPT) for photovoltaic (PV) modules using machine learning techniques in Python. It includes data preprocessing, model training, evaluation, and visualization.

## Dataset

The dataset used for this project is available from the U.S. Department of Energy:
### MPPT
- **Dataset**: Data Validating Models: PV Module Performance
- **Link**: [Data Validating Models PV Module Performance](https://www.osti.gov/dataexplorer/biblio/dataset/1811521-data-validating-models-pv-module-performance)
### Forecasting 
- **Dataset** : Dataset is gathered from the Nasa Power API . two downloaded datasets can be found in `Dataset` Folder by the the names `tabriz_w.csv` and `kerman_w.csv`
- **Link** [Nasa Power API](https://power.larc.nasa.gov/data-access-viewer/)
### Anomaly Detection 
- **Dataset** : InfraredSolarModules :  20000 infrared images of solar pannels
- **Link** [InfraredSolarModules](https://github.com/RaptorMaps/InfraredSolarModules)
  
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
the preprocessed Dataset is already available in `Dataset` directory. but if you wish to preprocess or analyse it from scratch , Before running the code, update the dataset paths in `src/Feature_engineering/ProjectPaths.py`. Open the file and set the following variables to the directory where you downloaded the dataset:

```python
# Example in src/ProjectPaths.py
# Change this to the folder containing the the 3 sites
folder_path = "/path/to/your/dataset/folder"

# configure where to save the preprocessed datasets
output_folder_paths = "/path/to/output/folder"
```

Make sure these paths are correct and accessible.

## Usage
### MPPT
After configuration, you can run experiments using the `Indirect Approach.ipynb` notebook to train diffrent models and save them in `Best Models` directory. the `main.py` file can also be used to test the trained models on some of your chosen solar pannels . 
### Forecasting
there are two files in the `forecasting` folder . `weather_data.py` can be used to download weather data from nasa api using diffrent locations . `predict power.py` can be used to predict the anual power for that location given the downloaded dataset.
### Anomaly Detection
in the `solar_anomaly.ipynb` you can train the model from scratch but there is also a pretrained model in the `Best Models` directory named `normal_cnn_model_state.pth` which you can use in the notebook to predict anomaly using image paths 
## Report

A detailed analysis and results are provided in the `report.pdf` file. Please refer to this report for methodology and results for MPPT task.

