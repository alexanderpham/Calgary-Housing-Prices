# COMP 4630 - Assignment 1
# Group: Alex Pham, Matt Manolov, Zakie Shah
# Due date: Jan 31, 2025 @ 5pm

import pandas as pd
import numpy as np
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
import joblib
import matplotlib.pyplot as plt

""" 
Function: predict

Inputs: dataframe with the data that the model will make predictions

Outputs: array of predictions based on the input data

Purpose: loads the training model from the pipeline to make the predictions
"""
def predict(data: pd.DataFrame) -> np.ndarray:
    pipeline = joblib.load("housing_pipeline.pkl") 
    # predict using the pipeline
    predictions = pipeline.predict(data)
    return predictions

# Function to plot predictions vs actual values
def plot_predictions(y_true: pd.Series, y_pred: np.ndarray):
    plt.figure(figsize=(10, 6))
    plt.scatter(y_true, y_pred, alpha=0.6, color='blue', label='Predictions')
    plt.plot([y_true.min(), y_true.max()], [y_true.min(), y_true.max()], color='red', linestyle='--', label='Ideal Fit')
    plt.xlabel('Actual Assessed Value')
    plt.ylabel('Predicted Assessed Value')
    plt.title('Predictions vs Actual Assessed Values')
    plt.legend()
    plt.grid(True)
    plt.show()

# testing our predict function
if __name__ == "__main__":

    test_set = pd.read_csv("test_set.csv")

    # separating features and target columns in the test set
    X_test = test_set.drop("ASSESSED_VALUE", axis=1)  
    y_test = test_set["ASSESSED_VALUE"]               

    # predict the assessed values 
    predicted_values = predict(X_test)

    # evaluating the performance of the model
    mae = mean_absolute_error(y_test, predicted_values)
    mse = mean_squared_error(y_test, predicted_values)
    r2 = r2_score(y_test, predicted_values)

    print("Mean Absolute Error (MAE):", mae)
    print("Mean Squared Error (MSE):", mse)
    print("R-squared Score:", r2)

    # plot the predictions vs actual values
    plot_predictions(y_test, predicted_values)
