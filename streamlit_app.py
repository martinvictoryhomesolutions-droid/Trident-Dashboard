import streamlit as st
import pandas as pd
import numpy as np

# --- PAGE CONFIGURATION (World Class Setup) ---
st.set_page_config(
    page_title="TRIDENT | Real Estate Investment",
    page_icon="🔱",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- CUSTOM CSS FOR HIGH-END BRANDING ---
st.markdown("""
    <style>
    .main {
        background-color: #0E1117;
        color: #FAFAFA;
    }
    h1, h2, h3 {
        color: #D4AF37; /* Gold for Luxury */
        font-family: 'Helvetica Neue', sans-serif;
    }
    .stMetric {
        background-color: #262730;
        padding: 15px;
        border-radius: 10px;
        border-left: 5px solid #D4AF37;
    }
    .stButton>button {
        background-color: #D4AF37;
        color: white;
        border-radius: 5px;
        border: none;
        width: 100%;
    }
    </style>
    """, unsafe_allow_html=True)

# --- SIDEBAR NAVIGATION ---
st.sidebar.title("🔱 TRIDENT SYSTEM")
st.sidebar.markdown("---")
page = st.sidebar.radio("Navigation", ["Dashboard", "Deal Calculator", "Market Intelligence", "Portfolio Tracker"])
st.sidebar.markdown("---")
st.sidebar.info("Identity: Real Estate Investor")

# --- 1. DASHBOARD ---
if page == "Dashboard":
    st.title("🔱 Executive Command Center")
    st.markdown("### Welcome back, Narcis.")
    
    # Top Level Metrics
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Active Deals", "3", "1 New")
    col2.metric("Portfolio Value", "$4.2M", "+12%")
    col3.metric("Monthly Cash Flow", "$38,500", "+5%")
    col4.metric("Capital Ready", "$850k", "Liquid")

    st.markdown("---")
    
    # Quick View of Deals
    st.subheader("🔥 Hot Leads")
    deals = pd.DataFrame({
        "Property": ["12 Ocean Dr", "45 Palm Ave", "88 Sunset Blvd"],
        "Type": ["Multi-Family", "Commercial", "Flip"],
        "Price": ["$1.2M", "$850k", "$450k"],
        "Proj. ROI": ["18%", "22%", "35%"],
        "Status": ["Negotiating", "Due Diligence", "New"]
    })
    st.dataframe(deals, use_container_width=True)

# --- 2. DEAL CALCULATOR ---
elif page == "Deal Calculator":
    st.title("🧮 Deal Analyzer")
    
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("Purchase Details")
        price = st.number_input("Purchase Price ($)", value=500000)
        reno = st.number_input("Renovation Cost ($)", value=50000)
        closing = st.number_input("Closing Costs ($)", value=15000)
    
    with col2:
        st.subheader("Income & Financing")
        arv = st.number_input("After Repair Value (ARV)", value=750000)
        rent = st.number_input("Monthly Rent ($)", value=4500)
        rate = st.slider("Interest Rate (%)", 3.0, 10.0, 6.5)

    # Calculation Engine
    total_investment = price + reno + closing
    equity = arv - total_investment
    roi = (equity / total_investment) * 100
    
    st.markdown("---")
    st.subheader("💰 Investment Outcome")
    
    m1, m2, m3 = st.columns(3)
    m1.metric("Total Investment", f"${total_investment:,.0f}")
    m2.metric("Instant Equity", f"${equity:,.0f}")
    m3.metric("Projected ROI", f"{roi:.1f}%")

    if roi > 20:
        st.success("✅ TRIDENT APPROVED: This deal meets your criteria.")
    else:
        st.warning("⚠️ CAUTION: Margins are tight.")

# --- 3. MARKET INTELLIGENCE ---
elif page == "Market Intelligence":
    st.title("📡 Market Recon")
    st.write("Live feed of market trends (Placeholder for API integration)")
    
    # Chart
    chart_data = pd.DataFrame(
        np.random.randn(20, 3),
        columns=['Miami', 'Austin', 'Tampa'])
    st.line_chart(chart_data)

# --- 4. PORTFOLIO TRACKER ---
elif page == "Portfolio Tracker":
    st.title("📂 Asset Portfolio")
    
    assets = pd.DataFrame({
        "Asset": ["Rental A", "Rental B", "Syndication X"],
        "Value": [1200000, 850000, 250000],
        "Cash Flow": [12000, 8500, 2500]
    })
    
    st.bar_chart(assets.set_index("Asset")["Value"])
