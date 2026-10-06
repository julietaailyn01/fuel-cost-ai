import numpy as np
import pandas as pd

from pathlib import Path

rng= np.random.default_rng(42)

n_samples = 500

distance_km= rng.uniform(low=10, high=800, size=n_samples)

fuel_per_km = 8/100

base_fuel_consumption = distance_km * fuel_per_km

noise = rng.normal(loc=0, scale=1.5, size=n_samples)

fuel_consumption = base_fuel_consumption + noise
print(fuel_consumption.min())

fuel_consumption = np.clip(fuel_consumption, a_min=0, a_max=None)

data= pd.DataFrame({
    'distance_km': distance_km,
    'fuel_consumption': fuel_consumption
})
print(data['fuel_consumption'].min())

project_root = Path(__file__).resolve().parents[2]

data_path = project_root/"ml"/"data"/"fuel_consumption.csv"

data.to_csv(data_path, index=False)

print(f"Dataset guardado en: {data_path}")