import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime

# --- 1. PAGE CONFIGURATION ---
st.set_page_config(
    page_title="TRIDENT | Real Estate Command",
    page_icon="🔱",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- 2. TRIDENT VISUAL IDENTITY (Black & Gold CSS) ---
st.markdown("""
    <style>
    .stApp { background-color: #000000; color: #FAFAFA; }
    h1, h2, h3, h4, h5 { color: #D4AF37 !important; font-family: 'Arial', sans-serif; font-weight: 700; text-transform: uppercase; }
    div[data-testid="stMetricValue"] { color: #D4AF37; font-size: 28px !important; }
    div[data-testid="stMetricLabel"] { color: #888888; }
    section[data-testid="stSidebar"] { background-color: #111111; border-right: 2px solid #D4AF37; }
    div.stButton > button { background-color: #D4AF37; color: #000000; border: 1px solid #D4AF37; font-weight: bold; text-transform: uppercase; width: 100%; }
    div.stButton > button:hover { background-color: #000000; color: #D4AF37; border: 1px solid #D4AF37; }
    .stTextInput > div > div > input { color: white; background-color: #222222; }
    div[data-testid="stDataFrame"] { background-color: #111111; border: 1px solid #333; }
    </style>
    """, unsafe_allow_html=True)

# --- 3. SIDEBAR ---
with st.sidebar:
    st.title("🔱 TRIDENT")
    st.caption("Real Estate Investment Systems")
    st.markdown("---")
    page = st.radio("COMMAND MODULE", ["Dashboard", "Deal Pipeline (CRM)", "Construction Tracker", "Market Intelligence"])
    st.markdown("---")
    st.info("System Online: Admin Mode")

# --- 4. MAIN PAGES ---
if page == "Dashboard":
    st.title("EXECUTIVE OVERVIEW")
    c1, c2, c3, c4 = st.columns(4)
    c1.metric("Total Equity", "$1,250,000", "+$45k")
    c2.metric("Active Projects", "4", "2 Flips / 2 Rentals")
    c3.metric("Pipeline Value", "$3.4M", "12 Leads")
    c4.metric("Liquid Capital", "$340,000", "Ready")
    st.markdown("---")
    col_left, col_right = st.columns([2,1])
    with col_left:
        st.subheader("Cash Flow Trajectory")
        chart_data = pd.DataFrame(np.random.randn(12, 2).cumsum(axis=0) + [50, 50], columns=["Rentals", "Flips"])
        st.line_chart(chart_data)
    with col_right:
        st.subheader("Portfolio Mix")
        fig = go.Figure(data=[go.Pie(labels=['Long Term', 'STR', 'Flip'], values=[40, 30, 30], hole=.5)])
        fig.update_traces(marker=dict(colors=['#D4AF37', '#333333', '#666666']))
        fig.update_layout(paper_bgcolor='rgba(0,0,0,0)', font=dict(color='white'), margin=dict(t=0, b=0, l=0, r=0))
        st.plotly_chart(fig, use_container_width=True)

elif page == "Deal Pipeline (CRM)":
    st.title("LEAD ACQUISITION CRM")
    st.success("🔥 **HOT LEADS:** 3")
    st.markdown("### 📋 Active Deal Flow")
    crm_data = pd.DataFrame({
        "Address": ["123 Palm Ave", "450 Ocean Dr", "88 Industrial Way"],
        "Status": ["New Lead", "Negotiating", "Under Contract"],
        "Offer Price": [450000, 620000, 310000]
    })
    st.data_editor(crm_data, num_rows="dynamic", use_container_width=True)

elif page == "Construction Tracker":
    st.title("PROJECT MANAGEMENT")
    st.metric("Budget Utilized", "$45,000 / $60,000", "75%")
    st.progress(75)
    st.error("⚠️ ALERT: HVAC Inspection Failed")

elif page == "Market Intelligence":
    st.title("MARKET INTELLIGENCE")
    st.subheader("Deal Calculator")
    price = st.number_input("Purchase Price", value=400000)
    arv = st.number_input("After Repair Value (ARV)", value=600000)
    rehab = st.number_input("Rehab Costs", value=50000)
    profit = arv - price - rehab - (arv * 0.10)
    st.metric("Projected Net Profit", f"${profit:,.2f}")
