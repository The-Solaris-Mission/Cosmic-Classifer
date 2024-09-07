import streamlit as st
import pandas as pd
import numpy as np
import pickle
from sklearn.preprocessing import StandardScaler
import base64

# Function to load and encode the image in base64 format
def load_background_image(image_file_path):
    with open(image_file_path, "rb") as img_file:
        b64_image = base64.b64encode(img_file.read()).decode()
    return b64_image

# Load the image and convert it to base64
image_file_path = "image.png"  # Ensure this is the correct path to your image file
encoded_image = load_background_image(image_file_path)

# Inject custom CSS to set the background and the translucent card
page_bg_img = f"""
<style>
[data-testid="stAppViewContainer"] {{
    background-image: url("data:image/png;base64,{encoded_image}");
    background-size: cover;
    background-position: center;
    background-attachment: fixed;
}}

[data-testid="stHeader"] {{
    background-color: rgba(0,0,0,0);  /* Transparent header */
}}

/* Translucent card around the stVerticalBlock */
[data-testid="stVerticalBlock"] {{
    background-color: rgba(0, 0, 0, 0.7);  /* Black with 70% opacity */
    border-radius: 15px;  /* Rounded corners */
    padding: 20px;  /* Padding inside the card */
    box-shadow: 0px 4px 12px rgba(0, 0, 0, 0.5);  /* Stronger shadow */
    margin: 20px;  /* Add some space around the card */
    width: 108%;  /* Set a wider width */
    max-width: 1200px;  /* Limit the maximum width */
    margin-left: auto;
    margin-right: auto;  /* Center the card */
}}
</style>
"""

st.markdown(page_bg_img, unsafe_allow_html=True)

# Title and description
st.title('Cosmic Classifier')
st.write("Exoplanet Confirmation Prediction: This app predicts whether an exoplanet is confirmed, a candidate, or a false positive based on the features provided.")

# Function to load the trained model
def load_model():
    with open('model/stacking_model.pkl', 'rb') as file:
        model = pickle.load(file)
    return model

# Function to load the fitted scaler
def load_scaler():
    with open('model/scaler.pkl', 'rb') as file:
        scaler = pickle.load(file)
    return scaler

# Load the model and scaler
stacking_model = load_model()
scaler = load_scaler()

# Initialize session state for input fields
if 'reset' not in st.session_state:
    st.session_state['reset'] = False

def reset_inputs():
    st.session_state['reset'] = True

def set_default_values():
    st.session_state['reset'] = False

# Reset button logic
if st.button("Reset"):
    reset_inputs()

# Input fields for user to enter the data with clear descriptions
st.header("Input Features")

# If reset is clicked, default values are loaded
if st.session_state['reset']:
    koi_period = st.number_input('Orbital Period of the Exoplanet (koi_period in days):', key='koi_period_key', value=0.0, help="The time taken for the planet to complete one orbit around its star.")
    koi_duration = st.number_input('Transit Duration (koi_duration in hours):', key='koi_duration_key', value=0.0, help="Duration of the planet's transit across the star (hours).")
    koi_depth = st.number_input('Transit Depth (koi_depth in ppm):', key='koi_depth_key', value=0.0, help="The depth of the transit as a percentage of the star's brightness.")
    koi_impact = st.number_input('Impact Parameter (koi_impact):', key='koi_impact_key', value=0.0, help="Measure of how central the planet's transit is across the star (0 = central).")
    koi_prad = st.number_input('Planet Radius (koi_prad in Earth radii):', key='koi_prad_key', value=0.0, help="The radius of the planet in Earth radii.")
    koi_model_snr = st.number_input('Signal-to-Noise Ratio (koi_model_snr):', key='koi_model_snr_key', value=0.0, help="The ratio of the transit signal to the noise in the data.")
    koi_steff = st.number_input('Stellar Effective Temperature (koi_steff in Kelvin):', key='koi_steff_key', value=0.0, help="The effective temperature of the star in Kelvin.")
    koi_slogg = st.number_input('Stellar Surface Gravity (koi_slogg in cgs):', key='koi_slogg_key', value=0.0, help="The logarithm of the star's surface gravity (cgs units).")
    koi_srad = st.number_input('Stellar Radius (koi_srad in solar radii):', key='koi_srad_key', value=0.0, help="The radius of the star in solar radii.")
    koi_kepmag = st.number_input('Kepler Magnitude (koi_kepmag):', key='koi_kepmag_key', value=0.0, help="The brightness of the star as seen by the Kepler telescope.")
    set_default_values()  # Reset the flag after setting default values
else:
    koi_period = st.number_input('Orbital Period of the Exoplanet (koi_period in days):', key='koi_period_key', help="The time taken for the planet to complete one orbit around its star.")
    koi_duration = st.number_input('Transit Duration (koi_duration in hours):', key='koi_duration_key', help="Duration of the planet's transit across the star (hours).")
    koi_depth = st.number_input('Transit Depth (koi_depth in ppm):', key='koi_depth_key', help="The depth of the transit as a percentage of the star's brightness.")
    koi_impact = st.number_input('Impact Parameter (koi_impact):', key='koi_impact_key', help="Measure of how central the planet's transit is across the star (0 = central).")
    koi_prad = st.number_input('Planet Radius (koi_prad in Earth radii):', key='koi_prad_key', help="The radius of the planet in Earth radii.")
    koi_model_snr = st.number_input('Signal-to-Noise Ratio (koi_model_snr):', key='koi_model_snr_key', help="The ratio of the transit signal to the noise in the data.")
    koi_steff = st.number_input('Stellar Effective Temperature (koi_steff in Kelvin):', key='koi_steff_key', help="The effective temperature of the star in Kelvin.")
    koi_slogg = st.number_input('Stellar Surface Gravity (koi_slogg in cgs):', key='koi_slogg_key', help="The logarithm of the star's surface gravity (cgs units).")
    koi_srad = st.number_input('Stellar Radius (koi_srad in solar radii):', key='koi_srad_key', help="The radius of the star in solar radii.")
    koi_kepmag = st.number_input('Kepler Magnitude (koi_kepmag):', key='koi_kepmag_key', help="The brightness of the star as seen by the Kepler telescope.")

# Create a DataFrame from the input features
input_data = pd.DataFrame({
    'koi_period': [koi_period],
    'koi_duration': [koi_duration],
    'koi_depth': [koi_depth],
    'koi_impact': [koi_impact],
    'koi_prad': [koi_prad],
    'koi_model_snr': [koi_model_snr],
    'koi_steff': [koi_steff],
    'koi_slogg': [koi_slogg],
    'koi_srad': [koi_srad],
    'koi_kepmag': [koi_kepmag]
})

# Ensure that all required inputs are provided
if st.button('Predict'):
    if input_data.isnull().values.any():
        st.write("Please enter all the required fields.")
    else:
        # Scale the input features
        input_scaled = scaler.transform(input_data)

        # Make prediction
        prediction = stacking_model.predict(input_scaled)
        confidence = stacking_model.predict_proba(input_scaled)

        # Display the prediction
        if prediction == 0:
            st.write("Prediction: **False Positive**")
        elif prediction == 1:
            st.write("Prediction: **Candidate**")
        else:
            st.write("Prediction: **Confirmed**")
        
        # Display the prediction confidence
        st.write(f"Prediction Confidence: {np.max(confidence)*100:.2f}%")
