#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split, GridSearchCV
from typing import Tuple

# Define constants for circularity scoring
CIRCULARITY_FACTORS = {
    "recyclability": 0.4,
    "reuse_potential": 0.3,
    "end_of_life_recovery": 0.2,
    "carbon_footprint": -0.1  # Negative as lower is better
}

def calculate_circularity_score(df: pd.DataFrame) -> pd.DataFrame:
    """
    Calculate circularity score for each material in the dataset.

    Parameters:
    df (pd.DataFrame): Input dataframe containing circularity factors.

    Returns:
    pd.DataFrame: DataFrame with an additional column for circularity scores.
    """
    try:
        weights = np.array([CIRCULARITY_FACTORS[factor] for factor in CIRCULARITY_FACTORS.keys()])
        df['circularity_score'] = df[list(CIRCULARITY_FACTORS.keys())].dot(weights)
    except KeyError as e:
        raise KeyError(f"Missing column in input data: {e}")
    return df

def preprocess_data(file_path: str) -> pd.DataFrame:
    """
    Load and preprocess the data.

    Parameters:
    file_path (str): Path to the CSV file containing data.

    Returns:
    pd.DataFrame: Preprocessed DataFrame.
    """
    try:
        df = pd.read_csv(file_path)
        # Check if required columns are present
        missing_columns = [col for col in CIRCULARITY_FACTORS.keys() if col not in df.columns]
        if missing_columns:
            raise ValueError(f"Input data is missing required columns: {missing_columns}")

        # Fill missing values with column means
        df.fillna(df.mean(numeric_only=True), inplace=True)

        # Scale numerical features
        scaler = StandardScaler()
        scaled_features = scaler.fit_transform(df[list(CIRCULARITY_FACTORS.keys())])
        df[list(CIRCULARITY_FACTORS.keys())] = scaled_features
    except FileNotFoundError:
        raise FileNotFoundError(f"The file at {file_path} was not found.")
    except Exception as e:
        raise Exception(f"An error occurred during preprocessing: {e}")
    return df

def visualize_circularity(df: pd.DataFrame) -> None:
    """
    Visualize circularity scores using a bar chart.

    Parameters:
    df (pd.DataFrame): DataFrame containing circularity scores and material names.
    """
    try:
        df = df.sort_values(by='circularity_score', ascending=False)
        plt.figure(figsize=(10, 6))
        plt.bar(df['material'], df['circularity_score'], color='skyblue')
        plt.xlabel('Material')
        plt.ylabel('Circularity Score')
        plt.title('Circularity Scores by Material')
        plt.xticks(rotation=45, ha='right')
        plt.tight_layout()
        plt.show()
    except KeyError as e:
        raise KeyError(f"Missing column for visualization: {e}")

def optimize_material_substitution(df: pd.DataFrame) -> RandomForestRegressor:
    """
    Use a Random Forest model to predict the impact of changing material properties on circularity.

    Parameters:
    df (pd.DataFrame): DataFrame containing features and target variable.

    Returns:
    RandomForestRegressor: Best Random Forest model after hyperparameter tuning.
    """
    try:
        features = list(CIRCULARITY_FACTORS.keys())
        target = 'circularity_score'

        X = df[features]
        y = df[target]

        # Split data
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

        # Define model and hyperparameter tuning
        rf = RandomForestRegressor(random_state=42)
        param_grid = {
            'n_estimators': [50, 100, 200],
            'max_depth': [None, 10, 20],
            'min_samples_split': [2, 5, 10]
        }
        grid_search = GridSearchCV(estimator=rf, param_grid=param_grid, cv=2, scoring='r2')
        grid_search.fit(X_train, y_train)

        best_model = grid_search.best_estimator_

        # Feature importance visualization
        feature_importances = best_model.feature_importances_
        plt.figure(figsize=(8, 5))
        plt.bar(features, feature_importances, color='green')
        plt.xlabel('Feature')
        plt.ylabel('Importance')
        plt.title('Feature Importance in Circularity Prediction')
        plt.tight_layout()
        plt.show()

    except KeyError as e:
        raise KeyError(f"Missing required columns for model training: {e}")
    except ValueError as e:
        raise ValueError(f"Error during model training or hyperparameter tuning: {e}")
    except Exception as e:
        raise Exception(f"An unexpected error occurred: {e}")

    return best_model

def save_results(df: pd.DataFrame, output_path: str) -> None:
    """
    Save DataFrame results to a CSV file.

    Parameters:
    df (pd.DataFrame): DataFrame to save.
    output_path (str): Path to save the CSV file.
    """
    try:
        df.to_csv(output_path, index=False)
        print(f"Results saved to {output_path}")
    except Exception as e:
        raise Exception(f"Failed to save results: {e}")

def main() -> None:
    """
    Main function to execute the Circularity Metrics Analyzer.
    """
    file_path = 'E:/walmart-project/Circularity Metrics Analyzer/packaging_data.csv'  # Example input file
    output_path = 'E:\walmart-project\Circularity Metrics Analyzer\circularity_results.csv'

    try:
        # Load and preprocess data
        print("Loading and preprocessing data...")
        df = preprocess_data(file_path)

        # Calculate circularity scores
        print("Calculating circularity scores...")
        df = calculate_circularity_score(df)

        # Visualize results
        print("Visualizing circularity scores...")
        visualize_circularity(df)

        # Optimize material substitution
        print("Optimizing material substitutions...")
        best_model = optimize_material_substitution(df)
        print("Best Random Forest Model:", best_model)

        # Save results
        save_results(df, output_path)

    except Exception as e:
        print(f"An error occurred during execution: {e}")

if __name__ == "__main__":
    main()

