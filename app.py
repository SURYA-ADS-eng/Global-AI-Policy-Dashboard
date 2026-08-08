import streamlit as st
import pandas as pd

# ==========================================================
# PAGE CONFIGURATION
# ==========================================================
st.set_page_config(
    page_title="Global AI Policy Dashboard",
    page_icon="🌍",
    layout="wide"
)

# ==========================================================
# TITLE
# ==========================================================
st.title("🌍 Global AI Policy Dashboard")

st.markdown("""
### Dashboard for Monitoring Global AI Policy Trends

This dashboard provides insights into AI policies across countries,
including policy maturity, compliance, ethics, investment,
and machine learning predictions.
""")

# ==========================================================
# LOAD DATASET
# ==========================================================
df = pd.read_csv("data/ai_final.csv")

# ==========================================================
# SIDEBAR FILTERS
# ==========================================================
st.sidebar.header("🔍 Filters")

# Country
country = st.sidebar.selectbox(
    "Select Country",
    ["All"] + sorted(df["country"].unique().tolist())
)

# Region
region = st.sidebar.selectbox(
    "Select Region",
    ["All"] + sorted(df["region"].unique().tolist())
)

# Year
year = st.sidebar.selectbox(
    "Select Year",
    ["All"] + sorted(df["year"].unique().tolist())
)

# Policy Type
policy_type = st.sidebar.selectbox(
    "Policy Type",
    ["All"] + sorted(df["policy_type"].unique().tolist())
)

# Policy Status
policy_status = st.sidebar.selectbox(
    "Policy Status",
    ["All"] + sorted(df["policy_status"].unique().tolist())
)

# ==========================================================
# APPLY FILTERS
# ==========================================================
filtered_df = df.copy()

if country != "All":
    filtered_df = filtered_df[
        filtered_df["country"] == country
    ]

if region != "All":
    filtered_df = filtered_df[
        filtered_df["region"] == region
    ]

if year != "All":
    filtered_df = filtered_df[
        filtered_df["year"] == year
    ]

if policy_type != "All":
    filtered_df = filtered_df[
        filtered_df["policy_type"] == policy_type
    ]

if policy_status != "All":
    filtered_df = filtered_df[
        filtered_df["policy_status"] == policy_status
    ]

# ==========================================================
# KPI CARDS
# ==========================================================
st.subheader("📊 Dashboard Overview")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        "📄 Total Records",
        len(filtered_df)
    )

with col2:
    st.metric(
        "🌍 Countries",
        filtered_df["country"].nunique()
    )

with col3:
    st.metric(
        "📑 Columns",
        len(filtered_df.columns)
    )

st.divider()

# ==========================================================
# DATASET PREVIEW
# ==========================================================
st.subheader("📋 Dataset Preview")

st.dataframe(
    filtered_df,
    use_container_width=True
)