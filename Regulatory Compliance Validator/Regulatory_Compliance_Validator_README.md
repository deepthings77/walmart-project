# Regulatory Compliance Validator

The **Regulatory Compliance Validator** is a Python-based tool designed to validate organizational compliance with regulatory requirements. It merges compliance data with regulatory thresholds, identifies non-compliance, and generates actionable summaries and reports.

## Features
- **Data Validation**:
  - Ensures required fields are present in both compliance data and regulations files.
- **Compliance Checking**:
  - Validates whether entities meet the required thresholds for each regulatory requirement.
- **Summary Generation**:
  - Provides detailed compliance summaries at both entity and overall levels.
- **Non-Compliance Flagging**:
  - Highlights entities and requirements where compliance is not met.
- **Export Reports**:
  - Saves compliance results to a CSV file for further analysis or record-keeping.
- **Logging**:
  - Tracks execution flow and errors for debugging and transparency.

## Setup
### Prerequisites
Ensure you have Python 3.7 or above installed.

### Installation
1. Install required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

### Input Data
Prepare the following CSV files:
1. **Compliance Data File**:
   - Contains organizational data to be validated.
   - Required columns: `Entity`, `Requirement`, `Status`, `Date`.

2. **Regulations File**:
   - Contains regulatory thresholds.
   - Required columns: `Requirement`, `Description`, `Threshold`.

### Running the Validator
To validate compliance and generate outputs:
```bash
python regulatory_compliance_validator.py compliance_data.csv regulations.csv
```

## Outputs
1. **Console Summaries**:
   - Entity-level compliance summary.
   - Overall compliance statistics.
2. **CSV Report**:
   - Detailed compliance results saved to `compliance_report.csv`.
3. **Non-Compliance Report**:
   - List of non-compliant entities and their failed requirements.

## Example Workflow
1. Prepare `compliance_data.csv` and `regulations.csv`.
2. Run the script:
   ```bash
   python regulatory_compliance_validator.py compliance_data.csv regulations.csv
   ```
3. Review the console output for summaries and non-compliance.
4. Open the generated `compliance_report.csv` for detailed results.

## License
This project is licensed under the MIT License.
