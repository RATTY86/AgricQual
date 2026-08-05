# app.py
import streamlit as st
import pandas as pd
import joblib
import plotly.express as px
import os   

# ==============================
# PATH FIX (PUT IT HERE)
# ==============================
# Setup Page Layout
st.set_page_config(page_title="AgricQual App", layout="wide")

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MODEL_PATH = os.path.join(BASE_DIR, "model", "rf_agricqual_model.joblib")
DATA_PATH = os.path.join(BASE_DIR, "dataset", "agricqual_dataset.csv")

st.markdown(
    """
    <style>
    /* Hide Streamlit default menu and footer */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}

    /* App background and card style */
    .stApp {
        background-color: #181c20;
        color: #f5f6fa;
    }
    .stTabs [data-baseweb="tab-list"] {
        gap: 2rem;
        justify-content: center;
        background: #23272f;
        border-radius: 12px 12px 0 0;
        padding: 0.5rem 0;
        margin-bottom: 2rem;
    }
    .stTabs [data-baseweb="tab"] {
        font-size: 1.3rem;
        font-weight: 600;
        color: #bfc9d1;
        padding: 0.9rem 2.5rem;
        border-radius: 8px 8px 0 0;
        transition: background 0.2s, color 0.2s;
    }
    .stTabs [aria-selected="true"] {
        background: #2d313a;
        color: #00cc96;
    }
    .stTabs [aria-selected="false"]:hover {
        background: #23272f;
        color: #fff;
    }
    /* Larger typography for readability */
    .stMarkdown h1 {
        font-size: 3rem;
    }
    .stMarkdown h2 {
        font-size: 2.4rem;
    }
    .stMarkdown h3 {
        font-size: 1.8rem;
    }
    .stMarkdown p,
    .stMarkdown li,
    .stText,
    .stMetric label,
    .stMetricValue,
    .stNumberInput label,
    .stSelectbox label,
    .stButton button,
    .stExpanderHeader,
    .css-1kyxreq {
        font-size: 1.2rem !important;
    }
    .block-container,
    .stApp,
    .stMarkdown,
    .stText,
    .stMetric,
    .stNumberInput,
    .stSelectbox,
    .stButton {
        font-size: 1.15rem !important;
    }
    .stNumberInput input,
    .stSelectbox div[data-baseweb="select"] {
        background: #23272f;
        color: #f5f6fa;
        border-radius: 6px;
        border: 1px solid #333;
    }
    label, .stSelectbox label {
        color: #bfc9d1 !important;
        font-weight: 500;
    }

    /* Responsive Design for Mobile and Tablets */
    @media (max-width: 768px) {
        .stTabs [data-baseweb="tab-list"] {
            flex-direction: column;
            gap: 0.5rem;
            padding: 0.5rem;
        }
        .stTabs [data-baseweb="tab"] {
            font-size: 1rem;
            padding: 0.5rem 1rem;
            width: 100%;
            text-align: center;
        }
        .stColumns > div {
            width: 100% !important;
            margin-bottom: 1rem;
        }
        .stNumberInput, .stSelectbox {
            width: 100%;
        }
        .stMarkdown h1, .stMarkdown h2, .stMarkdown h3 {
            font-size: 1.5rem;
        }
        .stButton button {
            width: 100%;
            padding: 0.75rem;
        }
        section[data-testid="stSidebar"] {
            display: none !important;
        }
        .stApp {
            padding-left: 0 !important;
        }
    }

    @media (max-width: 480px) {
        .stTabs [data-baseweb="tab"] {
            font-size: 0.9rem;
            padding: 0.4rem 0.8rem;
        }
        .stMarkdown p, .stMarkdown li {
            font-size: 0.9rem;
        }
    }
    </style>
    """,
    unsafe_allow_html=True
)



# Top Navigation Tabs
tab_compliance, tab_home, tab_regulator, tab_policy, tab_privacy = st.tabs(["📝 Compliance Assessment", "🏠 Home", "📊 Regulator Dashboard", "📋 Policy", "🔒 Data Protection"])

# Add sidebar for additional info
with st.sidebar:
    st.title("🌾 AgricQual")
    st.write("**Decision-support system for farmers, cooperatives, and export regulators.**")
    st.write("---")
    st.write("### 📊 Key Features:")
    st.write("- Real-time compliance assessment")
    st.write("- ML-powered predictions")
    st.write("- Historical data insights")
    st.write("- Codex/EU standards checking")
    st.write("---")
    st.write("**Version:** 1.0")
    st.write("**Model:** Random Forest Classifier")

