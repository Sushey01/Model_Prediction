import streamlit as st
import pickle
import numpy as np

# Function to load the trained model
@st.cache_data
def load_model():
    try:
        with open("best_model.pkl", "rb") as file:
            model = pickle.load(file)
        return model
    except Exception as e:
        st.error(f"Error loading model: {str(e)}")
        return None

# Load the model
model = load_model()
if model is None:
    st.stop()  # Stop the app if the model fails to load

# Streamlit UI
st.title("🩺 Stroke Prediction App")
st.markdown("This app predicts the likelihood of a stroke based on user input.")

# User input fields
gender = st.selectbox("Gender", ["Male", "Female", "Other"])
age = st.slider("Age", 1, 100, 50)
hypertension = st.radio("Hypertension (High Blood Pressure)", [0, 1])
heart_disease = st.radio("Heart Disease", [0, 1])
avg_glucose_level = st.number_input("Average Glucose Level", min_value=50.0, max_value=300.0, value=100.0)
bmi = st.number_input("BMI", min_value=10.0, max_value=50.0, value=25.0)

# Convert categorical inputs
gender_map = {"Male": 0, "Female": 1, "Other": 2}
gender_encoded = gender_map[gender]

# Prepare input for model
input_data = np.array([[gender_encoded, age, hypertension, heart_disease, avg_glucose_level, bmi]])

# Prediction
if st.button("Predict"):
    prediction = model.predict(input_data)[0]  # Get prediction
    if prediction == 1:
        st.error("⚠️ High risk of stroke! Please consult a doctor.")
    else:
        st.success("✅ Low risk of stroke. Keep maintaining a healthy lifestyle!")

# Footer
st.markdown("**Developed by Shekhar Lamichhane Magar | Deployed with Streamlit**")
