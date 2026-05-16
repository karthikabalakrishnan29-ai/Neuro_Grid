import streamlit as st
import pandas as pd
import time
import numpy as np
import plotly.graph_objects as go
from components.alerts_panel import render_sidebar_alerts

def show():
    st.header("📡 IoT Live Sensor Monitor")
    st.write("Real-time telemetry from Microgrid Edge Nodes")
    st.markdown("---")

    # 1. Sidebar for status
    render_sidebar_alerts()
    
    # 2. Connection Status Header
    c1, c2, c3 = st.columns(3)
    c1.success("MQTT Broker: CONNECTED")
    c2.info("Active Sensors: 12 Nodes")
    c3.warning("Data Rate: 100ms / Sample")

    # 3. Live Waveform (Oscilloscope View)
    st.subheader("📊 Real-time Waveform Analysis")
    
    # Simulate high-speed data stream
    # Real project-la inga 'iot_layer/mqtt_client.py' data-va session_state-la update pannanum
    if 'chart_data' not in st.session_state:
        st.session_state.chart_data = pd.DataFrame(columns=['Time', 'Voltage', 'Current'])

    # Dynamic Data Simulation for Demo
    new_time = time.strftime("%H:%M:%S")
    new_v = 230 + np.random.normal(0, 2)
    new_i = 15 + np.random.normal(0, 0.5)
    
    # Update buffer
    new_row = pd.DataFrame({'Time': [new_time], 'Voltage': [new_v], 'Current': [new_i]})
    st.session_state.chart_data = pd.concat([st.session_state.chart_data, new_row]).tail(20)

    # Plotting Live Graph
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=st.session_state.chart_data['Time'], 
                             y=st.session_state.chart_data['Voltage'],
                             name="Voltage (V)", line=dict(color='#1f77b4')))
    
    fig.update_layout(height=400, template="plotly_dark", 
                      xaxis_title="Time", yaxis_title="Volts")
    st.plotly_chart(fig, use_container_width=True)

    # 4. Detailed Sensor Table
    st.subheader("📑 Raw Telemetry Feed")
    sensor_df = pd.DataFrame({
        "Sensor ID": ["S_VOLT_01", "S_CURR_01", "S_TEMP_INV", "S_FREQ_01"],
        "Parameter": ["Voltage", "Current", "Inverter Temp", "Frequency"],
        "Value": [f"{new_v:.2f} V", f"{new_i:.2f} A", "42.5 °C", "50.01 Hz"],
        "Status": ["Normal", "Normal", "High", "Normal"]
    })
    
    # Highlighting rows
    def color_status(val):
        color = 'red' if val == 'High' else 'green'
        return f'color: {color}'

    st.table(sensor_df.style.applymap(color_status, subset=['Status']))

    # Auto-refresh logic (Streamlit specific)
    time.sleep(1)
    st.rerun()

import plotly.graph_objects as go
import streamlit as st

def display_iot_map():
    # Title for the section
    st.subheader("🌐 Microgrid IoT Network Topology")
    
    # Node Positions & Labels
    node_x = [1, 2, 3, 2, 4, 1.5] 
    node_y = [2, 4, 2, 1, 3, 3]
    node_labels = ["Solar_01", "Wind_01", "Battery_01", "Load_A", "Load_B", "Central Gateway"]

    # Connection Lines (Edges) - Connecting all nodes to the Central Gateway (1.5, 3)
    edge_x = []
    edge_y = []
    gateway_pos = (1.5, 3)
    
    for x, y in zip(node_x, node_y):
        edge_x.extend([x, gateway_pos[0], None])
        edge_y.extend([y, gateway_pos[1], None])

    fig = go.Figure()

    # 1. Add Connection Lines
    fig.add_trace(go.Scatter(
        x=edge_x, y=edge_y, 
        mode='lines', 
        line=dict(color='#4A90E2', width=1.5, dash='dot'),
        hoverinfo='none'
    ))

    # 2. Add Nodes
    fig.add_trace(go.Scatter(
        x=node_x, y=node_y, 
        mode='markers+text',
        text=node_labels, 
        textposition="top center",
        marker=dict(
            size=25, 
            color=['#FFD700', '#87CEEB', '#90EE90', '#FA8072', '#FA8072', '#FFFFFF'],
            line=dict(width=2, color='white'),
            symbol='diamond'
        )
    ))

    # Layout Styling (Matching your Dark/Light theme)
    fig.update_layout(
        showlegend=False,
        margin=dict(l=20, r=20, t=20, b=20),
        xaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
        yaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        height=400
    )

    st.plotly_chart(fig, use_container_width=True)

# Function call (Add this where you want the map to appear)
display_iot_map()

if __name__ == "__main__":
    show()