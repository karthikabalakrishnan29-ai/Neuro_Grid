from fastapi import FastAPI
from api_layer.routes import twin_routes, forecast_routes, anomaly_routes, control_routes, scenario_routes

app = FastAPI(title="Intelligent Microgrid Digital Twin API", version="1.0.0")

# Registering all routes
app.include_router(twin_routes.router, prefix="/api/twin", tags=["Digital Twin"])
app.include_router(forecast_routes.router, prefix="/api/forecast", tags=["Forecasting"])
app.include_router(anomaly_routes.router, prefix="/api/anomaly", tags=["Anomaly Detection"])
app.include_router(control_routes.router, prefix="/api/control", tags=["Control Layer"])
app.include_router(scenario_routes.router, prefix="/api/scenario", tags=["Scenarios"])

@app.get("/")
def read_root():
    return {"message": "Microgrid API is Live and Running!"}