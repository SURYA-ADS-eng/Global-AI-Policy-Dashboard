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

st.title("🌍 Global AI Policy Analysis")

st.markdown("""
Analyze AI policy adoption, implementation strength,
government initiatives, and regional performance.
""")

st.markdown("---")

# ==========================================================
# SIDEBAR FILTERS
# ==========================================================

st.sidebar.header("🌍 Global Analysis Filters")

country = st.sidebar.selectbox(
    "Country",
    ["All"] + sorted(df["country"].unique())
)

region = st.sidebar.selectbox(
    "Region",
    ["All"] + sorted(df["region"].unique())
)

year = st.sidebar.selectbox(
    "Year",
    ["All"] + sorted(df["year"].unique())
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

if year != "All":
    filtered_df = filtered_df[
        filtered_df["year"] == year
    ]

# ==========================================================
# KPI CARDS
# ==========================================================

k1, k2, k3, k4 = st.columns(4)

with k1:
    st.metric(
        "Countries",
        filtered_df["country"].nunique()
    )

with k2:
    st.metric(
        "Regions",
        filtered_df["region"].nunique()
    )

with k3:
    st.metric(
        "Avg AI Investment",
        round(filtered_df["ai_investment_index"].mean(),2)
    )

with k4:
    st.metric(
        "Avg Research Output",
        round(filtered_df["ai_research_output"].mean(),2)
    )

st.markdown("---")

# ==========================================================
# ROW 1
# ==========================================================

col1, col2 = st.columns(2)

with col1:

    st.subheader("🌍 AI Investment by Region")

    investment = filtered_df.groupby(
        "region"
    )["ai_investment_index"].mean().reset_index()

    fig = px.bar(
        investment,
        x="region",
        y="ai_investment_index",
        color="region",
        text_auto=".2f",
        title="Average AI Investment"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

with col2:

    st.subheader("🏛 Government AI Policy")

    gov = filtered_df.groupby(
        "government_ai_policy"
    ).size().reset_index(name="Count")

    fig = px.pie(
        gov,
        values="Count",
        names="government_ai_policy",
        hole=.45
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

# ==========================================================
# ROW 2
# ==========================================================

col3, col4 = st.columns(2)

with col3:

    st.subheader("⚖ Implementation Strength")

    imp = filtered_df.groupby(
        "implementation_strength"
    ).size().reset_index(name="Count")

    fig = px.bar(
        imp,
        x="implementation_strength",
        y="Count",
        color="implementation_strength",
        text_auto=True
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

with col4:

    st.subheader("⚠ Regulatory Risk Level")

    risk = filtered_df.groupby(
        "regulatory_risk_level"
    ).size().reset_index(name="Count")

    fig = px.pie(
        risk,
        values="Count",
        names="regulatory_risk_level",
        hole=.5
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

# ==========================================================
# ROW 3
# ==========================================================

st.subheader("🏆 Top 10 Countries by Policy Maturity")

top = (
    filtered_df.groupby("country")[
        "policy_maturity_score"
    ]
    .mean()
    .sort_values(ascending=False)
    .head(10)
    .reset_index()
)

fig = px.bar(
    top,
    x="country",
    y="policy_maturity_score",
    color="policy_maturity_score",
    text_auto=".2f"
)

st.plotly_chart(
    fig,
    use_container_width=True
)

# ==========================================================
# WORLD MAP
# ==========================================================

st.subheader("🗺 Global AI Investment Map")

fig = px.choropleth(
    filtered_df,
    locations="country",
    locationmode="country names",
    color="ai_investment_index",
    hover_name="country",
    color_continuous_scale="Viridis",
    title="AI Investment by Country"
)

st.plotly_chart(
    fig,
    use_container_width=True
)

# ==========================================================
# DATA TABLE
# ==========================================================

st.markdown("---")

st.subheader("📋 Global Analysis Dataset")

st.dataframe(
    filtered_df,
    use_container_width=True,
    height=400
)