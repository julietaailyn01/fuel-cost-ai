import numpy as np
import pandas as pd
from pathlib import Path

from linear_regression import predict, gradient_descent


# Paths
project_root = Path(__file__).resolve().parents[2]

data_path = project_root / "ml" / "data" / "fuel_consumption.csv"
model_path = project_root / "ml" / "models" / "linear_regression_model.npz"


# Load dataset
data = pd.read_csv(data_path)

X = data["distance_km"].to_numpy()
y = data["fuel_consumption"].to_numpy()


# Train / test split
rng = np.random.default_rng(42)
indices = rng.permutation(len(X))

split_index = int(len(X) * 0.8)

train_indices = indices[:split_index]
test_indices = indices[split_index:]

X_train = X[train_indices]
y_train = y[train_indices]

X_test = X[test_indices]
y_test = y[test_indices]


# Train model
initial_w = 0.0
initial_b = 0.0

learning_rate = 0.000001
iterations = 5000

w, b, cost_history = gradient_descent(
    X_train,
    y_train,
    initial_w,
    initial_b,
    learning_rate,
    iterations
)


# Evaluate model
train_predictions = predict(X_train, w, b)
test_predictions = predict(X_test, w, b)

train_mae = np.mean(np.abs(train_predictions - y_train))
test_mae = np.mean(np.abs(test_predictions - y_test))


# Save model
model_path.parent.mkdir(parents=True, exist_ok=True)

np.savez(
    model_path,
    w=w,
    b=b
)


# Results
print(f"w: {w}")
print(f"b: {b}")
print(f"Train MAE: {train_mae:.2f} liters")
print(f"Test MAE: {test_mae:.2f} liters")
print(f"Model saved to: {model_path}")