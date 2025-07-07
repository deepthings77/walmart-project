#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd
import logging
from datetime import datetime

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class RegulatoryComplianceValidator:
    def __init__(self, data_file, regulations_file):
        """
        Initialize the validator with compliance data and regulations.

        Parameters:
        - data_file (str): Path to the CSV file containing compliance data.
        - regulations_file (str): Path to the CSV file containing regulatory requirements.
        """
        logging.info("Initializing Regulatory Compliance Validator.")
        self.data = pd.read_csv(data_file)
        self.regulations = pd.read_csv(regulations_file)
        self._validate_data()

    def _validate_data(self):
        """Validate the input data format."""
        logging.info("Validating input data format.")
        required_data_columns = ['Entity', 'Requirement', 'Status', 'Date']
        required_regulation_columns = ['Requirement', 'Description', 'Threshold']

        for col in required_data_columns:
            if col not in self.data.columns:
                logging.error(f"Missing required column in data: {col}")
                raise ValueError(f"Missing required column in data: {col}")

        for col in required_regulation_columns:
            if col not in self.regulations.columns:
                logging.error(f"Missing required column in regulations: {col}")
                raise ValueError(f"Missing required column in regulations: {col}")

    def check_compliance(self):
        """
        Check compliance of entities against regulatory requirements.

        Adds a 'Compliance' column to the data indicating whether each entity is compliant or non-compliant.
        """
        logging.info("Checking compliance.")
        self.data = self.data.merge(self.regulations, on='Requirement', how='left')

        self.data['Compliance'] = self.data.apply(
            lambda row: 'Compliant' if row['Status'] >= row['Threshold'] else 'Non-Compliant', axis=1
        )

    def generate_compliance_summary(self):
        """
        Generate a summary of compliance by entity and overall.

        Prints a detailed summary of compliance at both the entity and overall levels.
        """
        logging.info("Generating compliance summary.")
        if 'Compliance' not in self.data.columns:
            logging.error("Compliance check not performed. Run check_compliance() first.")
            raise ValueError("Run check_compliance() before generating summary.")

        summary = self.data.groupby(['Entity', 'Compliance']).size().unstack(fill_value=0)
        overall_summary = self.data['Compliance'].value_counts()

        print("\nEntity-Level Compliance Summary:\n")
        print(summary)

        print("\nOverall Compliance Summary:\n")
        print(overall_summary)

    def export_compliance_report(self, output_file="compliance_report.csv"):
        """
        Export the compliance results to a CSV file.

        Parameters:
        - output_file (str): Path to the output CSV file.
        """
        logging.info(f"Exporting compliance report to {output_file}.")
        if 'Compliance' not in self.data.columns:
            logging.error("Compliance check not performed. Run check_compliance() first.")
            raise ValueError("Run check_compliance() before exporting report.")

        self.data.to_csv(output_file, index=False)
        logging.info(f"Compliance report exported successfully to {output_file}.")

    def flag_non_compliance(self):
        """
        Identify and display entities that are non-compliant.

        Prints a detailed list of non-compliant entities and their failed requirements.
        """
        logging.info("Flagging non-compliant entities.")
        if 'Compliance' not in self.data.columns:
            logging.error("Compliance check not performed. Run check_compliance() first.")
            raise ValueError("Run check_compliance() before flagging non-compliance.")

        non_compliant = self.data[self.data['Compliance'] == 'Non-Compliant']
        print("\nNon-Compliant Entities:\n")
        print(non_compliant[['Entity', 'Requirement', 'Status', 'Threshold']])

if __name__ == "__main__":
    # Example usage
    data_file = "E:/walmart-project/Regulatory Compliance Validator/compliance_data.csv"  # Replace with the path to your compliance data file
    regulations_file = "E:/walmart-project/Regulatory Compliance Validator/regulations.csv"  # Replace with the path to your regulations file

    try:
        validator = RegulatoryComplianceValidator(data_file, regulations_file)

        # Perform compliance checks
        validator.check_compliance()

        # Generate and display summaries
        validator.generate_compliance_summary()

        # Flag non-compliance
        validator.flag_non_compliance()

        # Export compliance report
        validator.export_compliance_report("compliance_report.csv")

    except Exception as e:
        logging.error(f"An error occurred: {e}")

