import streamlit as st
import pickle
import numpy as np

# Load the model
with open(r"C:\Users\Harsh\Random_Forest_Regressor.pkl", "rb") as file:
    model = pickle.load(file)

# Page configuration
st.set_page_config(
    page_title="Random Forest Prediction",
    page_icon="🌳",
    layout="centered"
)

# Title
st.title("🌳 Random Forest Regressor")
st.write("Enter the values of the 7 features to get a prediction.")

# Input features
feature1 = st.number_input("Feature 1", value=0.0)
feature2 = st.number_input("Feature 2", value=0.0)
feature3 = st.number_input("Feature 3", value=0.0)
feature4 = st.number_input("Feature 4", value=0.0)
feature5 = st.number_input("Feature 5", value=0.0)
feature6 = st.number_input("Feature 6", value=0.0)
feature7 = st.number_input("Feature 7", value=0.0)

# Prediction
if st.button("Predict", type="primary"):

    # Prepare input
    input_data = np.array([[
        feature1,
        feature2,
        feature3,
        feature4,
        feature5,
        feature6,
        feature7
    ]])

    # Make prediction
    prediction = model.predict(input_data)

    # Display result
    st.success(f"Predicted Value: {prediction[0]:.2f}")