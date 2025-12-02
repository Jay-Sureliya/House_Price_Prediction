🎯 HOUSE PRICE PREDICTION

📘 Overview
The House Price Prediction project focuses on building a machine learning model that predicts house prices based on multiple features such as bedrooms, bathrooms, square footage, year built, and more. The project uses Linear Regression and incorporates feature scaling, train-test splitting, and interactive user input for predictions.

This script ensures that the dataset is ready for modeling, scales relevant features, trains a regression model, evaluates its performance, and allows users to predict house prices by providing custom inputs.

🧠 Project Objective
To create an automated house price prediction pipeline that:

Handles multiple numeric and categorical features efficiently.

Scales numeric features for better regression performance.

Splits data into training and testing sets for model evaluation.

Allows interactive predictions based on user-provided house details.

Produces accurate and interpretable predictions.

📂 Dataset Description

Input file: data.csv
Columns:

| Column        | Description                             |
| ------------- | --------------------------------------- |
| bedrooms      | Number of bedrooms in the house         |
| bathrooms     | Number of bathrooms                     |
| sqft_living   | Square footage of the living area       |
| sqft_lot      | Total square footage of the lot         |
| floors        | Number of floors                        |
| waterfront    | 1 if the house has a waterfront, else 0 |
| view          | View rating of the house                |
| condition     | Overall condition rating                |
| grade         | Construction grade                      |
| sqft_above    | Square footage above ground             |
| sqft_basement | Square footage of basement              |
| yr_built      | Year the house was built                |
| yr_renovated  | Year the house was renovated            |
| price         | Target variable – house price           |


⚙️ Processing Steps

Load Raw Data

Loads data.csv safely and displays the first few rows.

Feature Scaling

Scales numeric features such as bedrooms, bathrooms, square footage, condition, grade, etc., using StandardScaler.

Split Data into Features and Target

Separates price as the target variable and all other columns as features.

Train-Test Split

Splits the dataset into 80% training and 20% testing sets to evaluate model performance.

Train Linear Regression Model

Fits a Linear Regression model on the training data.

Model Evaluation

Predicts on the test set and computes R² Score to measure model accuracy.

User Input for Prediction

Prompts the user to enter values for all features.

Scales the user input features using the same scaler.

Predicts the house price using the trained model.

📈 Model Evaluation

R2 Score: 99.66 %


The high R² Score indicates that the model predicts house prices accurately on the test set.
