# Sustainability KPI Tracker

The **Sustainability KPI Tracker** is a Python-based tool designed to track, analyze, and visualize sustainability key performance indicators (KPIs). This tool allows organizations to monitor their performance against sustainability targets, identify areas for improvement, and present insights through professional static and interactive visualizations.

## Features
- **Performance Metrics**:
  - Calculate performance percentages for KPIs based on actual vs. target values.
  - Categorize performance into `On Track` or `Needs Improvement`.
- **Visualization**:
  - Static bar charts using Matplotlib and Seaborn.
  - Interactive bar charts with Plotly for dynamic exploration.
  - Trend analysis over time for KPI performance.
- **Export Results**:
  - Save performance summaries to a CSV file for further reporting or sharing.
- **Logging**:
  - Provides detailed logs for all operations, including error handling and execution progress.

## Setup
### Prerequisites
Ensure you have Python 3.7 or above installed on your system.

### Installation
1. Install required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

### Sample Data
A sample dataset is provided in `example_data/sustainability_kpis.csv` to help you get started.

### Running the Tracker
To run the tracker:
```bash
python sustainability_kpi_tracker.py example_data/sustainability_kpis.csv
```

## Input Data Format
The tracker expects a CSV file with the following columns:
- `KPI`: Name of the key performance indicator.
- `Target`: The target value for the KPI.
- `Actual`: The actual achieved value for the KPI.
- `Date`: The date associated with the KPI data (YYYY-MM-DD format).

## Outputs
1. **Console Output**:
   - Displays performance summaries, including average performance and the number of KPIs on track.
2. **Static Visualization**:
   - Bar charts highlighting performance and status for each KPI.
3. **Interactive Visualization**:
   - Plotly-based bar charts with hover details for enhanced exploration.
4. **Trend Analysis**:
   - Line charts showing KPI performance trends over time.
5. **CSV Export**:
   - Save results to a specified CSV file for further analysis or archival.

## Example
Here’s an example of running the tracker with the sample data:
```bash
python sustainability_kpi_tracker.py example_data/sustainability_kpis.csv
```

## License
This project is licensed under the MIT License. 