# ==========================================
# 4.3.2 BACKEND INTEGRATION: Load Assets
# ==========================================
@st.cache_resource
def load_model():
    # Load the trained Random Forest model (saved using Joblib)
    return joblib.load(MODEL_PATH)

@st.cache_data
def load_historical_data():
    return pd.read_csv(DATA_PATH)

rf_model = load_model()
history_df = load_historical_data()

# ==========================================
# 4.3.1 FRONTEND INTERFACE: UI Components
# ==========================================

with tab_compliance:
    st.header("📝 Compliance Assessment")
    st.markdown("Enter the quality parameters for your agricultural batch below. The system will analyze compliance with Codex Alimentarius and EU standards.")
    
    # Input fields for food quality parameters
    st.subheader("Batch Parameters")
    col1, col2, col3 = st.columns(3)
    with col1:
        moisture = st.number_input("Moisture Content (%)", min_value=0.0, value=10.0, step=0.1, help="Maximum allowed: 12.0%", key="moisture")
        microbial = st.number_input("Microbial Load (CFU/g)", min_value=0, value=15000, step=100, help="Maximum allowed: 25,000 CFU/g", key="microbial")
        temp = st.number_input("Storage Temperature (°C)", min_value=-10.0, value=25.0, step=0.5, key="temp")

    with col2:
        pesticide = st.number_input("Pesticide Residue (mg/kg)", min_value=0.0, value=0.02, step=0.01, help="EU maximum: 0.05 mg/kg", key="pesticide")
        heavy = st.number_input("Heavy Metals (mg/kg)", min_value=0.0, value=0.05, step=0.01, help="Maximum allowed: 0.1 mg/kg", key="heavy")

    with col3:
        aflatoxin = st.number_input("Aflatoxin B1 (µg/kg)", min_value=0.0, value=2.0, step=0.1, help="Codex maximum: 5.0 µg/kg", key="aflatoxin")
        storage = st.number_input("Storage Duration (Days)", min_value=0, value=30, step=1, key="storage")
        packaging = st.selectbox("Packaging Integrity", ["Good", "Fair", "Poor"], help="Select the current packaging condition", key="packaging")

    # Predict button
    st.write("---")
    if st.button("🔍 Assess Compliance", type="primary"):
        
        # --- BACKEND EXECUTION ---
        
        # 1. Transform inputs into model-ready format
        packaging_map = {"Good": 2, "Fair": 1, "Poor": 0}
        input_data = pd.DataFrame([[
            moisture, pesticide, aflatoxin, microbial, 
            heavy, storage, temp, packaging_map[packaging]
        ]], columns=[
            "moisture_content", "pesticide_residue", "aflatoxin_b1", "microbial_load", 
            "heavy_metals", "storage_duration", "temperature", "packaging_integrity"
        ])
        
        # 2. Evaluate input thresholds first (threshold violations override ML prediction)
        strict_reasons = []
        warning_reasons = []

        if moisture > 12.0:
            strict_reasons.append(f"Moisture ({moisture}%) exceeds maximum of 12.0%.")
        if pesticide > 0.05:
            strict_reasons.append(f"Pesticide ({pesticide} mg/kg) exceeds EU maximum of 0.05 mg/kg.")
        if aflatoxin > 5.0:
            strict_reasons.append(f"Aflatoxin ({aflatoxin} µg/kg) exceeds Codex maximum of 5.0 µg/kg.")
        if microbial > 25000:
            strict_reasons.append(f"Microbial load ({microbial} CFU/g) is critically high.")
        if heavy > 0.1:
            strict_reasons.append(f"Heavy Metals ({heavy} mg/kg) exceeds maximum of 0.1 mg/kg.")

        if storage > 30:
            warning_reasons.append(f"Storage duration ({storage} days) exceeds recommended 30 days.")
        if temp < 0 or temp > 25:
            warning_reasons.append(f"Storage temperature ({temp}°C) is outside the recommended 0–25°C range.")
        if packaging != "Good":
            warning_reasons.append(f"Packaging integrity is {packaging}.")

        # --- FRONTEND OUTPUT ---
        
        # Compliance output panel
        st.header("Assessment Results")
        if strict_reasons or warning_reasons:
            st.error("❌ **Prediction: Non-Compliant** - One or more threshold limits were violated.")
            if strict_reasons:
                with st.expander("📋 **Threshold Violations:**"):
                    for reason in strict_reasons:
                        st.write(f"- {reason}")
            if warning_reasons:
                with st.expander("⚠️ **Warnings (Storage / Temperature / Packaging):**"):
                    for reason in warning_reasons:
                        st.write(f"- {reason}")
        else:
            # 3. Run prediction through Random Forest only when thresholds are satisfied
            prediction = rf_model.predict(input_data)[0]
            if prediction == 1:
                st.success("✅ **Prediction: Compliant** - This batch is approved for export.")
            else:
                st.error("❌ **Prediction: Non-Compliant** - This batch is rejected for export.")
                with st.expander("📋 **Detailed Reasons:**"):
                    st.write("- Model detected non-linear failure patterns based on historical training data.")

