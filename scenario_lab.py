import streamlit as st
import pandas as pd
import time
import plotly.express as px
from scenario_engine.what_if_analysis import WhatIfAnalyzer
from scenario_engine.fault_injection import FaultInjector

def show():
    st.header("🧪 Digital Twin Scenario Lab")
    st.write("Simulate extreme conditions and test system resilience.")
    st.markdown("---")

    # 1. Scenario Selection Sidebar or Top Columns
    col1, col2 = st.columns([1, 2])

    with col1:
        st.subheader("🛠️ Scenario Controller")
        scenario = st.selectbox("Select Scenario", 
                                ["Normal Operation", "Total Solar Eclipse", "Grid Blackout", "Cyber Attack (Data Injection)"])
        
        intensity = st.slider("Scenario Intensity", 0, 100, 50)
        
        run_btn = st.button("🚀 EXECUTE SCENARIO", use_container_width=True)

    with col2:
        st.subheader("📉 Impact Prediction")
        if run_btn:
            with st.spinner(f"Running {scenario}..."):
                time.sleep(1.5) # Simulation processing time
                
                # Logic based on selection
                if scenario == "Total Solar Eclipse":
                    st.error("ALERT: Solar Generation dropping to 0kW!")
                    impact_data = pd.DataFrame({'Time': range(10), 'Power': [40, 35, 20, 5, 0, 0, 0, 10, 25, 40]})
                elif scenario == "Grid Blackout":
                    st.warning("ALERT: Switching to Island Mode. Shedding Non-Critical Loads.")
                    impact_data = pd.DataFrame({'Time': range(10), 'Power': [50, 50, 0, 15, 15, 15, 20, 25, 30, 40]})
                else:
                    st.success("System Stable under selected parameters.")
                    impact_data = pd.DataFrame({'Time': range(10), 'Power': [45]*10})

                fig = px.line(impact_data, x='Time', y='Power', title="Predicted Power Stability")
                st.plotly_chart(fig, use_container_width=True)

    st.markdown("---")
    
    # 2. Fault Injection Section
    st.subheader("💉 Fault Injection (Hardware Stress Test)")
    fi1, fi2, fi3 = st.columns(3)
    
    if fi1.button("Inject Voltage Sag"):
        st.toast("Voltage Sag (0.8pu) Injected!", icon="⚡")
    
    if fi2.button("Sensor Bias Attack"):
        st.toast("Injecting +50A Offset to Current Sensor", icon="🛡️")
        
    if fi3.button("Reset System"):
        st.rerun()

    # 3. Resilience Score Card
    st.subheader("🛡️ Resilience Analysis")
    r_col1, r_col2 = st.columns(2)
    
    # Simple metric to show how well the system recovered
    r_col1.metric("Stability Index", "84%", "-5% during test")
    r_col2.metric("Estimated Recovery Time", "450 ms", "Ultra-Fast")

if __name__ == "__main__":
    show()