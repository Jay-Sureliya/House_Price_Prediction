import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
from sklearn.metrics import  r2_score


data = pd.read_csv('data.csv')

scaler_cols = ["bedrooms","bathrooms", "sqft_living", "sqft_lot", "condition", "grade", "yr_built", "sqft_above","sqft_basement","view","yr_renovated"]

scaler = StandardScaler()
data[scaler_cols] = scaler.fit_transform(data[scaler_cols])
print(data.head())

X = data.drop("price", axis=1)
y = data["price"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)


model = LinearRegression()
model.fit(X_train, y_train)

m_pred = model.predict(X_test)

print("R2 Score:", round(r2_score(y_test, m_pred)*100, 2),"%")


# USER INPUT FOR PREDICTION

all_features = data.drop("price", axis=1).columns

print("\nPlease provide the following details to predict the house price:")

user_input = {}

for col in all_features:
    user_input[col] = float(input(f"Enter {col}: "))

user_df = pd.DataFrame([user_input])

user_df[scaler_cols] = scaler.transform(user_df[scaler_cols])

predicted_price = model.predict(user_df)[0]

print(f"\nPredicted House Price: ${round(predicted_price, 2)}")