with tab_home:
    st.title("🌾 Welcome to AgricQual")
    # st.image("asset/logo.png", width=300, caption="AgricQual Logo")  # Disabled for now
    st.markdown("""
    ### About AgricQual
    AgricQual is an AI-powered decision-support system designed to help farmers, cooperatives, and export regulators assess the compliance of agricultural products with international standards.
    
    ### How It Works
    1. **Input Parameters**: Enter quality metrics for your batch
    2. **AI Analysis**: Our machine learning model evaluates compliance
    3. **Instant Results**: Get predictions and recommendations
    4. **Standards Check**: Automatic comparison with Codex and EU regulations
    
    ### Key Benefits
    - **Faster Decisions**: Reduce time for compliance checks
    - **Cost Savings**: Minimize rejected batches
    - **Quality Assurance**: Maintain export standards
    - **Data-Driven**: Backed by historical compliance data
    """)
    st.image("https://via.placeholder.com/800x400?text=Agricultural+Quality+Control")

with tab_regulator:
    st.header("📊 Regulator Dashboard")
    st.markdown("Overview of historical compliance data and trends for regulatory monitoring.")
    
    colA, colB = st.columns(2)
    
    with colA:
        st.subheader("Compliance Rate")
        # Pie chart of compliance
        fig1 = px.pie(history_df, names='compliant', title="", 
                      color_discrete_sequence=["#ef553b", "#00cc96"], labels={'compliant':'Status'})
        # Rename 0 and 1 for the chart
        fig1.for_each_trace(lambda t: t.update(labels=['Non-Compliant' if label == 0 else 'Compliant' for label in t.labels]))
        st.plotly_chart(fig1)

    with colB:
        st.subheader("Moisture vs Aflatoxin Levels")
        # Scatter plot of Moisture vs Aflatoxin
        fig2 = px.scatter(history_df, x="moisture_content", y="aflatoxin_b1", color="compliant",
                          title="",
                          labels={"moisture_content": "Moisture (%)", "aflatoxin_b1": "Aflatoxin (µg/kg)", "compliant": "Compliance Status"})
        st.plotly_chart(fig2)
    
    # Additional stats
    st.write("---")
    st.subheader("Key Statistics")
    total_batches = len(history_df)
    compliant_batches = history_df['compliant'].sum()
    compliance_rate = (compliant_batches / total_batches) * 100
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Total Batches", total_batches)
    with col2:
        st.metric("Compliant Batches", int(compliant_batches))
    with col3:
        st.metric("Compliance Rate", f"{compliance_rate:.1f}%")

with tab_policy:
    st.title("📋 Policy & Terms")
    st.markdown("""
    ### Terms of Use
    By using AgricQual, you agree to the following terms:
    
    1. **Purpose**: This tool is for informational purposes only and does not constitute legal advice.
    2. **Accuracy**: While we strive for accuracy, predictions are based on historical data and machine learning models.
    3. **Liability**: Users are responsible for final compliance decisions.
    4. **Data Usage**: Input data is processed locally and not stored permanently.
    
    ### Compliance Standards
    The system checks against:
    - **Codex Alimentarius** standards for aflatoxin levels
    - **EU Regulations** for pesticide residues
    - **General food safety** guidelines for moisture, microbial load, and heavy metals
    
    ### Contact
    For questions or support, please contact the development team.
    """)

with tab_privacy:
    st.title("🔒 Data Protection & Privacy")
    st.markdown("""
    ### Privacy Policy
    AgricQual is committed to protecting your privacy and data security.
    
    #### Data Collection
    - **Input Data**: Quality parameters entered by users are processed in real-time for compliance assessment.
    - **No Storage**: Input data is not stored on servers; calculations happen locally in your browser.
    - **Model Data**: The trained model contains aggregated historical data, not individual user inputs.
    
    #### Data Usage
    - Data is used solely for generating compliance predictions.
    - No personal information is collected or required.
    - Historical data is anonymized and used for model training only.
    
    #### Security Measures
    - All processing occurs client-side where possible.
    - Models are trained on secure, anonymized datasets.
    - No data transmission to external servers for core functionality.
    
    #### Your Rights
    - You control all input data.
    - No tracking or analytics beyond basic app functionality.
    - Data is not shared with third parties.
    
    If you have concerns about data privacy, please review our full privacy policy or contact us.
    """)
