"use client";

import { useState } from "react";
import {
  Alert,
  Box,
  Button,
  Card,
  CardContent,
  CircularProgress,
  Container,
  Stack,
  TextField,
  Typography,
} from "@mui/material";
import LocalGasStationIcon from "@mui/icons-material/LocalGasStation";

type FuelPrediction = {
  distance_km: number;
  fuel_price_per_liter: number;
  predicted_liters: number;
  estimated_cost: number;
};

export default function Home() {
  const [distance, setDistance] = useState("");
  const [fuelPrice, setFuelPrice] = useState("");
  const [prediction, setPrediction] = useState<FuelPrediction | null>(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");

  const handleCalculate = async () => {
    setError("");
    setPrediction(null);

    const distanceKm = Number(distance);
    const pricePerLiter = Number(fuelPrice);

    if (distanceKm <= 0 || pricePerLiter <= 0) {
      setError("Ingresá una distancia y un precio mayores a cero.");
      return;
    }

    setLoading(true);

    try {
      const response = await fetch("http://localhost:8000/predict", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
          distance_km: distanceKm,
          fuel_price_per_liter: pricePerLiter,
        }),
      });

      if (!response.ok) {
        throw new Error("No se pudo calcular el costo del viaje.");
      }

      const data: FuelPrediction = await response.json();
      setPrediction(data);
    } catch {
      setError(
        "No pudimos conectar con la API. Verificá que FastAPI esté funcionando.",
      );
    } finally {
      setLoading(false);
    }
  };

  return (
    <Box sx={{ minHeight: "100vh", bgcolor: "#f5f7fb", py: 8 }}>
      <Container maxWidth="sm">
        <Stack spacing={3}>
          <Stack sx={{ alignItems: "center" }} spacing={1}>
            <LocalGasStationIcon sx={{ fontSize: 48, color: "primary.main" }} />

            <Typography
              variant="h3"
              sx={{ fontWeight: 700, textAlign: "center" }}
            >
              FuelCost AI
            </Typography>

            <Typography color="text.secondary" sx={{ textAlign: "center" }}>
              Estimá el consumo y el costo de combustible de tu próximo viaje.
            </Typography>
          </Stack>

          <Card elevation={3} sx={{ borderRadius: 3 }}>
            <CardContent sx={{ p: 4 }}>
              <Stack spacing={3}>
                <Typography variant="h6" sx={{ fontWeight: 600 }}>
                  Datos del viaje
                </Typography>

                <TextField
                  label="Distancia (km)"
                  type="number"
                  fullWidth
                  value={distance}
                  onChange={(event) => setDistance(event.target.value)}
                  slotProps={{
                    htmlInput: { min: 0, step: "any" },
                  }}
                />

                <TextField
                  label="Precio por litro"
                  type="number"
                  fullWidth
                  value={fuelPrice}
                  onChange={(event) => setFuelPrice(event.target.value)}
                  slotProps={{
                    htmlInput: { min: 0, step: "any" },
                  }}
                />

                <Button
                  variant="contained"
                  size="large"
                  fullWidth
                  disabled={loading}
                  onClick={handleCalculate}
                  sx={{ py: 1.5 }}
                >
                  {loading ? (
                    <CircularProgress size={24} color="inherit" />
                  ) : (
                    "Calcular viaje"
                  )}
                </Button>

                {error && <Alert severity="error">{error}</Alert>}
              </Stack>
            </CardContent>
          </Card>

          {prediction && (
            <Stack direction={{ xs: "column", sm: "row" }} spacing={2}>
              <Card sx={{ flex: 1, borderRadius: 3 }}>
                <CardContent>
                  <Typography color="text.secondary" variant="body2">
                    Consumo estimado
                  </Typography>

                  <Typography variant="h4" sx={{ fontWeight: 700 }}>
                    {prediction.predicted_liters.toFixed(2)} L
                  </Typography>
                </CardContent>
              </Card>

              <Card sx={{ flex: 1, borderRadius: 3 }}>
                <CardContent>
                  <Typography color="text.secondary" variant="body2">
                    Costo estimado
                  </Typography>

                  <Typography variant="h4" sx={{ fontWeight: 700 }}>
                    ${prediction.estimated_cost.toLocaleString("es-AR")}
                  </Typography>
                </CardContent>
              </Card>
            </Stack>
          )}
        </Stack>
      </Container>
    </Box>
  );
}
