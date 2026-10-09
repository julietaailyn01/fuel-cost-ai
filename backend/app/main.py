from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from backend.app.services.fuel_service import calculate_fuel_cost

app = FastAPI(
    title="Fuel Cost AI API",
    description="API para estimar el consumo de combustible",
    version ="1.0.0"
)

class FuelPredictionRequest(BaseModel):
    distance_km: float = Field(gt=0, description = "Distancia del viaje en km")
    fuel_price_per_liter: float= Field(gt=0, description="Precio del combustible por litro")

class FuelPredictionResponse(BaseModel):
    distance_km:float
    predicted_liters:float
    fuel_price_per_liter:float
    estimated_cost:float

@app.get("/")
def home ():
    return {
        "message": "FuelCost AI API is running",
        "status": "success"
    }

@app.post("/predict", response_model=FuelPredictionResponse)
def predict_fuel(request: FuelPredictionRequest):
    try:
        return calculate_fuel_cost(request.distance_km, request.fuel_price_per_liter)
    except(OSError, ValueError) as error:
        raise HTTPException(status_code=500, detail="Could not generate fuel prediction") from error
    
