#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.optimize import minimize
import logging
from concurrent.futures import ThreadPoolExecutor

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class LifecycleImpactSimulator:
    def __init__(self, data_file):
        """
        Initialize the simulator with lifecycle impact data from a CSV file.
        The CSV should have columns: 'Stage', 'Cost', 'Carbon_Footprint', 'Water_Usage', 'Energy_Consumption'.
        """
        logging.info("Initializing Lifecycle Impact Simulator.")
        self.data = pd.read_csv(data_file)
        self._validate_data()

    def _validate_data(self):
        """Validate the input data format."""
        logging.info("Validating input data.")
        required_columns = ['Stage', 'Cost', 'Carbon_Footprint', 'Water_Usage', 'Energy_Consumption']
        for col in required_columns:
            if col not in self.data.columns:
                logging.error(f"Missing required column: {col}")
                raise ValueError(f"Missing required column: {col}")

    def normalize_columns(self):
        """Normalize columns for comparison purposes."""
        logging.info("Normalizing columns for simulation.")
        columns_to_normalize = ['Cost', 'Carbon_Footprint', 'Water_Usage', 'Energy_Consumption']
        for col in columns_to_normalize:
            if col in self.data.columns:
                self.data[f"{col}_normalized"] = (
                    (self.data[col] - self.data[col].min()) /
                    (self.data[col].max() - self.data[col].min())
                )

    def simulate(self, weight_cost=0.3, weight_carbon=0.3, weight_water=0.2, weight_energy=0.2):
        """
        Simulate lifecycle impact based on weighted criteria.

        Weights:
        - weight_cost: Weight for cost efficiency.
        - weight_carbon: Weight for reducing carbon footprint.
        - weight_water: Weight for minimizing water usage.
        - weight_energy: Weight for reducing energy consumption.
        """
        logging.info("Starting simulation with weights: cost=%s, carbon=%s, water=%s, energy=%s",
                     weight_cost, weight_carbon, weight_water, weight_energy)
        self.normalize_columns()

        def objective_function(x):
            """Objective function to minimize."""
            return (
                weight_cost * x[0] +
                weight_carbon * x[1] +
                weight_water * x[2] +
                weight_energy * x[3]
            )

        results = []

        def process_row(row):
            x0 = [row['Cost_normalized'], row['Carbon_Footprint_normalized'],
                  row['Water_Usage_normalized'], row['Energy_Consumption_normalized']]
            res = minimize(objective_function, x0, bounds=[(0, 1)] * 4)
            return row['Stage'], res.fun

        with ThreadPoolExecutor() as executor:
            results = list(executor.map(process_row, [row for _, row in self.data.iterrows()]))

        self.simulation_results = sorted(results, key=lambda x: x[1])
        logging.info("Simulation completed.")
        return self.simulation_results

    def display_results(self):
        """Display the simulation results."""
        if not hasattr(self, 'simulation_results'):
            logging.error("Attempted to display results before running simulation.")
            raise ValueError("Run simulate() before displaying results.")

        print("\nLifecycle Impact Simulation Results:\n")
        print("Stage\t\tImpact Score")
        print("--------------------------------")
        for stage, score in self.simulation_results:
            print(f"{stage}\t\t{score:.2f}")

    def visualize_results(self):
        """Visualize the simulation results as a bar chart."""
        if not hasattr(self, 'simulation_results'):
            logging.error("Attempted to visualize results before running simulation.")
            raise ValueError("Run simulate() before visualizing results.")

        stages = [result[0] for result in self.simulation_results]
        scores = [result[1] for result in self.simulation_results]

        plt.figure(figsize=(10, 6))
        sns.barplot(x=scores, y=stages, palette="coolwarm")
        plt.xlabel('Impact Score', fontsize=14)
        plt.ylabel('Lifecycle Stage', fontsize=14)
        plt.title('Lifecycle Impact Simulation Results', fontsize=16)
        plt.tight_layout()
        plt.show()

    def export_results(self, output_file="simulation_results.csv"):
        """Export simulation results to a CSV file."""
        if not hasattr(self, 'simulation_results'):
            logging.error("Attempted to export results before running simulation.")
            raise ValueError("Run simulate() before exporting results.")

        results_df = pd.DataFrame(self.simulation_results, columns=['Stage', 'Impact_Score'])
        results_df.to_csv(output_file, index=False)
        logging.info(f"Results exported to {output_file}")

if __name__ == "__main__":
    # Example usage
    data_file = "E:/walmart-project/Lifecycle Impact Simulator/lifecycle_data.csv"  # Replace with the actual path to your data file
    simulator = LifecycleImpactSimulator(data_file)

    # Run simulation
    results = simulator.simulate()

    # Display results
    simulator.display_results()

    # Visualize results
    simulator.visualize_results()

    # Export results
    simulator.export_results()

