import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go

# --- 1. PAGE CONFIGURATION ---
st.set_page_config(
    page_title="TRIDENT | Real Estate Command",
    page_icon="🔱",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- 2. TRIDENT VISUAL IDENTITY (Fixed Readability) ---
st.markdown("""
    <style>
    /* Force Background to Black */
    .stApp {
        background-color: #000000;
        color: #FAFAFA;
    }
    /* Gold Headers */
    h1, h2, h3, h4, h5 {
        color: #D4AF37 !important;
        font-family: 'Arial', sans-serif;
        font-weight: 700;
        text-transform: uppercase;
    }
    /* FIX: Input Boxes (Make them White with Black Text) */
    .stTextInput > div > div > input {
        color: #000000 !important;
        background-color: #FFFFFF !important;
        border: 1px solid #D4AF37;
    }
    .stNumberInput > div > div > input {
        color: #000000 !important;
        background-color: #FFFFFF !important;
        border: 1px solid #D4AF37;
    }
    .stSelectbox > div > div > div {
        color: #000000 !important;
        background-color: #FFFFFF !important;
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
        font-weight: bold;
        width: 100%;
        border-radius: 5px;
    }
    </style>
    """, unsafe_allow_html=True)

# --- 3. SIDEBAR NAVIGATION ---
with st.sidebar:
    st.title("🔱 TRIDENT")
    st.markdown("---")
    page = st.radio("COMMAND MODULE", ["Dashboard", "Nationwide Map", "Deal Pipeline (CRM)", "Deal Calculator"])
    st.markdown("---")
    st.caption("System Status: Online")

# --- 4. MAIN PAGES ---

# === DASHBOARD ===
if page == "Dashboard":
    st.title("EXECUTIVE OVERVIEW")
    c1, c2, c3, c4 = st.columns(4)
    c1.metric("Total Equity", "$1.2M", "+8%")
    c2.metric("Cash Flow", "$38,500", "+12%")
    c3.metric("Active Deals", "4", "Nationwide")
    c4.metric("Liquid Capital", "$850k", "Ready")
    
    st.markdown("---")
    
    # Financial Chart
    st.subheader("Revenue Trajectory")
    chart_data = pd.DataFrame(np.random.randn(12, 2).cumsum(axis=0) + [100, 100], columns=["Rentals", "Flips"])
    st.line_chart(chart_data)

# === NATIONWIDE MAP (NEW FEATURE) ===
elif page == "Nationwide Map":
    st.title("🇺🇸 NATIONWIDE ASSET TRACKER")
    
    # Dummy Data: Major Markets (Miami, Austin, Nashville, Phoenix)
    map_data = pd.DataFrame({
        'lat': [25.7617, 30.2672, 36.1627, 33.4484],
        'lon': [-80.1918, -97.7431, -86.7816, -112.0740],
        'Market': ['Miami (HQ)', 'Austin (Growth)', 'Nashville (Rental)', 'Phoenix (Flip)'],
        'Value': [1200000, 850000, 620000, 450000]
    })
    
    # Interactive Map Controls
    col1, col2 = st.columns([3, 1])
    with col1:
        st.map(map_data, zoom=3) # Zoom=3 shows the whole US
    with col2:
        st.subheader("Market Details")
        st.write("**Active Markets:** 4")
        st.write("**Total Value:** $3.12M")
        st.info("Hover over the map to zoom in on specific markets.")

# === DEAL PIPELINE ===
elif page == "Deal Pipeline (CRM)":
    st.title("LEAD MANAGEMENT")
    crm_data = pd.DataFrame({
        "Property": ["12 Ocean Dr", "45 Ranch Rd", "88 Industrial"],
        "Market": ["Miami, FL", "Austin, TX", "Detroit, MI"],
        "Status": ["Negotiating", "Under Contract", "New Lead"],
        "Offer ($)": [450000, 320000, 150000]
    })
    st.data_editor(crm_data, num_rows="dynamic", use_container_width=True)

# === CALCULATOR (FIXED VISIBILITY) ===
elif page == "Deal Calculator":
    st.title("RAPID DEAL ANALYZER")
    
    c1, c2, c3 = st.columns(3)
    with c1:
        price = st.number_input("Purchase Price ($)", value=400000, step=5000)
    with c2:
        arv = st.number_input("After Repair Value ($)", value=600000, step=5000)
    with c3:
        rehab = st.number_input("Rehab Budget ($)", value=50000, step=1000)
        
    profit = arv - price - rehab - (arv * 0.10)
    roi = (profit / (price * 0.20 + rehab)) * 100
    
    st.markdown("### Results")
    rc1, rc2 = st.columns(2)
    rc1.metric("Net Profit", f"${profit:,.0f}")
    rc2.metric("ROI", f"{roi:.1f}%")
    
    if roi > 15:
        st.success("✅ BUY SIGNAL: High Profit Potential")
    else:
        st.warning("⚠️ CAUTION: Low Margin Deal")
