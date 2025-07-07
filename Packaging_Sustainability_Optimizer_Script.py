#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd
import numpy as np
from scipy.optimize import minimize
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import argparse

class PackagingSustainabilityOptimizer:
    def __init__(self, data_file):
        """
        Initialize the optimizer with data from a CSV file.
        The CSV should have columns: 'Material', 'Cost_per_unit', 'Recyclability', 'Carbon_Footprint', 'Durability'.
        """
        self.data = pd.read_csv(data_file)
        self._validate_data()

    def _validate_data(self):
        """Validate the input data format."""
        required_columns = ['Material', 'Cost_per_unit', 'Recyclability', 'Carbon_Footprint', 'Durability']
        for col in required_columns:
            if col not in self.data.columns:
                raise ValueError(f"Missing required column: {col}")

    def normalize_columns(self):
        """Normalize columns for comparison purposes."""
        columns_to_normalize = ['Cost_per_unit', 'Recyclability', 'Carbon_Footprint', 'Durability']
        for col in columns_to_normalize:
            if col in self.data.columns:
                self.data[f"{col}_normalized"] = (
                    (self.data[col] - self.data[col].min()) /
                    (self.data[col].max() - self.data[col].min())
                )

    def optimize(self, weight_cost=0.3, weight_recyclability=0.4, weight_carbon_footprint=0.2, weight_durability=0.1):
        """
        Perform optimization to find the most sustainable packaging.

        Weights:
        - weight_cost: Weight for cost efficiency
        - weight_recyclability: Weight for recyclability
        - weight_carbon_footprint: Weight for carbon footprint reduction
        - weight_durability: Weight for durability
        """
        self.normalize_columns()

        def objective_function(x):
            """Objective function to minimize."""
            return (
                weight_cost * x[0] +
                weight_recyclability * (1 - x[1]) +  # Higher recyclability is better, so subtract from 1
                weight_carbon_footprint * x[2] +
                weight_durability * (1 - x[3])  # Higher durability is better, so subtract from 1
            )

        results = []
        for index, row in self.data.iterrows():
            x0 = [row['Cost_per_unit_normalized'], row['Recyclability_normalized'],
                  row['Carbon_Footprint_normalized'], row['Durability_normalized']]

            res = minimize(objective_function, x0, bounds=[(0, 1)] * 4)
            results.append((row['Material'], res.fun))

        self.optimized_results = sorted(results, key=lambda x: x[1])
        return self.optimized_results

    def display_results(self):
        """Display the optimization results."""
        if not hasattr(self, 'optimized_results'):
            raise ValueError("Run optimize() before displaying results.")

        print("\nSustainable Packaging Recommendations:\n")
        print("Material\t\tScore")
        print("--------------------------------")
        for material, score in self.optimized_results:
            print(f"{material}\t\t{score:.2f}")

    def export_results(self, output_file="optimized_results.csv"):
        """Export optimization results to a CSV file."""
        if not hasattr(self, 'optimized_results'):
            raise ValueError("Run optimize() before exporting results.")

        results_df = pd.DataFrame(self.optimized_results, columns=['Material', 'Score'])
        results_df.to_csv(output_file, index=False)
        print(f"Results exported to {output_file}")

    def visualize_results(self):
        """Visualize the optimization results as a professional bar chart."""
        if not hasattr(self, 'optimized_results'):
            raise ValueError("Run optimize() before visualizing results.")

        materials = [result[0] for result in self.optimized_results]
        scores = [result[1] for result in self.optimized_results]

        plt.figure(figsize=(12, 8))
        sns.barplot(x=scores, y=materials, palette="viridis")
        plt.xlabel('Sustainability Score', fontsize=14)
        plt.ylabel('Material', fontsize=14)
        plt.title('Sustainability Optimization Results', fontsize=16)
        plt.xticks(fontsize=12)
        plt.yticks(fontsize=12)
        plt.grid(axis='x', linestyle='--', alpha=0.7)
        plt.tight_layout()
        plt.show()

    def visualize_metric_breakdown(self):
        """Visualize the breakdown of metrics for each material."""
        normalized_columns = ['Cost_per_unit_normalized', 'Recyclability_normalized', 'Carbon_Footprint_normalized', 'Durability_normalized']
        if not all(col in self.data.columns for col in normalized_columns):
            raise ValueError("Normalized columns are missing. Run normalize_columns() before visualizing metrics.")

        melted_data = self.data[['Material'] + normalized_columns].melt(id_vars='Material', var_name='Metric', value_name='Value')

        plt.figure(figsize=(14, 8))
        sns.barplot(x='Value', y='Material', hue='Metric', data=melted_data, palette='pastel')
        plt.xlabel('Normalized Value', fontsize=14)
        plt.ylabel('Material', fontsize=14)
        plt.title('Metric Breakdown by Material', fontsize=16)
        plt.legend(title='Metric', fontsize=12, title_fontsize=14)
        plt.xticks(fontsize=12)
        plt.yticks(fontsize=12)
        plt.grid(axis='x', linestyle='--', alpha=0.7)
        plt.tight_layout()
        plt.show()

    def visualize_results_interactive(self):
        """Visualize optimization results interactively using Plotly."""
        if not hasattr(self, 'optimized_results'):
            raise ValueError("Run optimize() before visualizing results.")

        results_df = pd.DataFrame(self.optimized_results, columns=['Material', 'Score'])
        fig = px.bar(results_df, x='Score', y='Material', orientation='h', 
                     title='Sustainability Optimization Results (Interactive)',
                     labels={'Score': 'Sustainability Score', 'Material': 'Material'},
                     text='Score', color='Score', color_continuous_scale='Viridis')
        fig.update_layout(title_font_size=18, xaxis_title='Sustainability Score', yaxis_title='Material')
        fig.show()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Packaging Sustainability Optimizer")
    parser.add_argument("data_file", type=str, help="Path to the CSV file containing packaging data")
    parser.add_argument("--output_file", type=str, default="optimized_results.csv", help="File name for exporting results")
    parser.add_argument("--weight_cost", type=float, default=0.3, help="Weight for cost efficiency")
    parser.add_argument("--weight_recyclability", type=float, default=0.4, help="Weight for recyclability")
    parser.add_argument("--weight_carbon_footprint", type=float, default=0.2, help="Weight for carbon footprint")
    parser.add_argument("--weight_durability", type=float, default=0.1, help="Weight for durability")

    args = parser.parse_args()

    optimizer = PackagingSustainabilityOptimizer(args.data_file)

    # Run optimization
    results = optimizer.optimize(
        weight_cost=args.weight_cost,
        weight_recyclability=args.weight_recyclability,
        weight_carbon_footprint=args.weight_carbon_footprint,
        weight_durability=args.weight_durability
    )

    # Display results
    optimizer.display_results()

    # Export results
    optimizer.export_results(output_file=args.output_file)

    # Visualize results
    optimizer.visualize_results()

    # Visualize metric breakdown
    optimizer.visualize_metric_breakdown()

    # Interactive visualization
    optimizer.visualize_results_interactive()

