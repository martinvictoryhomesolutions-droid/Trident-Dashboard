I see exactly what is happening in that screenshot.

The text is "Dark Blue" on a "Black" background, making it impossible to read. This happens because the app is confused—it's trying to use "Light Mode" text on our "Dark Mode" background.

We are going to switch to Trident V5 (High Contrast Protocol).

This update does two specific things:

Forces ALL text to White/Gold: No more invisible labels.

Luxury Inputs: Instead of blinding white boxes, the input fields will now be "Matte Grey" with white text (easier on the eyes and looks more expensive).

The Fix (V5 Code)
Go to GitHub.

Open streamlit_app.py.

Delete Everything.

Paste this fixed code:

Python

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

# --- 2. TRIDENT VISUAL IDENTITY (High Contrast Fix) ---
st.markdown("""
    <style>
    /* Force Global Text to White */
    .stApp, .stMarkdown, .stText, p, span, div {
        color: #FAFAFA !important;
    }
    
    /* Main Background - Deep Black */
    .stApp {
        background-color: #050505;
    }

    /* Gold Headers */
    h1, h2, h3, h4, h5, h6 {
        color: #D4AF37 !important;
        font-family: 'Arial', sans-serif;
        font-weight: 700;
        text-transform: uppercase;
    }

    /* FIX: Sidebar Text Visibility */
    section[data-testid="stSidebar"] {
        background-color: #111111;
        border-right: 2px solid #D4AF37;
    }
    section[data-testid="stSidebar"] p, 
    section[data-testid="stSidebar"] span, 
    section[data-testid="stSidebar"] label {
        color: #FFFFFF !important; /* Force White Text in Sidebar */
    }

    /* Radio Buttons (The Navigation Menu) */
    .stRadio label {
        color: #FFFFFF !important;
        font-size: 16px;
        font-weight: bold;
    }

    /* FIX: Input Boxes (Luxury Dark Grey instead of blinding White) */
    .stTextInput > div > div > input, 
    .stNumberInput > div > div > input, 
    .stSelectbox > div > div > div {
        color: #FFFFFF !important;            /* White Text */
        background-color: #262730 !important; /* Dark Grey Background */
        border: 1px solid #444444;
    }
    /* Input Focus State (Gold Border when clicking) */
    .stTextInput > div > div > input:focus {
        border-color: #D4AF37 !important;
    }

    /* Metrics */
    div[data-testid="stMetricValue"] {
        color: #D4AF37 !important;
    }
    
    /* Buttons */
    div.stButton > button {
        background-color: #D4AF37;
        color: #000000 !important; /* Black Text on Gold Button */
        font-weight: bold;
        border-radius: 5px;
        border: none;
    }
    div.stButton > button:hover {
        background-color: #FFFFFF;
        color: #D4AF37 !important;
    }
    </style>
    """, unsafe_allow_html=True)

# --- 3. SIDEBAR NAVIGATION ---
with st.sidebar:
    st.title("🔱 TRIDENT")
    st.markdown("---")
    # This radio button was the issue - fixed via CSS above
    page = st.radio("COMMAND MODULE", ["Dashboard", "Nationwide Map", "Deal Pipeline (CRM)", "Deal Calculator"])
    st.markdown("---")
    st.caption("System Status: Online | V5.0")

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
    
    st.subheader("Revenue Trajectory")
    chart_data = pd.DataFrame(np.random.randn(12, 2).cumsum(axis=0) + [100, 100], columns=["Rentals", "Flips"])
    st.line_chart(chart_data)

# === NATIONWIDE MAP ===
elif page == "Nationwide Map":
    st.title("🇺🇸 NATIONWIDE ASSET TRACKER")
    
    # Map Data: Miami, Austin, Nashville, Phoenix
    map_data = pd.DataFrame({
        'lat': [25.7617, 30.2672, 36.1627, 33.4484],
        'lon': [-80.1918, -97.7431, -86.7816, -112.0740],
        'Market': ['Miami (HQ)', 'Austin', 'Nashville', 'Phoenix'],
        'Value': [1200000, 850000, 620000, 450000]
    })
    
    col1, col2 = st.columns([3, 1])
    with col1:
        # Zoom 3 shows the whole USA
        st.map(map_data, zoom=3)
    with col2:
        st.subheader("Market Details")
        st.info("Hover over points to see asset values.")
        st.dataframe(map_data[['Market', 'Value']], hide_index=True)

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

# === CALCULATOR ===
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
