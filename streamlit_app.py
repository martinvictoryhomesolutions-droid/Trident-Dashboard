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

# --- 2. VISUAL IDENTITY (FIXED FOR VISIBILITY) ---
st.markdown("""
    <style>
    /* Main Background */
    .stApp { background-color: #0F172A; color: #FFFFFF; }
    
    /* SIDEBAR FIX: FORCE WHITE TEXT */
    [data-testid="stSidebar"] {
        background-color: #1E293B;
        border-right: 1px solid #475569;
    }
    [data-testid="stSidebar"] h1, [data-testid="stSidebar"] h2, [data-testid="stSidebar"] h3 {
        color: #38BDF8 !important; /* Cyan Title */
    }
    [data-testid="stSidebar"] p, [data-testid="stSidebar"] span, [data-testid="stSidebar"] div, [data-testid="stSidebar"] label {
        color: #FFFFFF !important; /* Bright White Text */
        font-size: 16px !important; /* Larger Font */
    }
    
    /* RADIO BUTTONS (The Menu) */
    .stRadio label {
        color: #FFFFFF !important;
        font-weight: bold !important;
    }
    
    /* Main Panels */
    div[data-testid="stVerticalBlock"] > div { 
        background-color: #1E293B; 
        border-radius: 10px; 
        padding: 15px; 
        border: 1px solid #334155; 
    }
    
    /* Metrics */
    div[data-testid="stMetricValue"] { color: #38BDF8 !important; font-size: 26px !important; }
    div[data-testid="stMetricLabel"] { color: #CBD5E1 !important; }
    
    /* Inputs */
    .stTextInput > div > div > input, .stNumberInput > div > div > input, .stSelectbox > div > div > div {
        color: #FFFFFF !important; 
        background-color: #334155 !important; 
        border: 1px solid #475569;
    }
    
    /* Buttons */
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
    st.markdown("### SYSTEM MODULES") # Using header to ensure visibility
    
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
            'Size': [20, 20, 20, 20, 15, 10],
            'Color': ['#10B981', '#F59E0B', '#EF4444', '#8B5CF6', '#3B82F6', '#9CA3AF']
        })
        
        fig = px.scatter_mapbox(
            map_data, lat="lat", lon="lon", hover_name="Type", size="Size",
            color="Type", color_discrete_sequence=px.colors.qualitative.Bold,
            zoom=3, height=500
        )
        fig.update_layout(mapbox_style="carto-darkmatter", margin={"r":0,"t":0,"l":0,"b":0}, paper_bgcolor="#1E293B", showlegend=True)
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
        updated_leads = st.data_editor(st.session_state.leads, num_rows="dynamic", use_container_width=True)
        
    with c2:
        st.subheader("💬 Activity Log (Hypothetical)")
        st.selectbox("Select Lead to View History", st.session_state.leads["Address"])
        
        st.markdown("""
        **Today, 10:00 AM** - *Called Seller*
        > "Seller is motivated. Divorce situation. Needs to move in 30 days. Open to creative finance."
        
        **Yesterday, 4:30 PM** - *Sent Text*
        > "Hey John, just following up on our offer for 123 Maple."
        """)
        if st.button("➕ Log New Call"):
            st.toast("Call Logged: Seller didn't answer.")

# =========================================================
# MODULE 3: DEAL ARCHITECT
# =========================================================
elif module == "DEAL ARCHITECT (Analyze)":
    st.title("🏗️ DEAL ARCHITECT & CALCULATOR")
    
    st.markdown("#### 1. PROPERTY VITALS")
    i1, i2, i3, i4 = st.columns(4)
    purchase_price = i1.number_input("Purchase Price", value=200000)
    arv = i2.number_input("ARV (After Repair)", value=350000)
    rehab_cost = i3.number_input("Rehab Estimate", value=50000)
    rent_est = i4.number_input("Est. Monthly Rent", value=2500)

    st.markdown("---")
    st.markdown("#### 2. STRATEGY COMPARISON")
    
    tab1, tab2, tab3 = st.tabs(["🔨 FLIP / WHOLESALE", "🏠 BRRRR STRATEGY", "🎨 CREATIVE (SUB-TO)"])
    
    with tab1:
        st.subheader("Flip & Wholesale Analysis")
        c1, c2 = st.columns(2)
        with c1:
            flip_profit = arv - (purchase_price + rehab_cost + (arv*0.09)) # Simplified costs
            st.metric(" Projected Net Profit (Flip)", f"${flip_profit:,.0f}")
        with c2:
            mao = (arv * 0.70) - rehab_cost
            st.metric("MAO (70% Rule)", f"${mao:,.0f}")

    with tab2:
        st.subheader("BRRRR Analysis")
        new_loan = arv * 0.75
        cash_left = (purchase_price + rehab_cost) - new_loan
        st.metric("Cash Left in Deal", f"${cash_left:,.0f}")
        if cash_left <= 0: st.success("✅ INFINITE RETURN POSSIBLE")

    with tab3:
        st.subheader("Creative Finance / Subject-To")
        entry_fee = 15000
        st.metric("Cash to Seller (Entry)", f"${entry_fee:,.0f}")
        st.metric("Monthly Net Cashflow", "$450/mo")

# =========================================================
# MODULE 4: CONSTRUCTION
# =========================================================
elif module == "CONSTRUCTION (Rehabs)":
    st.title("🚧 CONSTRUCTION MANAGER")
    
    col1, col2 = st.columns([1, 2])
    with col1:
        st.subheader("Budget Tracker")
        budget_data = pd.DataFrame({
            "Item": ["Demolition", "Roof", "HVAC", "Kitchen", "Paint"],
            "Budget": [2000, 8000, 6000, 15000, 5000],
            "Actual": [2000, 10500, 6000, 12000, 0]
        })
        st.dataframe(budget_data, hide_index=True)
        st.error("⚠️ ALERT: Roof is $2,500 OVER Budget")
        
    with col2:
        st.subheader("Project Timeline")
        tasks = pd.DataFrame({
            'Task': ['Demo', 'Roofing', 'Rough Electric', 'Insulation', 'Drywall', 'Cabinets'],
            'Start': [1, 5, 8, 15, 18, 25],
            'Duration': [4, 7, 5, 3, 7, 10],
            'Status': ['Done', 'Active', 'Pending', 'Pending', 'Pending', 'Pending']
        })
        fig_gantt = px.bar(tasks, x="Duration", y="Task", orientation='h', color="Status", base="Start",
                           color_discrete_map={'Done':'#10B981', 'Active':'#38BDF8', 'Pending':'#475569'})
        fig_gantt.update_layout(paper_bgcolor="#1E293B", plot_bgcolor="#1E293B", font=dict(color="#E2E8F0"))
        st.plotly_chart(fig_gantt, use_container_width=True)

# =========================================================
# MODULE 5: RENTAL PORTFOLIO
# =========================================================
elif module == "RENTAL PORTFOLIO (Hold)":
    st.title("🔑 RENTAL PORTFOLIO MANAGER")
    
    r1, r2, r3 = st.columns(3)
    r1.metric("Occupancy Rate", "92%", "11/12 Units")
    r2.metric("Total Monthly Rent", "$18,500", "Gross")
    
    st.markdown("### Tenant Roster")
    tenants = pd.DataFrame({
        "Address": ["Unit 1A", "Unit 1B", "Unit 2A", "House 44"],
        "Tenant": ["John Doe", "Jane Smith", "Mike Ross", "Sarah Connor"],
        "Status": ["Paid", "Paid", "Late (3 Days)", "Paid"]
    })
    st.dataframe(tenants, use_container_width=True)
    st.warning("⚠️ **Alert:** Unit 2A (Mike Ross) is 3 days late.")
