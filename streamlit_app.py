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

# Initialize Session State for Interactive Simulation
if 'capital' not in st.session_state: st.session_state.capital = 500000
if 'leads' not in st.session_state:
    st.session_state.leads = pd.DataFrame({
        "Address": ["123 Maple Ave", "88 Ocean Dr", "404 Industrial", "99 Ranch Rd"],
        "Source": ["Direct Mail", "Wholesaler", "Cold Call", "PPC"],
        "Status": ["New Lead", "Negotiating", "Under Contract", "Closed"],
        "Motivation": ["Divorce", "Probate", "Tired Landlord", "Foreclosure"],
        "Offer_Price": [120000, 450000, 320000, 210000]
    })

# --- 2. VISUAL IDENTITY (Dark Slate & Gold) ---
st.markdown("""
    <style>
    .stApp { background-color: #0F172A; color: #E2E8F0; }
    div[data-testid="stVerticalBlock"] > div { background-color: #1E293B; border-radius: 10px; padding: 15px; border: 1px solid #334155; }
    h1, h2, h3, h4 { color: #F8FAFC !important; font-family: 'Arial', sans-serif; font-weight: 700; text-transform: uppercase; }
    div[data-testid="stMetricValue"] { color: #38BDF8 !important; font-size: 26px !important; }
    .stTextInput > div > div > input, .stNumberInput > div > div > input, .stSelectbox > div > div > div {
        color: #FFFFFF !important; background-color: #334155 !important; border: 1px solid #475569;
    }
    div.stButton > button { background-color: #38BDF8; color: #0F172A !important; font-weight: bold; border: none; width: 100%; }
    div.stButton > button:hover { background-color: #0EA5E9; }
    </style>
    """, unsafe_allow_html=True)

# --- 3. SIDEBAR NAVIGATION ---
with st.sidebar:
    st.title("🔱 TRIDENT OMNI")
    st.caption("Invest | Build | Rent | Scale")
    st.markdown("---")
    
    module = st.radio("SELECT MODULE", 
        ["COMMAND DASHBOARD", 
         "CRM & LEADS (Active)", 
         "DEAL ARCHITECT (Analyze)", 
         "CONSTRUCTION (Rehabs)", 
         "RENTAL PORTFOLIO (Hold)"]
    )
    
    st.markdown("---")
    st.info("System Ready. All Modules Loaded.")

# =========================================================
# MODULE 1: COMMAND DASHBOARD (The Cockpit)
# =========================================================
if module == "COMMAND DASHBOARD":
    st.title("🛡️ COMMAND CENTER")
    
    # KPI Row
    k1, k2, k3, k4 = st.columns(4)
    k1.metric("Liquid Capital", f"${st.session_state.capital:,.0f}", "Ready to Deploy")
    k2.metric("Active Rehabs", "2", "Budget: $120k")
    k3.metric("Pipeline Value", "$3.4M", "8 Leads")
    k4.metric("Rental Cashflow", "$12,500/mo", "+5 Units")
    
    st.markdown("---")
    
    c_left, c_right = st.columns([2, 1])
    
    with c_left:
        st.subheader("🗺️ Nationwide Asset Map")
        # Comprehensive Map Data
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
# MODULE 2: CRM & LEADS (Hypothetical Scenarios)
# =========================================================
elif module == "CRM & LEADS (Active)":
    st.title("📇 CRM: LEAD PIPELINE")
    
    c1, c2 = st.columns([2, 1])
    
    with c1:
        st.subheader("Active Leads")
        # Editable Data Table for managing leads
        updated_leads = st.data_editor(st.session_state.leads, num_rows="dynamic", use_container_width=True)
        
    with c2:
        st.subheader("💬 Activity Log (Hypothetical)")
        st.selectbox("Select Lead to View History", st.session_state.leads["Address"])
        
        st.markdown("""
        **Today, 10:00 AM** - *Called Seller*
        > "Seller is motivated. Divorce situation. Needs to move in 30 days. Open to creative finance."
        
        **Yesterday, 4:30 PM** - *Sent Text*
        > "Hey John, just following up on our offer for 123 Maple."
        
        **Jan 15** - *Status Change*
        > Moved from 'New Lead' to 'Negotiating'.
        """)
        
        if st.button("➕ Log New Call"):
            st.toast("Call Logged: Seller didn't answer.")

