import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime

# --- 1. PAGE CONFIGURATION & STATE ---
st.set_page_config(
    page_title="TRIDENT | Real Estate Omni-System",
    page_icon="🔱",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Initialize Session State
if 'capital' not in st.session_state: st.session_state.capital = 500000
if 'leads' not in st.session_state:
    st.session_state.leads = pd.DataFrame({
        "Address": ["123 Maple Ave", "88 Ocean Dr", "404 Industrial", "99 Ranch Rd"],
        "Source": ["Direct Mail", "Wholesaler", "Cold Call", "PPC"],
        "Status": ["New Lead", "Negotiating", "Under Contract", "Closed"],
        "Motivation": ["Divorce", "Probate", "Tired Landlord", "Foreclosure"],
        "Offer_Price": [120000, 450000, 320000, 210000]
    })

# --- 2. VISUAL IDENTITY (FIXED METRIC VISIBILITY) ---
st.markdown("""
    <style>
    /* Main Background */
    .stApp { background-color: #0F172A; color: #FFFFFF; }
    
    /* SIDEBAR FIX */
    [data-testid="stSidebar"] { background-color: #1E293B; border-right: 1px solid #475569; }
    [data-testid="stSidebar"] h1, [data-testid="stSidebar"] h2, [data-testid="stSidebar"] h3 { color: #38BDF8 !important; }
    [data-testid="stSidebar"] p, [data-testid="stSidebar"] span, [data-testid="stSidebar"] div, [data-testid="stSidebar"] label { color: #FFFFFF !important; font-size: 16px !important; }
    .stRadio label { color: #FFFFFF !important; font-weight: bold !important; }
    
    /* PANEL BACKGROUNDS */
    div[data-testid="stVerticalBlock"] > div { 
        background-color: #1E293B; 
        border-radius: 10px; 
        padding: 15px; 
        border: 1px solid #334155; 
    }
    
    /* --- METRICS FIX (THE GHOST TEXT) --- */
    /* This forces the label (e.g. "Liquid Capital") to be White */
    div[data-testid="stMetricLabel"] { 
        color: #FFFFFF !important; 
        font-weight: bold !important;
        font-size: 16px !important;
    }
    /* This keeps the value (e.g. "$500,000") Blue */
    div[data-testid="stMetricValue"] { 
        color: #38BDF8 !important; 
        font-size: 28px !important; 
    }
    
    /* INPUTS */
    .stTextInput > div > div > input, .stNumberInput > div > div > input, .stSelectbox > div > div > div {
        color: #FFFFFF !important; 
        background-color: #334155 !important; 
        border: 1px solid #475569;
    }
    
    /* BUTTONS */
    div.stButton > button { 
        background-color: #38BDF8; 
        color: #0F172A !important; 
        font-weight: bold; 
        border: none; 
        width: 100%; 
    }
    </style>
    """, unsafe_allow_html=True)

# --- 3. SIDEBAR NAVIGATION ---
with st.sidebar:
    st.title("🔱 TRIDENT OMNI")
    st.markdown("### SYSTEM MODULES") 
    
    module = st.radio("NAVIGATE TO:", 
        ["COMMAND DASHBOARD", 
         "CRM & LEADS (Active)", 
         "DEAL ARCHITECT (Analyze)", 
         "CONSTRUCTION (Rehabs)", 
         "RENTAL PORTFOLIO (Hold)"]
    )
    st.markdown("---")
    st.info("System Ready. All Modules Loaded.")

# =========================================================
# MODULE 1: COMMAND DASHBOARD
# =========================================================
if module == "COMMAND DASHBOARD":
    st.title("🛡️ COMMAND CENTER")
    
    # METRICS ROW
    k1, k2, k3, k4 = st.columns(4)
    k1.metric("Liquid Capital", f"${st.session_state.capital:,.0f}", "Ready to Deploy")
    k2.metric("Active Rehabs", "2", "Budget: $120k")
    k3.metric("Pipeline Value", "$3.4M", "8 Leads")
    k4.metric("Rental Cashflow", "$12,500/mo", "+5 Units")
    
    st.markdown("---")
    
    c_left, c_right = st.columns([2, 1])
    
    with c_left:
        st.subheader("🗺️ Nationwide Asset Map")
        map_data = pd.DataFrame({
            'lat': [25.7617, 30.2672, 36.1627, 33.4484, 40.7128, 34.0522],
            'lon': [-80.1918, -97.7431, -86.7816, -112.0740, -74.0060, -118.2437],
            'Type': ['Rental (Cashflow)', 'BRRRR (In Progress)', 'Flip (Active)', 'Creative (Sub-To)', 'Wholesale Deal', 'Lead'],
            'Size': [25, 25, 25, 25, 20, 15], 
            'Color': ['#10B981', '#F59E0B', '#EF4444', '#8B5CF6', '#3B82F6', '#9CA3AF']
        })
        
        fig = px.scatter_mapbox(
            map_data, lat="lat", lon="lon", hover_name="Type", size="Size",
            color="Type", color_discrete_sequence=px.colors.qualitative.Bold,
            zoom=3, height=600
        )
        
        # LEGEND BOX (High Contrast)
        fig.update_layout(
            mapbox_style="carto-darkmatter", 
            margin={"r":0,"t":0,"l":0,"b":0}, 
            paper_bgcolor="#1E293B",
            legend=dict(
                title="Asset Types",
                yanchor="top", y=0.95,
                xanchor="left", x=0.02,
                bgcolor="rgba(0,0,0,0.8)", 
                bordercolor="#FFFFFF", borderwidth=1,
                font=dict(family="Arial", size=14, color="white")
            )
        )
        st.plotly_chart(fig, use_container_width=True)

    with c_right:
        st.subheader("🔔 Urgent Alerts")
        st.error("⚠️ **123 Maple Ave (Flip)**\n\nRoofing Estimate came in $2k over budget.")
        st.warning("⚡ **New Creative Lead**\n\nSeller asking $0 down, 3% interest.")
        st.success("💰 **Rent Collected**\n\nUnit 4B Paid Early (+$1,200)")

# =========================================================
# MODULE 2: CRM & LEADS
# =========================================================
elif module == "CRM & LEADS (Active)":
    st.title("📇 CRM: LEAD PIPELINE")
    c1, c2 = st.columns([2, 1])
    with c1:
        st.subheader("Active Leads")
        st.data_editor(st.session_state.leads, num_rows="dynamic", use_container_width=True)
    with c2:
        st.subheader("💬 Activity Log")
        st.info("Call Logged: Seller motivated.")

# =========================================================
# MODULE 3: DEAL ARCHITECT
# =========================================================
elif module == "DEAL ARCHITECT (Analyze)":
    st.title("🏗️ DEAL ARCHITECT & CALCULATOR")
    st.markdown("#### 1. PROPERTY VITALS")
    i1, i2, i3, i4 = st.columns(4)
    purchase_price = i1.number_input("Purchase Price", value=200000)
    arv = i2.number_input("ARV", value=350000)
    rehab_cost = i3.number_input("Rehab Est", value=50000)
    rent_est = i4.number_input("Rent Est", value=2500)

    st.markdown("---")
    tab1, tab2, tab3 = st.tabs(["🔨 FLIP", "🏠 BRRRR", "🎨 CREATIVE"])
    
    with tab1:
        st.subheader("Flip Analysis")
        profit = arv - (purchase_price + rehab_cost + (arv*0.09))
        st.metric("Net Profit", f"${profit:,.0f}")
    with tab2:
        st.subheader("BRRRR Analysis")
        cash_left = (purchase_price + rehab_cost) - (arv * 0.75)
        st.metric("Cash Left in Deal", f"${cash_left:,.0f}")
    with tab3:
        st.subheader("Creative / Sub-To")
        st.metric("Entry Fee", "$15,000")

# =========================================================
# MODULE 4: CONSTRUCTION
# =========================================================
elif module == "CONSTRUCTION (Rehabs)":
    st.title("🚧 CONSTRUCTION MANAGER")
    st.dataframe(pd.DataFrame({"Item":["Roof","HVAC"], "Budget":[8000, 6000], "Actual":[10500, 6000]}), use_container_width=True)

# =========================================================
# MODULE 5: RENTAL PORTFOLIO
# =========================================================
elif module == "RENTAL PORTFOLIO (Hold)":
    st.title("🔑 RENTAL PORTFOLIO")
    st.dataframe(pd.DataFrame({"Unit":["1A","1B"], "Tenant":["John","Jane"], "Status":["Paid","Paid"]}), use_container_width=True)
