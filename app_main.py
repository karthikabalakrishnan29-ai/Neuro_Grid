import sys

import os

import streamlit as st

import streamlit.components.v1 as components

import plotly.graph_objects as go

import plotly.express as px



# 1. Path Setup

sys.path.append(os.path.abspath(os.path.dirname(__file__) + '/..'))



# 2. Page Config

st.set_page_config(page_title="Microgrid Digital Twin", layout="wide")



# --- SMART IMPORT WITH FALLBACK ---

ai_hub = None

fault_analytics = None



try:

    import importlib.util

    def load_module(module_name, file_name):

        base_dir = os.path.join(os.path.dirname(__file__), 'pages')

        possible_files = [

            os.path.join(base_dir, f"{file_name}.py"),

            os.path.join(base_dir, f"04_{file_name}.py"),

            os.path.join(base_dir, f"06_{file_name}.py"),

        ]

        for filepath in possible_files:

            if os.path.exists(filepath):

                spec = importlib.util.spec_from_file_location(module_name, filepath)

                mod = importlib.util.module_from_spec(spec)

                spec.loader.exec_module(mod)

                return mod

        return None



    ai_hub = load_module("ai_decision_hub", "ai_decision_hub")

    fault_analytics = load_module("fault_analytics", "fault_analytics")

except Exception as e:

    pass



# --- UPDATED SVG RENDERER (CONVERTERS ADDED) ---

def render_microgrid_svg(is_active):

    flow_class = "flow" if is_active else ""

    svg_code = f"""

    <div style="display: flex; justify-content: center; align-items: center; background: #1e1e1e; padding: 20px; border-radius: 15px;">

        <svg width="700" height="350" viewBox="0 0 700 350" xmlns="http://www.w3.org/2000/svg">

            <style>

                .flow {{ stroke-dasharray: 8; animation: dash 1s linear infinite; }}

                @keyframes dash {{ to {{ stroke-dashoffset: -16; }} }}

                .label {{ font-family: 'Segoe UI', sans-serif; font-size: 13px; font-weight: bold; fill: #ffffff; text-anchor: middle; }}

                .conv-label {{ font-family: 'Segoe UI', sans-serif; font-size: 10px; font-weight: bold; fill: #aaa; text-anchor: middle; }}

            </style>

           

            <!-- MAIN DC BUS -->

            <rect x="330" y="50" width="40" height="250" fill="#444" rx="5"/>

            <text x="350" y="40" class="label">MAIN DC BUS</text>



            <!-- SOLAR SECTION -->

            <rect x="50" y="70" width="70" height="45" fill="#f1c40f" rx="5"/>

            <text x="85" y="60" class="label">SOLAR☀️</text>

            <!-- Solar Converter (MPPT) -->

            <rect x="180" y="77" width="65" height="30" fill="#2c2c2c" stroke="#f1c40f" stroke-width="2" rx="3"/>

            <text x="212" y="96" class="conv-label">MPPT CONV</text>

            <path d="M120 92 H180 M245 92 H330" stroke="#2ecc71" stroke-width="4" class="{flow_class}" fill="none"/>



            <!-- WIND SECTION -->

            <circle cx="85" cy="230" r="28" fill="#3498db"/>

            <text x="85" y="190" class="label">WIND🌀</text>

            <!-- Wind Converter (AC-DC) -->

            <rect x="180" y="215" width="65" height="30" fill="#2c2c2c" stroke="#3498db" stroke-width="2" rx="3"/>

            <text x="212" y="234" class="conv-label">AC-DC RECT</text>

            <path d="M113 230 H180 M245 230 H330" stroke="#3498db" stroke-width="4" class="{flow_class}" fill="none"/>



            <!-- BATTERY SECTION -->

            <rect x="550" y="150" width="80" height="50" fill="#27ae60" rx="5"/>

            <text x="590" y="140" class="label">BATTERY🔋</text>

            <!-- Bi-Directional Converter -->

            <rect x="430" y="160" width="70" height="30" fill="#2c2c2c" stroke="#e67e22" stroke-width="2" rx="3"/>

            <text x="465" y="179" class="conv-label">BI-DIR CONV</text>

            <path d="M370 175 H430 M500 175 H550" stroke="#e67e22" stroke-width="4" class="{flow_class}" fill="none"/>

        </svg>

    </div>

    """

    components.html(svg_code, height=380)



# --- MOBILE APP INTERFACE LAYER ---

def render_mobile_app():

    st.markdown("""

        <style>

            .stApp { background-color: #0e1117; }

            .mobile-header {

                text-align: center; padding: 15px; background: linear-gradient(90deg, #00c6ff, #0072ff);

                border-radius: 15px; margin-bottom: 20px; color: white;

            }

        </style>

        <div class="mobile-header"><h2>NeuroGrid Mobile 🔋</h2></div>

    """, unsafe_allow_html=True)



    m1, m2 = st.columns(2)

    with m1: st.metric("⚡ PV Power", "4.8 kW", "0.2")

    with m2: st.metric("🔋 SoC", "82%", "-1%")



    app_tab = st.tabs(["🏠 Monitor", "📊 Analytics", "⚠️ Alerts"])

    with app_tab[0]:

        render_microgrid_svg(is_active=True)

        st.success("System Status: Optimal")

    with app_tab[1]:

        display_core_analytics()

    with app_tab[2]:

        st.warning("Anomaly: DC Bus Spike (10:15 AM)")

        st.info("AI Mitigation: Active")



