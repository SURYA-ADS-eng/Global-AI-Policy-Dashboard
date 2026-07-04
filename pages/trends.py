import streamlit as st
import pandas as pd
import plotly.express as px

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

st.title("📈 AI Policy Trends Analysis")

st.markdown("""
Analyze AI policy growth, maturity, compliance,
ethical alignment and sentiment trends over time.
""")

st.markdown("---")

# ==========================================================
# SIDEBAR FILTERS
# ==========================================================

st.sidebar.header("📊 Trend Filters")

country = st.sidebar.selectbox(
    "Country",
    ["All"] + sorted(df["country"].unique())
)

region = st.sidebar.selectbox(
    "Region",
    ["All"] + sorted(df["region"].unique())
)

policy_type = st.sidebar.selectbox(
    "Policy Type",
    ["All"] + sorted(df["policy_type"].unique())
)

filtered_df = df.copy()

if country != "All":
    filtered_df = filtered_df[
        filtered_df["country"] == country
    ]

if region != "All":
    filtered_df = filtered_df[
        filtered_df["region"] == region
    ]

if policy_type != "All":
    filtered_df = filtered_df[
        filtered_df["policy_type"] == policy_type
    ]

# ==========================================================
# KPI CARDS
# ==========================================================

k1, k2, k3, k4 = st.columns(4)

with k1:
    st.metric(
        "Years Covered",
        filtered_df["year"].nunique()
    )

with k2:
    st.metric(
        "Average Maturity",
        round(filtered_df["policy_maturity_score"].mean(),2)
    )

with k3:
    st.metric(
        "Average Compliance",
        round(filtered_df["compliance_score"].mean(),2)
    )

with k4:
    st.metric(
        "Average Ethics",
        round(filtered_df["ethical_alignment_score"].mean(),2)
    )

st.markdown("---")

# ==========================================================
# POLICIES OVER YEARS
# ==========================================================

st.subheader("📈 Policies Published Over Time")

policy_year = (
    filtered_df.groupby("year")
    .size()
    .reset_index(name="Policies")
)

fig = px.line(
    policy_year,
    x="year",
    y="Policies",
    markers=True,
    title="Number of Policies"
)

st.plotly_chart(fig, use_container_width=True)

# ==========================================================
# POLICY MATURITY TREND
# ==========================================================

st.subheader("📊 Policy Maturity Trend")

maturity = (
    filtered_df.groupby("year")[
        "policy_maturity_score"
    ].mean().reset_index()
)

fig = px.line(
    maturity,
    x="year",
    y="policy_maturity_score",
    markers=True,
    color_discrete_sequence=["green"]
)

st.plotly_chart(fig, use_container_width=True)

# ==========================================================
# COMPLIANCE TREND
# ==========================================================

st.subheader("✅ Compliance Score Trend")

compliance = (
    filtered_df.groupby("year")[
        "compliance_score"
    ].mean().reset_index()
)

fig = px.line(
    compliance,
    x="year",
    y="compliance_score",
    markers=True,
    color_discrete_sequence=["blue"]
)

st.plotly_chart(fig, use_container_width=True)

# ==========================================================
# ETHICAL ALIGNMENT TREND
# ==========================================================

st.subheader("⚖ Ethical Alignment Trend")

ethics = (
    filtered_df.groupby("year")[
        "ethical_alignment_score"
    ].mean().reset_index()
)

fig = px.line(
    ethics,
    x="year",
    y="ethical_alignment_score",
    markers=True,
    color_discrete_sequence=["purple"]
)

st.plotly_chart(fig, use_container_width=True)

# ==========================================================
# POLICY SENTIMENT
# ==========================================================

left,right = st.columns(2)

with left:

    st.subheader("😊 Policy Sentiment")

    sentiment = (
        filtered_df.groupby("policy_sentiment")
        .size()
        .reset_index(name="Count")
    )

    fig = px.pie(
        sentiment,
        values="Count",
        names="policy_sentiment",
        hole=0.45
    )

    st.plotly_chart(fig,use_container_width=True)

with right:

    st.subheader("🚨 Alert Flag")

    alerts = (
        filtered_df.groupby("alert_flag")
        .size()
        .reset_index(name="Count")
    )

    fig = px.bar(
        alerts,
        x="alert_flag",
        y="Count",
        color="alert_flag",
        text_auto=True
    )

    st.plotly_chart(fig,use_container_width=True)

# ==========================================================
# POLICY RESTRICTIVENESS
# ==========================================================

st.subheader("📌 Policy Restrictiveness Trend")

restrict = (
    filtered_df.groupby("year")[
        "policy_restrictiveness_score"
    ].mean().reset_index()
)

fig = px.area(
    restrict,
    x="year",
    y="policy_restrictiveness_score"
)

st.plotly_chart(fig,use_container_width=True)

# ==========================================================
# DATA TABLE
# ==========================================================

st.markdown("---")

st.subheader("📋 Trend Dataset")

st.dataframe(
    filtered_df,
    use_container_width=True,
    height=400
)