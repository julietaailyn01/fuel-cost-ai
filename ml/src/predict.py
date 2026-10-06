import numpy as np
from pathlib import Path

from linear_regression import predict


# Model path
project_root = Path(__file__).resolve().parents[2]
model_path = project_root / "ml" / "models" / "linear_regression_model.npz"


# Load trained model
model = np.load(model_path)

w = model["w"]
b = model["b"]


def predict_fuel_consumption(distance_km):
    estimated_fuel = predict(distance_km, w, b)

    return float(estimated_fuel)


if __name__ == "__main__":
    distance = 250

    prediction = predict_fuel_consumption(distance)

    print(f"Distance: {distance} km")
    print(f"Estimated fuel consumption: {prediction:.2f} liters")