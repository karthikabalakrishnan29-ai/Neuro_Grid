import streamlit as st
import pandas as pd
from components.kpi_cards import render_kpis
from components.charts import MicrogridCharts
from components.alerts_panel import render_sidebar_alerts
from utils.logger import logger
from components.svg_renderer import render_microgrid_svg

def show():
    st.header("📊 Executive Summary Dashboard")
    st.markdown("---")

    # 1. Sidebar Notifications
    render_sidebar_alerts()

    # 2. Key Performance Indicators (KPIs)
    live_data = {
        'solar_kw': 45.8,
        'wind_kw': 12.4,
        'load_kw': 38.2,
        'battery_soc': 82
    }
    render_kpis(live_data)

    st.markdown("### 📈 Operational Insights")
    col1, col2 = st.columns([2, 1])

    with col1:
        chart_helper = MicrogridCharts()
        hist_df = pd.DataFrame({
            'Timestamp': pd.date_range(start='2026-04-02', periods=10, freq='H'),
            'Solar_kW': [10, 25, 45, 50, 48, 30, 10, 0, 0, 0],
            'Load_kW': [20, 22, 25, 30, 35, 40, 45, 42, 38, 30]
        })
        chart_helper.render_power_balance(hist_df)

    with col2:
        st.write("**System Stability**")
        chart_helper = MicrogridCharts()
        chart_helper.render_battery_soc_gauge(live_data['battery_soc'])
        st.metric("Grid Frequency", "50.02 Hz", "Normal")
        st.metric("Voltage Phase Sync", "Stable", delta_color="normal")

    # 3. SVG Schematic
    st.markdown("### ⚡ Live Power Flow")
    render_microgrid_svg(is_active=True)

    # 4. Financial/Market Summary
    st.markdown("### 💰 Economic Impact")
    ec1, ec2, ec3 = st.columns(3)
    ec1.metric("Daily Savings", "₹1,240", "+12% vs Grid")
    ec2.metric("Carbon Offset", "4.2 Tons", "Target: 5.0")
    ec3.metric("Grid Export Revenue", "₹450", "Peak Rate")

if __name__ == "__main__":
    show()