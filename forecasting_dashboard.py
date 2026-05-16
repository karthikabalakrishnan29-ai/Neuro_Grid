import streamlit as st
import pandas as pd
import plotly.express as px
from models.forecasting.model_loader import ForecastingLoader

def show():
    st.header("🔮 AI Load Forecasting")
    
    # Load Model
    loader = ForecastingLoader()
    model = loader.load_trained_model()
    
    # Simulate Future 24 hours
    # Real-time-la inga namma API layer-a call pannuvom
    st.subheader("Next 24 Hours Prediction")
    chart_data = pd.DataFrame({
        'Hour': list(range(24)),
        'Predicted Load (kW)': [15.2, 14.8, 14.1, 13.5, 18.0, 22.0, 25.5, 24.0, 20.0, 18.0, 16.0, 15.0, 15.2, 14.8, 14.1, 13.5, 18.0, 22.0, 25.5, 24.0, 20.0, 18.0, 16.0, 15.0]
    })
    
    fig = px.line(chart_data, x='Hour', y='Predicted Load (kW)', title="Demand Forecast")
    st.plotly_chart(fig, use_container_width=True)

if __name__ == "__main__":
    show()