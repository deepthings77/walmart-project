#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import logging
from datetime import datetime
from plotly import express as px

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class SustainabilityKPITracker:
    def __init__(self, data_file):
        """
        Initialize the tracker with sustainability KPI data from a CSV file.
        The CSV should have columns: 'KPI', 'Target', 'Actual', 'Date'.
        """
        logging.info("Initializing Sustainability KPI Tracker.")
        self.data = pd.read_csv(data_file, parse_dates=['Date'])
        self._validate_data()

    def _validate_data(self):
        """Validate the input data format."""
        logging.info("Validating input data.")
        required_columns = ['KPI', 'Target', 'Actual', 'Date']
        for col in required_columns:
            if col not in self.data.columns:
                logging.error(f"Missing required column: {col}")
                raise ValueError(f"Missing required column: {col}")

    def calculate_performance(self):
        """Calculate performance metrics for each KPI."""
        logging.info("Calculating performance metrics.")
        self.data['Performance'] = (self.data['Actual'] / self.data['Target']) * 100
        self.data['Status'] = self.data['Performance'].apply(
            lambda x: 'On Track' if x >= 100 else 'Needs Improvement'
        )

    def display_summary(self):
        """Display a summary of the KPI performance."""
        logging.info("Displaying KPI summary.")
        if 'Performance' not in self.data.columns:
            logging.error("Performance metrics not calculated. Run calculate_performance() first.")
            raise ValueError("Run calculate_performance() before displaying summary.")

        summary = self.data.groupby('KPI').agg({
            'Performance': 'mean',
            'Status': lambda x: (x == 'On Track').sum()
        }).rename(columns={'Performance': 'Average Performance', 'Status': 'On Track Count'})

        print("\nSustainability KPI Summary:\n")
        print(summary)

    def visualize_performance(self):
        """Visualize the performance of KPIs as a bar chart."""
        logging.info("Visualizing KPI performance.")
        if 'Performance' not in self.data.columns:
            logging.error("Performance metrics not calculated. Run calculate_performance() first.")
            raise ValueError("Run calculate_performance() before visualizing performance.")

        plt.figure(figsize=(12, 6))
        sns.barplot(x='KPI', y='Performance', hue='Status', data=self.data, palette='coolwarm')
        plt.axhline(100, color='green', linestyle='--', label='Target Met')
        plt.title('Sustainability KPI Performance', fontsize=16)
        plt.xlabel('KPI', fontsize=14)
        plt.ylabel('Performance (%)', fontsize=14)
        plt.legend(title='Status', fontsize=12)
        plt.xticks(rotation=45, fontsize=12)
        plt.tight_layout()
        plt.show()

    def visualize_interactive(self):
        """Visualize KPI performance interactively using Plotly."""
        logging.info("Creating interactive visualization.")
        if 'Performance' not in self.data.columns:
            logging.error("Performance metrics not calculated. Run calculate_performance() first.")
            raise ValueError("Run calculate_performance() before visualizing performance.")

        fig = px.bar(
            self.data,
            x='KPI',
            y='Performance',
            color='Status',
            text='Performance',
            title='Interactive Sustainability KPI Performance',
            labels={"Performance": "Performance (%)", "KPI": "Key Performance Indicator"},
            template='plotly_white'
        )
        fig.update_traces(texttemplate='%{text:.2f}%', textposition='outside')
        fig.add_hline(y=100, line_dash="dash", line_color="green", annotation_text="Target Met")
        fig.show()

    def export_results(self, output_file="kpi_performance_summary.csv"):
        """Export the KPI performance results to a CSV file."""
        logging.info(f"Exporting results to {output_file}.")
        if 'Performance' not in self.data.columns:
            logging.error("Performance metrics not calculated. Run calculate_performance() first.")
            raise ValueError("Run calculate_performance() before exporting results.")

        self.data.to_csv(output_file, index=False)
        logging.info(f"Results exported successfully to {output_file}.")

    def add_trend_analysis(self):
        """Perform trend analysis on KPIs over time."""
        logging.info("Performing trend analysis on KPIs.")
        trend_data = self.data.groupby(['Date', 'KPI'])['Performance'].mean().reset_index()

        plt.figure(figsize=(14, 7))
        sns.lineplot(data=trend_data, x='Date', y='Performance', hue='KPI', marker="o")
        plt.axhline(100, color='green', linestyle='--', label='Target Met')
        plt.title('KPI Performance Trend Over Time', fontsize=16)
        plt.xlabel('Date', fontsize=14)
        plt.ylabel('Performance (%)', fontsize=14)
        plt.legend(title='KPI', fontsize=12)
        plt.xticks(rotation=45, fontsize=12)
        plt.tight_layout()
        plt.show()

if __name__ == "__main__":
    # Example usage
    data_file = "sustainability_kpis.csv"  # Replace with the path to your KPI data file
    tracker = SustainabilityKPITracker(data_file)

    # Calculate performance metrics
    tracker.calculate_performance()

    # Display a summary of performance
    tracker.display_summary()

    # Visualize performance
    tracker.visualize_performance()

    # Create interactive visualization
    tracker.visualize_interactive()

    # Perform trend analysis
    tracker.add_trend_analysis()

    # Export results
    tracker.export_results("kpi_performance_summary.csv")

