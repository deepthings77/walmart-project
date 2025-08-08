# Lifecycle Impact Simulator

The **Lifecycle Impact Simulator** is a Python-based tool designed to assess and optimize lifecycle stages of a product or process based on key criteria like cost, carbon footprint, water usage, and energy consumption. It enables users to simulate lifecycle impacts using weighted criteria and provides detailed visualizations and outputs.

## Features
- **Multi-Criteria Simulation**:
  - Simulate lifecycle impacts based on customizable weights for cost, carbon footprint, water usage, and energy consumption.
- **Parallel Processing**:
  - Speeds up simulation for large datasets using multi-threaded processing.
- **Professional Logging**:
  - Tracks key events and errors with detailed log messages.
- **Visualizations**:
  - Professional bar charts displaying impact scores for lifecycle stages.
- **Export Results**:
  - Save simulation results to a CSV file for further analysis.

## Setup
### Prerequisites
Ensure you have Python 3.7 or above installed on your system.

### Installation
1. Install required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

### Sample Data
A sample dataset is provided in `example_data/lifecycle_data.csv` to help you get started.

### Running the Simulator
To run the simulator:
```bash
python lifecycle_impact_simulator.py example_data/lifecycle_data.csv \
  --weight_cost 0.3 \  # Priority for minimizing cost (higher value = more focus on cost reduction)
  --weight_carbon 0.3 \  # Priority for reducing carbon footprint (higher value = more focus on low-emission stages)
  --weight_water 0.2 \  # Priority for minimizing water usage (higher value = more focus on water conservation)
  --weight_energy 0.2 \  # Priority for reducing energy consumption (higher value = more focus on efficiency)
  --output_file results.csv  # Name of the file where results will be saved
```

## Input Data Format
The simulator expects a CSV file with the following columns:
- `Stage`: Name of the lifecycle stage.
- `Cost`: Cost associated with the lifecycle stage.
- `Carbon_Footprint`: Carbon emissions for the lifecycle stage.
- `Water_Usage`: Water consumption for the lifecycle stage.
- `Energy_Consumption`: Energy usage for the lifecycle stage.

## Outputs
1. **Console Output**: Displays lifecycle stages ranked by impact score.
2. **CSV Export**: Saves simulation results to a specified output file.
3. **Visualizations**:
   - Bar charts ranking lifecycle stages by impact score.

## Example
Here’s an example of running the simulator with the sample data:
```bash
python lifecycle_impact_simulator.py example_data/lifecycle_data.csv
```

## License
This project is licensed under the MIT License. 

