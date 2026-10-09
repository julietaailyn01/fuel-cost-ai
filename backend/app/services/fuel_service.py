from ml.src.predict import predict_fuel_consumption


def calculate_fuel_cost(
    distance_km: float,
    fuel_price_per_liter: float,
) -> dict:
    predicted_liters = float(
        predict_fuel_consumption(distance_km)
    )

    estimated_cost = predicted_liters * fuel_price_per_liter

    return {
        "distance_km": distance_km,
        "fuel_price_per_liter": fuel_price_per_liter,
        "predicted_liters": round(predicted_liters, 2),
        "estimated_cost": round(estimated_cost, 2),
    }