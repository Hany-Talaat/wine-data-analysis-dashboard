# Wine Data Analysis Dashboard

## Overview

A Python-based data analysis project using a wine dataset to demonstrate data cleaning, exploratory analysis, statistical aggregation, and data visualization.

The project uses Pandas for data processing, Matplotlib and Seaborn for visualization, and Plotly with Dash to create an interactive wine dashboard.

## Technologies

* Python
* Pandas
* Matplotlib
* Seaborn
* Plotly
* Dash

## Project Features

### Data Cleaning

The project handles missing and inconsistent data by:

* Filling missing countries using the most frequent country
* Filling missing prices using the mean price
* Replacing missing province and region information
* Cleaning wine taster Twitter handles
* Filling missing designations
* Removing records without a wine variety
* Checking remaining missing values

### Data Analysis

The project analyzes:

* Average wine scores by country
* Wine prices and ratings
* Wine review frequency by country
* Average prices by province
* Italian wine provinces
* Spanish wine provinces
* Canadian wine provinces

### Data Visualization

The project includes several visualization techniques:

* Line charts
* Bar charts
* Scatter plots
* Pie charts
* Histograms
* KDE plots
* Faceted visualizations
* Interactive Plotly charts

### Interactive Dashboard

The project includes a Dash dashboard that compares:

* Average wine price
* Average rating points
* Top Italian wine provinces

## Project Structure

```text
wine-data-analysis-dashboard/
│
├── README.md
├── wine_analysis.py
├── dashboard.py
├── requirements.txt
│
└── data/
    └── README.md
```

## Installation

Clone the repository and install the required libraries:

```bash
pip install -r requirements.txt
```

## Dataset

The project expects the wine dataset to be placed at:

```text
data/Wine_data.csv
```

The dataset is not included in this repository.

## Running the Analysis

Run:

```bash
python wine_analysis.py
```

This executes the data cleaning, analysis, and visualization operations.

## Running the Dashboard

Run:

```bash
python dashboard.py
```

The Dash application will start locally and provide an interactive wine analysis dashboard.

## Skills Demonstrated

* Python programming
* Data cleaning
* Missing value handling
* Data transformation
* Pandas
* GroupBy and aggregation
* Data visualization
* Exploratory data analysis
* Dashboard development
* Plotly
* Dash

## Author

**Hany Talaat**
