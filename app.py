import streamlit as st
import pandas as pd
import joblib
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import OneHotEncoder

# Load the model and scaler
@st.cache_resource
def load_model():
    try:
        model = joblib.load('best_model.pkl')
        scaler = joblib.load('scaler.pkl')
        return model, scaler
    except FileNotFoundError:
        st.error("Model or scaler file not found. Please ensure 'best_model.pkl' and 'scaler.pkl' exist.")
        return None, None

# Load model and scaler
model, scaler = load_model()

# Define feature input function
def get_user_input():
    st.sidebar.header("User  Input Features")
    gender = st.sidebar.selectbox("Gender", ["Male", "Female", "Other"])
    age = st.sidebar.number_input("Age", min_value=1, max_value=100, value=40, help="Enter your age.")
    hypertension = st.sidebar.selectbox("Hypertension", ["No", "Yes"], help="Have you ever been diagnosed with hypertension?")
    heart_disease = st.sidebar.selectbox("Heart Disease", ["No", "Yes"], help="Have you ever been diagnosed with heart disease?")
    ever_married = st.sidebar.selectbox("Ever Married", ["No", "Yes"], help="Have you ever been married?")
    work_type = st.sidebar.selectbox("Work Type", ["Private", "Self-employed", "Govt-job", "Children", "Never_worked"], help="What is your type of work?")
    residence_type = st.sidebar.selectbox("Residence Type", ["Urban", "Rural"], help="Where do you live?")
    avg_glucose_level = st.sidebar.number_input("Average Glucose Level", min_value=50.0, max_value=300.0, value=100.0, help="Enter your average glucose level.")
    bmi = st.sidebar.number_input("BMI", min_value=10.0, max_value=50.0, value=25.0, help="Enter your Body Mass Index (BMI).")
    smoking_status = st.sidebar.selectbox("Smoking Status", ["Never smoked", "Formerly smoked", "Smokes", "Unknown"], help="What is your smoking status?")

    user_data = {
        'gender': gender,
        'age': age,
        'hypertension': hypertension,
        'heart_disease': heart_disease,
        'ever_married': ever_married,
        'work_type': work_type,
        'Residence_type': residence_type,
        'avg_glucose_level': avg_glucose_level,
        'bmi': bmi,
        'smoking_status': smoking_status
    }
    
    return pd.DataFrame([user_data])

# Streamlit UI
st.set_page_config(page_title="Stroke Prediction System", layout="wide")
st.title("Stroke Prediction System")
st.markdown("### Enter the following details to predict stroke risk.")

if model is None:
    st.error("Model file not found. Please ensure 'best_model.pkl' and 'scaler.pkl' exist.")
else:
    user_input = get_user_input()
    
    # One-hot encode categorical features
    categorical_features = ['gender', 'hypertension', 'heart_disease', 'ever_married', 'work_type', 'Residence_type', 'smoking_status']
    user_input_encoded = pd.get_dummies(user_input, columns=categorical_features)

    # Ensure the columns match the model's expected input
    expected_columns = model.feature_names_in_  # Get the columns used during training
    user_input_encoded = user_input_encoded.reindex(columns=expected_columns, fill_value=0)

    # Scale the numeric features
    numeric_features = ['age', 'avg_glucose_level', 'bmi']
    user_input_encoded[numeric_features] = scaler.transform(user_input_encoded[numeric_features])
    
    if st.button("Predict Stroke Risk"):
        prediction = model.predict(user_input_encoded)
        probability = model.predict_proba(user_input_encoded)[:, 1][0]
        
        if prediction[0] == 1:
            st.error(f"High risk of stroke! (Probability: {probability:.2f})")
        else:
            st.success(f"Low risk of stroke. (Probability: {probability:.2f})")

# Add a footer with contact information
st.markdown("---")
st.markdown("© 2025 Stroke Prediction System. For suggestions, contact [susmagar012@gmail.com](mailto:susmagar012@gmail.com)")

# Custom CSS for better styling
st.markdown(
    """
    <style>
    .stButton>button {
        background-color: #4CAF50; /* Green */
        color: white;
        border: none;
        padding: 10px 20px;
        text-align: center;
        text-decoration: none;
        display: inline-block;
        font-size: 16px;
        margin: 4px 2px;
        cursor: pointer;
        border-radius: 5px;
    }
    </style>
    """,
    unsafe_allow_html=True
)