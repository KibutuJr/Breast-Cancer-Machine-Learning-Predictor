import streamlit as st
import pandas as pd
import joblib
import os

# Dynamically build model path relative to this script
script_dir = os.path.dirname(os.path.abspath(__file__))
model_path = os.path.join(script_dir, '..', 'models', 'random_forest_model.pkl')

# Load model with error handling
try:
    model = joblib.load(model_path)
except FileNotFoundError:
    st.error(f"Model file not found at {model_path}. Please check the path and file.")
    st.stop()

st.title("ML Model Predictor App")

st.markdown("""
This app allows you to input features and get predictions from the trained model.
""")

# Input fields matching training features
clump_thickness = st.slider("Clump Thickness", 1, 10, 5)
uniformity_of_cell_size = st.slider("Uniformity of Cell Size", 1, 10, 1)
uniformity_of_cell_shape = st.slider("Uniformity of Cell Shape", 1, 10, 1)
marginal_adhesion = st.slider("Marginal Adhesion", 1, 10, 1)
single_epithelial_cell_size = st.slider("Single Epithelial Cell Size", 1, 10, 2)
bare_nuclei = st.slider("Bare Nuclei", 1, 10, 1)
bland_chromatin = st.slider("Bland Chromatin", 1, 10, 3)
normal_nucleoli = st.slider("Normal Nucleoli", 1, 10, 1)
mitoses = st.slider("Mitoses", 1, 10, 1)

# Prepare input data for prediction
input_data = pd.DataFrame({
    "clump_thickness": [clump_thickness],
    "uniformity_of_cell_size": [uniformity_of_cell_size],
    "uniformity_of_cell_shape": [uniformity_of_cell_shape],
    "marginal_adhesion": [marginal_adhesion],
    "single_epithelial_cell_size": [single_epithelial_cell_size],
    "bare_nuclei": [bare_nuclei],
    "bland_chromatin": [bland_chromatin],
    "normal_nucleoli": [normal_nucleoli],
    "mitoses": [mitoses]
})

# Predict on button click
if st.button("Predict"):
    prediction = model.predict(input_data)
    st.success(f"Prediction: {prediction[0]}")
