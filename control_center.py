import streamlit as st
from control_layer.actuator_interface import ActuatorInterface

def show():
    st.header("🎛️ Manual Control Center")
    actuator = ActuatorInterface()

    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Main Breakers")
        if st.button("OPEN MAIN RELAY"):
            actuator.send_signal("Main_CB", "OPEN")
        if st.button("CLOSE MAIN RELAY"):
            actuator.send_signal("Main_CB", "CLOSE")

    with col2:
        st.subheader("Storage System")
        mode = st.radio("Battery Mode", ["Charge", "Discharge", "Standby"])
        if st.button("Apply Battery Mode"):
            st.write(f"Mode set to {mode}")