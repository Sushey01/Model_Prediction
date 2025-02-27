import streamlit as st
import pickle
import pandas as pd

# Load the trained model
def load_model():
    with open("best_model.pkl", "rb") as file:  # Ensure your trained model is named correctly
        model = pickle.load(file)
    return model

model = load_model()

# Streamlit UI
st.title("Stroke Prediction App 🚑")

st.write("Enter patient details below to predict stroke risk.")

# User input fields
age = st.number_input("Age", min_value=0, max_value=120, value=50)
hypertension = st.selectbox("Hypertension", [0, 1])
heart_disease = st.selectbox("Heart Disease", [0, 1])
avg_glucose_level = st.number_input("Average Glucose Level", value=100.0)
bmi = st.number_input("BMI", value=25.0)

# Convert input into DataFrame
input_data = pd.DataFrame([[age, hypertension, heart_disease, avg_glucose_level, bmi]],
                          columns=["age", "hypertension", "heart_disease", "avg_glucose_level", "bmi"])

if st.button("Predict"):
    prediction = model.predict(input_data)
    if prediction[0] == 1:
        st.error("⚠️ High risk of stroke! Consult a doctor.")
    else:
        st.success("✅ Low risk of stroke.")

