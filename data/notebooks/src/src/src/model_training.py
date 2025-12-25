from src.model_training import train_model
import pandas as pd
data = pd.read_csv("data/processed/processed_data.csv")

X = data.drop(columns=["Label"]).values
y = data["Label"]

model, X_test, y_test = train_model(X, y)

