# Circularity Metrics Analyzer

## Overview
The **Circularity Metrics Analyzer** is a Python-powered tool designed to evaluate and optimize packaging materials for sustainability and circularity. By leveraging machine learning and visualization techniques, it provides actionable insights to improve material circularity and reduce environmental impact.

## Features
- **Circularity Score Calculation:** Computes circularity scores based on weighted metrics like recyclability, reuse potential, and carbon footprint.
- **Data Preprocessing:** Handles missing values, scales numerical features, and validates dataset integrity.
- **Visualization:** Generates professional bar charts to display circularity scores for different materials.
- **AI-Powered Optimization:** Utilizes Random Forest Regressor with hyperparameter tuning to suggest material improvements.
- **Error Handling:** Ensures robust execution with meaningful error messages for missing data, invalid inputs, and other issues.

## Installation

### Prerequisites
- Python 3.8+
- Libraries: `pandas`, `numpy`, `matplotlib`, `sklearn`

### Step

1. Install the required libraries:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

### Input Data Requirements
- A CSV file containing the following columns:
  - `material`: Name or identifier of the material.
  - `recyclability`: Float value representing material recyclability.
  - `reuse_potential`: Float value indicating potential for reuse.
  - `end_of_life_recovery`: Float value for recovery potential at the end of the lifecycle.
  - `carbon_footprint`: Float value for carbon footprint (lower is better).

### Running the Script
1. Prepare your dataset and save it as `packaging_data.csv` in the project directory.
2. Execute the script:
   ```bash
   python circularity_metrics_analyzer.py
   ```
3. Results:
   - **Circularity scores** will be computed and visualized.
   - Optimized recommendations will be displayed.
   - A CSV file with results will be saved as `circularity_results.csv`.

### Example Input
```csv
material,recyclability,reuse_potential,end_of_life_recovery,carbon_footprint
Material A,0.8,0.7,0.9,0.2
Material B,0.6,0.5,0.4,0.3
Material C,0.7,0.6,0.8,0.1
```

### Example Output
```csv
material,recyclability,reuse_potential,end_of_life_recovery,carbon_footprint,circularity_score
Material A,0.8,0.7,0.9,0.2,1.042
Material B,0.6,0.5,0.4,0.3,-1.258
Material C,0.7,0.6,0.8,0.1,0.215
```

## Roadmap
- Add support for additional circularity metrics and visualizations.
- Integrate with external APIs for real-time sustainability data.
- Expand AI models to include lifecycle cost analysis.

## Contributing
Contributions are welcome!

## License
This project is licensed under the MIT License. 