# --- CORE VISUAL FUNCTIONS ---

def display_iot_map():

    st.subheader("🌐 Microgrid IoT Network Topology")

    node_x = [1, 2, 3, 2, 4, 1.5, 0.5, 3.5, 2.5, 1, 3, 4.5]

    node_y = [2, 4, 2, 1, 3, 3, 3.5, 4, 0.5, 0.5, 4.5, 1.5]

    node_labels = ["Solar_01", "Wind_01", "Battery_01", "Load_A", "Load_B", "Gateway",

                   "Node_07", "Node_08", "Node_09", "Node_10", "Node_11", "Node_12"]

    edge_x, edge_y = [], []

    gateway_pos = (1.5, 3)

    for x, y in zip(node_x, node_y):

        edge_x.extend([x, gateway_pos[0], None])

        edge_y.extend([y, gateway_pos[1], None])

    fig = go.Figure()

    fig.add_trace(go.Scatter(x=edge_x, y=edge_y, mode='lines',

                             line=dict(color='#4A90E2', width=1, dash='dot'), hoverinfo='none'))

    fig.add_trace(go.Scatter(x=node_x, y=node_y, mode='markers+text', text=node_labels,

                             textposition="top center",

                             marker=dict(size=18, color='#00CC96', line=dict(width=1, color='white'))))

    fig.update_layout(showlegend=False, margin=dict(l=10, r=10, t=10, b=10),

                      xaxis=dict(visible=False), yaxis=dict(visible=False),

                      paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)', height=400)

    st.plotly_chart(fig, use_container_width=True)



def display_core_analytics():

    st.subheader("📊 Core Asset Analytics")

    col1, col2 = st.columns(2)

    with col1:

        fig_pie = px.pie(names=['Solar PV', 'Wind', 'Battery Bank'], values=[45, 25, 30],

                         title="Generation Mix (%)", hole=0.4, color_discrete_sequence=px.colors.sequential.RdBu)

        fig_pie.update_layout(paper_bgcolor='rgba(0,0,0,0)', font_color="white")

        st.plotly_chart(fig_pie, use_container_width=True)

    with col2:

        fig_bar = px.bar(x=['Mon', 'Tue', 'Wed', 'Thu', 'Fri'], y=[120, 155, 110, 145, 130],

                         title="Weekly Load Demand (kWh)", labels={'x': 'Day', 'y': 'Load'})

        fig_bar.update_layout(paper_bgcolor='rgba(0,0,0,0)', font_color="white")

        st.plotly_chart(fig_bar, use_container_width=True)



# --- FALLBACK PAGES ---

def show_ai_hub_fallback():

    st.header("🤖 AI Decision Hub")

    st.info("ai_decision_hub.py not found.")



def show_fault_analytics_fallback():

    st.header("🚨 Fault Analytics")

    st.info("fault_analytics.py not found.")



# --- MAIN APPLICATION LOGIC ---

def main():

    if 'logged_in' not in st.session_state:

        st.session_state.logged_in = False



    if not st.session_state.logged_in:

        st.sidebar.title("🔐 Control Center")

        user = st.sidebar.text_input("Username")

        pwd = st.sidebar.text_input("Password", type="password")

        if st.sidebar.button("Login"):

            if user == "admin" and pwd == "admin123":

                st.session_state.logged_in = True

                st.rerun()

            else:

                st.error("Invalid Credentials ❌")

        return



    st.sidebar.title("🎛️ Navigation")

    app_mode = st.sidebar.toggle("📱 Enable Mobile App View", value=False)

    page = st.sidebar.radio("Select Module:", ["Dashboard Home", "Digital Twin Lab", "AI Decision Hub", "Fault Analytics"])



    if app_mode:

        render_mobile_app()

    else:

        st.toast("🛡️ Cyber-Security: Active", icon="✅")

        st.title("⚡ Intelligent Microgrid Digital Twin")



        if page == "Dashboard Home":

            st.markdown("### Welcome to the **Digital Twin Framework**")

            st.info("System Live | Mode: Grid-Connected")

            display_core_analytics()



        elif page == "Digital Twin Lab":

            st.header("🏢 Digital Twin Simulation Lab")

            col1, col2 = st.columns([2, 1])

            with col1:

                st.subheader("Live Schematic")

                is_active = st.toggle("Activate Power Flow Animation", value=True)

                render_microgrid_svg(is_active)

            with col2:

                st.subheader("Twin Sync Status")

                st.success("✅ Physical Layer: Connected")

                st.success("✅ Virtual Layer: Synchronized")

                st.metric("Sync Latency", "45ms", "-2ms")

            st.divider()

            display_iot_map()



        elif page == "AI Decision Hub":

            if ai_hub and hasattr(ai_hub, 'show'): ai_hub.show()

            else: show_ai_hub_fallback()



        elif page == "Fault Analytics":

            if fault_analytics and hasattr(fault_analytics, 'show'): fault_analytics.show()

            else: show_fault_analytics_fallback()



if __name__ == "__main__":

    main()