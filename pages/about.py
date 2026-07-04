import streamlit as st
import pandas as pd

# ==========================================================
# PAGE TITLE
# ==========================================================

st.title("ℹ️ About This Project")

st.markdown("""
# 🌍 Global AI Policy Dashboard

An interactive AI-powered analytics dashboard developed using
**Python, Streamlit, Machine Learning, and Plotly** to monitor,
analyze, and predict global AI policy trends.

---
""")

# ==========================================================
# PROJECT OVERVIEW
# ==========================================================

st.header("📖 Project Overview")

st.write("""
The **Global AI Policy Dashboard** provides policymakers,
researchers, educators, and AI enthusiasts with interactive
visualizations and machine learning insights into AI policy
adoption across multiple countries.

The project combines:

- Data Analytics
- Data Visualization
- Machine Learning
- Interactive Dashboard
- Policy Trend Analysis

into one application.
""")

st.markdown("---")

# ==========================================================
# OBJECTIVES
# ==========================================================

st.header("🎯 Objectives")

st.markdown("""
- Monitor Global AI Policies
- Compare AI adoption across countries
- Analyze policy maturity
- Evaluate compliance scores
- Analyze ethical alignment
- Predict Policy Maturity Score using Machine Learning
""")

st.markdown("---")

# ==========================================================
# DATASET INFORMATION
# ==========================================================

st.header("📂 Dataset")

st.write("""
Dataset contains information about

- AI Policies
- Countries
- Regions
- AI Investment
- Compliance Score
- Ethical Alignment
- AI Research Output
- Government AI Policy
- Policy Status
- Policy Type
- Policy Domain
- Alert Flags
- Policy Versions

Total Features : **48**
""")

st.markdown("---")

# ==========================================================
# TECHNOLOGIES USED
# ==========================================================

st.header("💻 Technologies")

tech = pd.DataFrame({

    "Technology":[
        "Python",
        "Streamlit",
        "Pandas",
        "NumPy",
        "Plotly",
        "Scikit-learn",
        "Joblib",
        "Git",
        "GitHub"
    ],

    "Purpose":[
        "Programming",
        "Dashboard Development",
        "Data Processing",
        "Numerical Computing",
        "Interactive Visualization",
        "Machine Learning",
        "Model Loading",
        "Version Control",
        "Project Hosting"
    ]

})

st.dataframe(
    tech,
    use_container_width=True
)

st.markdown("---")

# ==========================================================
# MACHINE LEARNING MODEL
# ==========================================================

st.header("🤖 Machine Learning")

st.write("""

Algorithm Used

✅ Random Forest Regressor

Target Variable

✅ Policy Maturity Score

Model predicts policy maturity based on

- Policy Restrictiveness
- Ethical Alignment
- AI Investment
- AI Research Output
- Amendment Count
- Compliance Score
- Volatility Score
- Expert Review Score

""")

st.markdown("---")

# ==========================================================
# DASHBOARD FEATURES
# ==========================================================

st.header("📊 Dashboard Modules")

st.markdown("""

🏠 Home

📊 Dashboard

🌍 Global Analysis

📈 Policy Trends

🤖 Machine Learning

ℹ About

""")

st.markdown("---")

# ==========================================================
# DEVELOPER
# ==========================================================

st.header("👨‍💻 Developer")

st.success("""

Name:
Surya S

Department:
Artificial Intelligence and Data Science

Project:
Global AI Policy Dashboard

Developed using

Python
Streamlit
Machine Learning
Plotly

""")

st.markdown("---")

# ==========================================================
# FUTURE ENHANCEMENTS
# ==========================================================

st.header("🚀 Future Enhancements")

st.markdown("""

✅ Live Policy API Integration

✅ Real-time AI News

✅ User Authentication

✅ PDF Report Generation

✅ AI Chat Assistant

✅ Advanced Deep Learning Models

✅ Cloud Deployment

""")

st.markdown("---")

st.info(
    "Thank you for exploring the Global AI Policy Dashboard."
)

st.success("Project Completed Successfully ✅")