import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go

# --- 1. PAGE CONFIGURATION (Wide Mode for Cockpit View) ---
st.set_page_config(
    page_title="TRIDENT | Real Estate Protector",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="collapsed" # Hiding standard sidebar to use custom panels
)

# --- 2. TITAN VISUAL IDENTITY (Dark Navy/Slate Theme) ---
st.markdown("""
    <style>
    /* Main Background - Dark Slate Blue like the image */
    .stApp {
        background-color: #0F172A;
        color: #E2E8F0;
    }
    
    /* Card/Panel Backgrounds */
    div[data-testid="stVerticalBlock"] > div {
        background-color: #1E293B;
        border-radius: 10px;
        padding: 10px;
        border: 1px solid #334155;
    }
    
    /* Headers - Gold & White */
    h1, h2, h3 {
        color: #F8FAFC !important;
        font-family: 'Helvetica Neue', sans-serif;
        font-weight: 700;
    }
    h4, h5, h6 {
        color: #94A3B8 !important;
        text-transform: uppercase;
        font-size: 12px;
    }

    /* Metrics (Top Bar) */
    div[data-testid="stMetricValue"] {
        color: #38BDF8 !important; /* Cyan Blue for numbers */
        font-size: 24px !important;
    }
    div[data-testid="stMetricLabel"] {
        color: #94A3B8;
    }

    /* Buttons (Green Approve / Red Deny) */
    .approve-btn > button {
        background-color: #10B981 !important; /* Green */
        color: white !important;
        border: none;
    }
    .deny-btn > button {
        background-color: #EF4444 !important; /* Red */
        color: white !important;
        border: none;
    }
    
    /* Map Container Fix */
    iframe {
        border-radius: 10px;
        border: 1px solid #334155;
    }
    </style>
    """, unsafe_allow_html=True)

# --- 3. TOP LEVEL METRICS (The "Heads Up Display") ---
st.title("🛡️ TRIDENT PROTECTOR COMMAND")

# Top Metrics Row
m1, m2, m3, m4, m5 = st.columns(5)
m1.metric("Total Lent", "$450,000", "Lender's Vault")
m2.metric("Active Loans", "3", "Performing")
m3.metric("Blended Return", "12.5%", "+2.1%")
m4.metric("Fresh Catches", "5", "New Leads")
m5.metric("Wholesaler Deals", "12", "Pending Review")

st.markdown("---")

# --- 4. THE COCKPIT LAYOUT (3 Columns) ---
# Left: Alerts | Middle: Map | Right: Actions
col_left, col_mid, col_right = st.columns([1.5, 4, 2])

# === LEFT PANEL: ALERTS ===
with col_left:
    st.markdown("### 🔔 RECENT ALERTS")
    
    # Alert 1
    st.info("**Shark Deal (Atlanta)**\n\nMargin: 35% | Speed: High\n\n*12 mins ago*")
    
    # Alert 2
    st.warning("**Fresh Catch (Owner)**\n\nMotivated Seller - Divorce\n\n*1 hour ago*")
    
    # Alert 3
    st.error("**Draw Request**\n\n123 Maple Ave - Roofing\n\n*$5,000 Pending*")
    
    # Alert 4
    st.success("**Wholesaler Deal**\n\nOff-Market Duplex\n\n*3 hours ago*")

# === MIDDLE PANEL: THE MAP ===
with col_mid:
    st.markdown("### 🗺️ NATIONWIDE INTEL")
    
    # Creating a Dark Mode Map using Plotly
    # Locations: Miami, Atlanta, Austin, Phoenix
    map_data = pd.DataFrame({
        'lat': [25.7617, 33.7490, 30.2672, 33.4484, 40.7128],
        'lon': [-80.1918, -84.3880, -97.7431, -112.0740, -74.0060],
        'Type': ['HQ', 'Shark Deal', 'Fresh Catch', 'Wholesale', 'Active Loan'],
        'Size': [20, 15, 15, 15, 15],
        'Color': ['#38BDF8', '#EF4444', '#F59E0B', '#10B981', '#ffffff']
    })

    fig = px.scatter_mapbox(
        map_data, 
        lat="lat", 
        lon="lon", 
        hover_name="Type",
        color="Type",
        size="Size",
        color_discrete_sequence=['#38BDF8', '#EF4444', '#F59E0B', '#10B981', '#ffffff'],
        zoom=3,
        height=600
    )
    
    # visual settings for Dark Map
    fig.update_layout(
        mapbox_style="carto-darkmatter", # THE DARK THEME
        margin={"r":0,"t":0,"l":0,"b":0},
        paper_bgcolor="#1E293B",
        showlegend=False
    )
    
    st.plotly_chart(fig, use_container_width=True)
    
    # Map Filters underneath
    f1, f2, f3 = st.columns(3)
    f1.checkbox("Show Crime Heatmap", value=True)
    f2.checkbox("Show School Ratings")
    f3.checkbox("Show MLS Listings")

# === RIGHT PANEL: LENDER'S VAULT ===
with col_right:
    st.markdown("### 🏦 LENDER'S VAULT")
    
    st.image("https://images.unsplash.com/photo-1568605114967-8130f3a36994?ixlib=rb-1.2.1&auto=format&fit=crop&w=800&q=80", use_container_width=True)
    st.markdown("#### 123 Maple Ave (Flip Project)")
    st.caption("Borrower: Mauee Ave LLC")
    
    st.progress(75, text="Project Completion: 75%")
    
    st.markdown("---")
    
    st.markdown("#### ⚠️ ACTION REQUIRED")
    st.write("**Draw Request: Roofing**")
    st.write("Amount: **$5,000.00**")
    
    # Custom Columns for Buttons to mimic the image
    btn_col1, btn_col2 = st.columns(2)
    with btn_col1:
        # Green Button Trick
        st.markdown('<span class="approve-btn">', unsafe_allow_html=True)
        if st.button("✅ APPROVE", use_container_width=True):
            st.toast("Funds Released to Borrower!")
        st.markdown('</span>', unsafe_allow_html=True)
        
    with btn_col2:
        # Red Button Trick
        st.markdown('<span class="deny-btn">', unsafe_allow_html=True)
        if st.button("❌ DENY", use_container_width=True):
            st.toast("Request Denied.")
        st.markdown('</span>', unsafe_allow_html=True)

    st.markdown("---")
    st.markdown("#### 📂 ACTIVE PORTFOLIO")
    
    # Mini List of properties
    st.markdown("""
    * **123 Maple Ave** - *Roofing Phase*
    * **88 Ocean Dr** - *Permitting*
    * **909 Industrial** - *Tenant Placement*
    """)
