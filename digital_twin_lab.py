import streamlit as st
import time
from components.svg_renderer import render_microgrid_svg

def show():
    st.header("🏢 Digital Twin Simulation Lab")
    
    col1, col2 = st.columns([2, 1])

    with col1:
        st.subheader("Live Schematic")
        # Intha toggle-a on panna 'solar_active' True aagum, 
        # Namma 'svg_renderer'-la irukura 'AC-DC' box-um auto-va theriyum.
        is_active = st.toggle("Activate Power Flow Animation", value=True)
        
        # Simple-a koopta podhum mapla
        render_microgrid_svg(solar_active=is_active)

    with col2:
        st.subheader("Twin Sync Status")
        st.success("✅ Physical Layer: Connected")
        st.success("✅ Virtual Layer: Synchronized")
        st.metric("Sync Latency", "45ms", "-2ms")
        
        if st.button("Reset Twin State"):
            with st.spinner("Re-aligning..."):
                time.sleep(1)
                st.warning("Twin State Reset Successful!")