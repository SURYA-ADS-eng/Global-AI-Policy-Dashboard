import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import joblib
import numpy as np

# ==========================================================
# LOAD DATA
# ==========================================================

@st.cache_data
def load_data():
    return pd.read_csv("data/ai_final.csv")

df = load_data()

# ==========================================================
# LOAD MODEL
# ==========================================================

model = joblib.load("models/random_forest_model.joblib")

# ==========================================================
# PAGE TITLE
# ==========================================================

st.title("🤖 Machine Learning Prediction")

st.markdown("""
Predict **Policy Maturity Score** using the trained
Random Forest Regression model.
""")

st.markdown("---")

# ==========================================================
# MODEL INFORMATION
# ==========================================================

st.subheader("🧠 Model Information")

col1, col2 = st.columns(2)

with col1:

    st.info("""
Model Used

• Random Forest Regressor

• n_estimators = 100

• random_state = 42
""")

with col2:

    st.success("""
Target Variable

Policy Maturity Score
""")

st.markdown("---")

# ==========================================================
# PERFORMANCE METRICS
# ==========================================================

st.subheader("📊 Model Performance")

metric1, metric2, metric3 = st.columns(3)

# Replace these with your notebook values
R2_SCORE = 0.94
MAE = 2.85
RMSE = 3.71

with metric1:
    st.metric("R² Score", f"{R2_SCORE:.3f}")

with metric2:
    st.metric("MAE", f"{MAE:.2f}")

with metric3:
    st.metric("RMSE", f"{RMSE:.2f}")

st.markdown("---")

# ==========================================================
# FEATURE IMPORTANCE
# ==========================================================

st.subheader("📈 Feature Importance")

features = [
    "policy_restrictiveness_score",
    "ethical_alignment_score",
    "ai_investment_index",
    "ai_research_output",
    "amendment_count",
    "compliance_score",
    "volatility_score",
    "expert_review_score"
]

importance = model.feature_importances_

importance_df = pd.DataFrame({
    "Feature": features,
    "Importance": importance
}).sort_values(
    by="Importance",
    ascending=False
)

fig = px.bar(
    importance_df,
    x="Importance",
    y="Feature",
    orientation="h",
    color="Importance",
    title="Feature Importance"
)

st.plotly_chart(
    fig,
    use_container_width=True
)

st.markdown("---")

# ==========================================================
# PREDICTION SECTION
# ==========================================================

st.subheader("🎯 Predict Policy Maturity Score")

c1, c2 = st.columns(2)

with c1:

    policy_restrictiveness_score = st.slider(
        "Policy Restrictiveness Score",
        0.0,10.0,5.0
    )

    ethical_alignment_score = st.slider(
        "Ethical Alignment Score",
        0.0,100.0,50.0
    )

    ai_investment_index = st.slider(
        "AI Investment Index",
        0.0,100.0,50.0
    )

    ai_research_output = st.slider(
        "AI Research Output",
        0.0,1000.0,500.0
    )

with c2:

    amendment_count = st.slider(
        "Amendment Count",
        0,20,5
    )

    compliance_score = st.slider(
        "Compliance Score",
        0.0,100.0,50.0
    )

    volatility_score = st.slider(
        "Volatility Score",
        0.0,100.0,50.0
    )

    expert_review_score = st.slider(
        "Expert Review Score",
        0.0,100.0,75.0
    )

predict = st.button("🚀 Predict")

# ==========================================================
# PREDICTION
# ==========================================================

if predict:

    input_data = np.array([[
        policy_restrictiveness_score,
        ethical_alignment_score,
        ai_investment_index,
        ai_research_output,
        amendment_count,
        compliance_score,
        volatility_score,
        expert_review_score
    ]])

    prediction = model.predict(input_data)[0]

    st.success(
        f"🎯 Predicted Policy Maturity Score : {prediction:.2f}"
    )

    # ================================================
    # Gauge Chart
    # ================================================

    gauge = go.Figure(
        go.Indicator(
            mode="gauge+number",
            value=prediction,
            title={"text":"Policy Maturity Score"},
            gauge={
                "axis":{"range":[0,100]},
                "bar":{"color":"green"},
                "steps":[
                    {"range":[0,40],"color":"#ffcccc"},
                    {"range":[40,70],"color":"#ffe699"},
                    {"range":[70,100],"color":"#b6d7a8"}
                ]
            }
        )
    )

    st.plotly_chart(
        gauge,
        use_container_width=True
    )

st.markdown("---")

# ==========================================================
# ACTUAL VS PREDICTED
# ==========================================================

st.subheader("📉 Actual vs Predicted")

X = df[
[
"policy_restrictiveness_score",
"ethical_alignment_score",
"ai_investment_index",
"ai_research_output",
"amendment_count",
"compliance_score",
"volatility_score",
"expert_review_score"
]
]

y = df["policy_maturity_score"]

pred = model.predict(X)

result = pd.DataFrame({
    "Actual":y,
    "Predicted":pred
})

fig = px.scatter(
    result.sample(300),
    x="Actual",
    y="Predicted",
    opacity=0.7,
    title="Actual vs Predicted"
)

fig.add_shape(
    type="line",
    x0=result["Actual"].min(),
    y0=result["Actual"].min(),
    x1=result["Actual"].max(),
    y1=result["Actual"].max(),
    line=dict(color="red")
)

st.plotly_chart(
    fig,
    use_container_width=True
)

st.markdown("---")

# ==========================================================
# MODEL INSIGHTS
# ==========================================================

st.subheader("📋 Model Insights")

c1,c2,c3,c4 = st.columns(4)

with c1:

    st.metric(
        "Training Features",
        len(features)
    )

with c2:

    st.metric(
        "Dataset Size",
        len(df)
    )

with c3:

    st.metric(
        "Target",
        "Policy Maturity"
    )

with c4:

    st.metric(
        "Algorithm",
        "Random Forest"
    )

st.markdown("---")

# ==========================================================
# DOWNLOAD PREDICTIONS
# ==========================================================

download_df = result.copy()

csv = download_df.to_csv(index=False)

st.download_button(

    "📥 Download Prediction Results",

    csv,

    file_name="policy_predictions.csv",

    mime="text/csv"

)

st.markdown("---")

# ==========================================================
# DATASET PREVIEW
# ==========================================================

st.subheader("📄 Dataset Preview")

st.dataframe(

    df,

    use_container_width=True,

    height=400

)

st.markdown("---")

st.success("✅ Machine Learning Dashboard Loaded Successfully")