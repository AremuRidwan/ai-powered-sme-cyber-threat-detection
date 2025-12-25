from src.evaluation import evaluate_model
import joblib
model = joblib.load("model.pkl")
report, matrix = evaluate_model(model, X_test, y_test)
print(report)
print(matrix)

