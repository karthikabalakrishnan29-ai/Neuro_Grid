# Safety limits for the Microgrid
# Intha values-a thaanduna AI 'Anomaly' nu trigger pannum.

GRID_LIMITS = {
    "voltage": {
        "min": 210.0,  # Volts
        "max": 245.0
    },
    "frequency": {
        "min": 48.5,   # Hz
        "max": 51.5
    },
    "current_max": 30.0 # Amps
}

MODEL_PARAMS = {
    "contamination": 0.05, # 5% data outliers-ah irukkalam
    "random_state": 42
}