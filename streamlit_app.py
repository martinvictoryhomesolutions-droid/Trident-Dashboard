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
    /* Deep Black Background */
    .stApp {
        background-color: #000000;
        color: #FAFAFA;
    }
    /* Gold Accents */
    h1, h2, h3, h4, h5 {
        color: #D4AF37 !important;
        font-family: 'Arial', sans-serif;
        font-weight: 700;
        text-transform: uppercase;
    }
    /* Metrics */
    div[data-testid="stMetricValue"] {
        color: #D4AF37;
        font-size: 28px !important;
    }
    div[data-testid="stMetricLabel"] {
        color: #888888;
    }
    /* Sidebar */
    section[data-testid="stSidebar"] {
        background-color: #111111;
        border-right: 2px solid #D4AF37;
    }
    /* Buttons */
    div.stButton > button {
        background-color: #D4AF37;
        color: #000000;
        border: 1px solid #D4AF37;
        font-weight: bold;
        text-transform: uppercase;
        width: 100%;
    }
    div.stButton > button:hover {
        background-color: #000000;
        color: #D4AF37;
        border: 1px solid #D4AF37;
    }
    /* Inputs */
    .stTextInput > div > div > input {
        color: white;
        background-color: #222222;
    }
    /* Dataframe/Tables */
    div[data-testid="stDataFrame"] {
        background-color: #111111;
        border: 1px solid #333;
    }
    </style>
    """, unsafe_allow_html=True)

# --- 3. SIDEBAR: NAVIGATION & AI ---
with st.sidebar:
    st.title("🔱 TRIDENT")
    st.caption("Real Estate Investment Systems")
    st.markdown("---")
    
    # Navigation
    page = st.radio("COMMAND MODULE", ["Dashboard", "Deal Pipeline (CRM)", "Construction Tracker", "Market Intelligence"])
    
    st.markdown("---")
    
    # The "Trident AI" Placeholder
    st.subheader("🤖 Trident Advisor")
    user_query = st.text_input("Ask Trident (e.g., 'Analyze ROI')")
    if user_query:
        st.info("Trident AI: Analyzing market data... (AI Integration Pending)")
    
    st.markdown("---")
    st.markdown("### 🔒 Secure Mode")
    st.caption(f"User: Admin | ID: 8821-X")

# --- 4. MAIN PAGES ---

# === DASHBOARD PAGE ===
if page == "Dashboard":
    st.title("EXECUTIVE OVERVIEW")
    
    # Top Metrics
    c1, c2, c3, c4 = st.columns(4)
    c1.metric("Total Equity", "$1,250,000", "+$45k this month")
    c2.metric("Active Projects", "4", "2 Flips / 2 Rentals")
    c3.metric("Pipeline Value", "$3.4M", "12 Leads")
    c4.metric("Liquid Capital", "$340,000", "Ready to Deploy")
    
    st.markdown("---")
    
    # Charts Row
    col_left, col_right = st.columns([2,1])
    
    with col_left:
        st.subheader("Cash Flow Trajectory")
        # Dummy Data
        chart_data = pd.DataFrame(np.random.randn(12, 2).cumsum(axis=0) + [50, 50], columns=["Rentals", "Flips"])
        st.line_chart(chart_data)
        
    with col_right:
        st.subheader("Portfolio Mix")
        labels = ['Long Term', 'STR (Airbnb)', 'Fix & Flip']
        values = [40, 30, 30]
        fig = go.Figure(data=[go.Pie(labels=labels, values=values, hole=.5)])
        fig.update_traces(marker=dict(colors=['#D4AF37', '#333333', '#666666']))
        fig.update_layout(paper_bgcolor='rgba(0,0,0,0)', font=dict(color='white'), margin=dict(t=0, b=0, l=0, r=0))
        st.plotly_chart(fig, use_container_width=True)

# === DEAL PIPELINE (CRM) PAGE ===
elif page == "Deal Pipeline (CRM)":
    st.title("LEAD ACQUISITION CRM")
    
    c1, c2, c3 = st.columns(3)
    c1.success("🔥 **HOT LEADS:** 3")
    c2.warning("⏳ **FOLLOW UP:** 8")
    c3.info("📝 **OFFERS OUT:** 2")
    
    st.markdown("### 📋 Active Deal Flow")
    
    # Editable Data Table
    crm_data = pd.DataFrame({
        "Address": ["123 Palm Ave", "450 Ocean Dr", "88 Industrial Way", "990 Lakeview"],
        "Seller": ["John Doe", "Jane Smith", "LLC Corp", "Estate of Mark"],
        "Status": ["New Lead", "Negotiating", "Under Contract", "Closed"],
        "Offer Price": [450000, 620000, 310000, 0],
        "Est. Profit": [85000, 120000, 45000, 0],
        "Last Contact": ["Today", "Yesterday", "2 days ago", "Last week"]
    })
    
    edited_df = st.data_editor(crm_data, num_rows="dynamic", use_container_width=True)
    
    st.caption("*Tip: You can edit cells directly in this table.*")

# === CONSTRUCTION TRACKER PAGE ===
elif page == "Construction Tracker":
    st.title("PROJECT MANAGEMENT")
    
    # Project Selector
    project = st.selectbox("Select Active Project", ["123 Palm Ave (Flip)", "450 Ocean Dr (Airbnb Rehab)"])
    
    col1, col2 = st.columns([1, 2])
    
    with col1:
        st.subheader("Project Health")
        st.metric("Budget Utilized", "$45,000 / $60,000", "75%")
        st.progress(75)
        st.metric("Timeline", "Week 4 of 8", "On Track")
        st.progress(50)
        
        st.error("⚠️ ALERT: HVAC Inspection Failed")
    
    with col2:
        st.subheader("Gantt Chart / Timeline")
        # Simple Timeline Visual
        task_data = pd.DataFrame({
            "Task": ["Demo", "Plumbing", "Electrical", "Drywall", "Paint", "Floors"],
            "Status": ["Done", "Done", "In Progress", "Pending", "Pending", "Pending"],
            "Completion": [100, 100, 60, 0, 0, 0]
        })
        st.dataframe(task_data, use_container_width=True)

# === MARKET INTELLIGENCE PAGE ===
elif page == "Market Intelligence":
    st.title("MARKET INTELLIGENCE")
    
    st.subheader("📍 Opportunity Map")
    
    # Map
    map_data = pd.DataFrame(
        np.random.randn(10, 2) / [50, 50] + [25.7617, -80.1918],
        columns=['lat', 'lon'])
    st.map(map_data)
    
    c1, c2 = st.columns(2)
    with c1:
        st.subheader("Deal Calculator")
        price = st.number_input("Purchase Price", value=400000)
        arv = st.number_input("After Repair Value (ARV)", value=600000)
        rehab = st.number_input("Rehab Costs", value=50000)
        
        profit = arv - price - rehab - (arv * 0.10) # 10% closing/holding costs
        st.metric("Projected Net Profit", f"${profit:,.2f}")
        
    with c2:
        st.subheader("70% Rule Check")
        max_offer = (arv * 0.70) - rehab
        st.metric("Max Allowable Offer (MAO)", f"${max_offer:,.2f}")
        
        if price <= max_offer:
            st.success("✅ BUY SIGNAL")
        else:
            st.error("❌ OVERPRICED")