# =========================================================
# MODULE 3: DEAL ARCHITECT (The Brain)
# =========================================================
elif module == "DEAL ARCHITECT (Analyze)":
    st.title("🏗️ DEAL ARCHITECT & CALCULATOR")
    
    # Input Section
    st.markdown("#### 1. PROPERTY VITALS")
    i1, i2, i3, i4 = st.columns(4)
    purchase_price = i1.number_input("Purchase Price", value=200000)
    arv = i2.number_input("ARV (After Repair)", value=350000)
    rehab_cost = i3.number_input("Rehab Estimate", value=50000)
    rent_est = i4.number_input("Est. Monthly Rent", value=2500)

    st.markdown("---")
    st.markdown("#### 2. STRATEGY COMPARISON")
    
    tab1, tab2, tab3 = st.tabs(["🔨 FLIP / WHOLESALE", "🏠 BRRRR STRATEGY", "🎨 CREATIVE (SUB-TO)"])
    
    # --- FLIP CALCULATOR ---
    with tab1:
        st.subheader("Flip & Wholesale Analysis")
        c1, c2 = st.columns(2)
        with c1:
            closing_costs = purchase_price * 0.03
            holding_costs = 5000 # hypothetical 4 months
            selling_costs = arv * 0.06 # agent fees
            total_cost = purchase_price + rehab_cost + closing_costs + holding_costs + selling_costs
            flip_profit = arv - total_cost
            
            st.metric(" Projected Net Profit (Flip)", f"${flip_profit:,.0f}")
            st.metric("ROI", f"{(flip_profit/total_cost)*100:.1f}%")
        
        with c2:
            st.markdown("**Wholesaler View**")
            mao = (arv * 0.70) - rehab_cost
            fee = mao - purchase_price
            st.metric("MAO (70% Rule)", f"${mao:,.0f}")
            st.metric("Wholesale Fee Potential", f"${fee:,.0f}")

    # --- BRRRR CALCULATOR ---
    with tab2:
        st.subheader("BRRRR: Buy, Rehab, Rent, Refinance, Repeat")
        
        # Hypothetical Refi Scenario
        refi_ltv = 0.75
        new_loan_amount = arv * refi_ltv
        cash_out = new_loan_amount - (purchase_price + rehab_cost) # simplified
        
        b1, b2, b3 = st.columns(3)
        b1.metric("1. All-In Cost", f"${purchase_price + rehab_cost:,.0f}")
        b2.metric("2. New Loan (75% ARV)", f"${new_loan_amount:,.0f}")
        b3.metric("3. Cash Left / (Out)", f"${(purchase_price + rehab_cost) - new_loan_amount:,.0f}")
        
        if new_loan_amount > (purchase_price + rehab_cost):
            st.success("✅ PERFECT BRRRR: You get all your money back + profit!")
        else:
            st.warning(f"⚠️ You leave ${(purchase_price + rehab_cost) - new_loan_amount:,.0f} in the deal.")

    # --- CREATIVE / SUB-TO ---
    with tab3:
        st.subheader("Creative Finance / Subject-To")
        st.caption("Hypothetical: Seller has $180k mortgage at 3%. We take over payments.")
        
        mortgage_balance = 180000
        interest_rate = 0.03
        monthly_payment = 950 # PITI
        
        entry_fee = purchase_price - mortgage_balance
        cashflow_subto = rent_est - monthly_payment - 300 # expenses
        
        s1, s2, s3 = st.columns(3)
        s1.metric("Cash to Seller (Entry)", f"${entry_fee:,.0f}")
        s2.metric("Mortgage Taken Over", f"${mortgage_balance:,.0f} @ {interest_rate*100}%")
        s3.metric("Monthly Net Cashflow", f"${cashflow_subto:,.0f}")
        
        st.success("Strategy: Low entry fee, high cashflow due to low inherited rate.")

# =========================================================
# MODULE 4: CONSTRUCTION (Rehabs)
# =========================================================
elif module == "CONSTRUCTION (Rehabs)":
    st.title("🚧 CONSTRUCTION MANAGER")
    
    col1, col2 = st.columns([1, 2])
    
    with col1:
        st.subheader("Budget Tracker")
        st.selectbox("Project", ["123 Maple (Full Gut)", "88 Ocean (Cosmetic)"])
        
        # Budget Item Hypotheticals
        budget_data = pd.DataFrame({
            "Item": ["Demolition", "Roof", "HVAC", "Kitchen", "Paint"],
            "Budget": [2000, 8000, 6000, 15000, 5000],
            "Actual": [2000, 10500, 6000, 12000, 0]
        })
        budget_data["Variance"] = budget_data["Actual"] - budget_data["Budget"]
        st.dataframe(budget_data, hide_index=True)
        
        st.error("⚠️ ALERT: Roof is $2,500 OVER Budget")
        
    with col2:
        st.subheader("Project Timeline")
        # Gantt Chart
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
# MODULE 5: RENTAL PORTFOLIO (Hold)
# =========================================================
elif module == "RENTAL PORTFOLIO (Hold)":
    st.title("🔑 RENTAL PORTFOLIO MANAGER")
    
    r1, r2, r3 = st.columns(3)
    r1.metric("Occupancy Rate", "92%", "11/12 Units")
    r2.metric("Total Monthly Rent", "$18,500", "Gross")
    r3.metric("Net Operating Income", "$12,100", "After Exp")
    
    st.markdown("### Tenant Roster (Hypothetical)")
    
    tenants = pd.DataFrame({
        "Address": ["Unit 1A", "Unit 1B", "Unit 2A", "House 44"],
        "Tenant": ["John Doe", "Jane Smith", "Mike Ross", "Sarah Connor"],
        "Rent ($)": [1200, 1200, 1400, 2500],
        "Lease End": ["2026-06-01", "2026-08-15", "2026-02-28", "M-to-M"],
        "Status": ["Paid", "Paid", "Late (3 Days)", "Paid"]
    })
    
    # Color code the table based on status logic (simplified visual)
    st.dataframe(tenants, use_container_width=True)
    
    st.warning("⚠️ **Alert:** Unit 2A (Mike Ross) is 3 days late. Auto-text sent.")
