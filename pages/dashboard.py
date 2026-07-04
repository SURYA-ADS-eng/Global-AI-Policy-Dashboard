import streamlit as st
import pandas as pd
import plotly.express as px

# ==========================================================
# PAGE CONFIGURATION
# ==========================================================
st.set_page_config(
    page_title="Dashboard",
    page_icon="📊",
    layout="wide"
)

# ==========================================================
# LOAD DATA
# ==========================================================
@st.cache_data
def load_data():
    return pd.read_csv("data/ai_final.csv")

df = load_data()

# ==========================================================
# PAGE TITLE
# ==========================================================
st.title("🌍 Dashboard for Monitoring Global AI Policy Trends")

st.markdown(
"""
This dashboard provides an overview of global AI policies,
policy maturity, compliance, ethics, and AI investment trends.
"""
)

st.markdown("---")

# ==========================================================
# SIDEBAR FILTERS
# ==========================================================

st.sidebar.header("🔍 Dashboard Filters")

country = st.sidebar.selectbox(
    "🌍 Country",
    ["All"] + sorted(df["country"].unique().tolist())
)

region = st.sidebar.selectbox(
    "🌎 Region",
    ["All"] + sorted(df["region"].unique().tolist())
)

year = st.sidebar.selectbox(
    "📅 Year",
    ["All"] + sorted(df["year"].unique().tolist())
)

policy_type = st.sidebar.selectbox(
    "📑 Policy Type",
    ["All"] + sorted(df["policy_type"].unique().tolist())
)

policy_status = st.sidebar.selectbox(
    "📌 Policy Status",
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

st.subheader("📊 Key Performance Indicators")

kpi1, kpi2, kpi3 = st.columns(3)

with kpi1:

    st.metric(
        "📄 Total Policies",
        len(filtered_df)
    )

with kpi2:

    st.metric(
        "🌍 Countries",
        filtered_df["country"].nunique()
    )

with kpi3:

    st.metric(
        "📈 Avg Policy Maturity",
        f"{filtered_df['policy_maturity_score'].mean():.2f}"
    )

kpi4, kpi5, kpi6 = st.columns(3)

with kpi4:

    st.metric(
        "✅ Avg Compliance",
        f"{filtered_df['compliance_score'].mean():.2f}"
    )

with kpi5:

    st.metric(
        "⚖ Avg Ethical Alignment",
        f"{filtered_df['ethical_alignment_score'].mean():.2f}"
    )

with kpi6:

    st.metric(
        "💰 Avg AI Investment",
        f"{filtered_df['ai_investment_index'].mean():.2f}"
    )

st.markdown("---")

# ==========================================================
# CHARTS ROW 1
# ==========================================================

left_col, right_col = st.columns(2)

# ---------------- Region Distribution ----------------

with left_col:

    st.subheader("🌍 Region Distribution")

    region_chart = (
        filtered_df.groupby("region")
        .size()
        .reset_index(name="Policies")
    )

    fig_region = px.bar(
        region_chart,
        x="region",
        y="Policies",
        color="Policies",
        text="Policies",
        title="Policies by Region",
    )

    fig_region.update_layout(
        template="plotly_white",
        xaxis_title="Region",
        yaxis_title="Number of Policies",
    )

    st.plotly_chart(fig_region, use_container_width=True)


# ---------------- Policy Type ----------------

with right_col:

    st.subheader("📑 Policy Type Distribution")

    policy_type_chart = (
        filtered_df.groupby("policy_type")
        .size()
        .reset_index(name="Count")
    )

    fig_type = px.pie(
        policy_type_chart,
        names="policy_type",
        values="Count",
        hole=0.45,
        title="Policy Type Distribution",
    )

    st.plotly_chart(fig_type, use_container_width=True)


# ==========================================================
# CHARTS ROW 2
# ==========================================================

left2, right2 = st.columns(2)

# ---------------- Policy Status ----------------

with left2:

    st.subheader("📌 Policy Status")

    status_chart = (
        filtered_df.groupby("policy_status")
        .size()
        .reset_index(name="Count")
    )

    fig_status = px.pie(
        status_chart,
        names="policy_status",
        values="Count",
        hole=0.55,
        title="Policy Status Distribution",
    )

    st.plotly_chart(fig_status, use_container_width=True)


# ---------------- Policy Domain ----------------

with right2:

    st.subheader("🌳 Policy Domain")

    domain_chart = (
        filtered_df.groupby("policy_domain")
        .size()
        .reset_index(name="Count")
    )

    fig_domain = px.treemap(
        domain_chart,
        path=["policy_domain"],
        values="Count",
        color="Count",
        title="Policy Domain Distribution",
    )

    st.plotly_chart(fig_domain, use_container_width=True)


# ==========================================================
# DATASET PREVIEW
# ==========================================================

st.markdown("---")

st.subheader("📋 Dataset Preview")

st.dataframe(
    filtered_df,
    use_container_width=True,
    height=400,
)