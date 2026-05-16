import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
import plotly.express as px

def show():
    st.header("🚨 Fault & Anomaly Analytics")
    
    # --- 1. Real-time Monitoring Section ---
    st.subheader("Real-time Anomaly Intelligence")
    
    # Layout for Slider and Metrics
    col_a, col_b = st.columns([1, 1])
    
    with col_a:
        score = st.slider("Simulated Anomaly Score", 0.0, 1.0, 0.2)
        if score > 0.7:
            st.error(f"⚠️ CRITICAL FAULT DETECTED! (Score: {score})")
            st.button("Acknowledge Alarm", use_container_width=True)
        else:
            st.success("✅ System Health: Healthy")

    with col_b:
        # Gauge Chart for visual appeal
        fig_gauge = go.Figure(go.Indicator(
            mode = "gauge+number",
            value = score * 100,
            domain = {'x': [0, 1], 'y': [0, 1]},
            title = {'text': "Security Risk %"},
            gauge = {
                'axis': {'range': [None, 100]},
                'bar': {'color': "#EF553B" if score > 0.7 else "#00CC96"},
                'steps': [
                    {'range': [0, 70], 'color': "lightgray"},
                    {'range': [70, 100], 'color': "gray"}]
            }
        ))
        fig_gauge.update_layout(height=250, margin=dict(t=0, b=0, l=10, r=10))
        st.plotly_chart(fig_gauge, use_container_width=True)

    st.divider()

    # --- 2. Advanced Visualizations (The "Worth" Factor) ---
    col1, col2 = st.columns(2)

    with col1:
        st.subheader("🔍 ML Fault Classification")
        # Scatter Plot - To show how ML identifies outliers (Volts vs Current)
        np.random.seed(42)
        v = np.random.normal(230, 2, 50)
        i = np.random.normal(15, 0.5, 50)
        # Adding 2 fake anomalies
        v = np.append(v, [255, 212])
        i = np.append(i, [28, 22])
        status = (['Normal'] * 50) + (['Anomaly'] * 2)
        
        df_scatter = pd.DataFrame({'Voltage (V)': v, 'Current (A)': i, 'Status': status})
        fig_scatter = px.scatter(df_scatter, x='Voltage (V)', y='Current (A)', color='Status',
                                 color_discrete_map={'Normal': '#00CC96', 'Anomaly': '#EF553B'},
                                 template="seaborn")
        st.plotly_chart(fig_scatter, use_container_width=True)

    with col2:
        st.subheader("📊 Fault Source Distribution")
        # Bar Chart - Where are the faults happening?
        fault_data = pd.DataFrame({
            'Component': ['Solar', 'Battery', 'DC Bus', 'Inverter', 'Load'],
            'Faults': [2, 1, 7, 1, 3]
        })
        fig_bar = px.bar(fault_data, x='Component', y='Faults', 
                         color='Faults', color_continuous_scale='Reds')
        st.plotly_chart(fig_bar, use_container_width=True)

    st.divider()

    # --- 3. Historical Logs ---
    st.subheader("📋 Recent Event Logs")
    df_logs = pd.DataFrame({
        'Timestamp': ['10:00:15', '10:05:42', '10:10:05', '12:15:30', '14:20:10'],
        'Type': ['Voltage Spike', 'None', 'Frequency Drop', 'Inverter Overheat', 'DC Bus Ripple'],
        'Severity': ['🔴 High', '🟢 Normal', '🟡 Medium', '🔴 High', '🟡 Medium'],
        'Action': ['Auto-Isolated', 'Logged', 'Load Shedding', 'Fan Activated', 'Filter Engaged']
    })
    
    # Styled Table for better look
    st.dataframe(df_logs, use_container_width=True, hide_index=True)

if __name__ == "__main__":
    show()