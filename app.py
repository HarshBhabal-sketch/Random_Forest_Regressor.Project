import streamlit as st
import pickle
import numpy as np

# Load the trained model
with open(r"C:\Users\Harsh\Random_Forest_Regressor.pkl",'rb') as file:
    model = pickle.load(file)

# Page settings
st.set_page_config(
    page_title="Salary Prediction",
    page_icon="💰",
    layout="centered"
)

# Title
st.title("💰 Annual Salary Prediction")
st.write("Random Forest Regression Model")

st.markdown("---")

# Input 1
age = st.number_input(
    "Age",
    min_value=18,
    max_value=70,
    value=30
)

# Input 2
experience = st.number_input(
    "Experience (Years)",
    min_value=0,
    max_value=50,
    value=2
)

# Input 3
education = st.number_input(
    "Education (Years)",
    min_value=0,
    max_value=30,
    value=15
)

# Input 4
hours_per_week = st.number_input(
    "Hours Per Week",
    min_value=1,
    max_value=100,
    value=40
)

# Input 5
projects = st.number_input(
    "Projects Completed",
    min_value=0,
    max_value=100,
    value=5
)

# Input 6
certifications = st.number_input(
    "Certifications",
    min_value=0,
    max_value=50,
    value=2
)

# Input 7
performance = st.number_input(
    "Performance Score",
    min_value=0.0,
    max_value=100.0,
    value=90.0
)

st.markdown("---")

# Prediction button
if st.button("🔮 Predict Salary"):

    # Create input data
    input_data = np.array([[
        age,
        experience,
        education,
        hours_per_week,
        projects,
        certifications,
        performance
    ]])

    # Make prediction
    prediction = model.predict(input_data)

    # Display result
    st.success(
        f"Predicted Annual Salary: {prediction[0]:.2f} LPA"
    )