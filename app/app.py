import streamlit as st
import pandas as pd
import joblib
from sklearn.preprocessing import StandardScaler

# Load the trained model and scaler
model = joblib.load('app/model.pkl')
scaler = joblib.load('app/scaler.pkl')

# Load and display the logo
st.image('images/logo.png', use_column_width=True)

# Streamlit app layout
st.title('Predictive Maintenance Multi-Label Classification')

# Sliders for adjusting sensor values
air_temp = st.slider('Air Temperature [K]', min_value=290, max_value=310, value=298)
process_temp = st.slider('Process Temperature [K]', min_value=290, max_value=310, value=308)
rotational_speed = st.slider('Rotational Speed [rpm]', min_value=1000, max_value=3000, value=1500)
torque = st.slider('Torque [Nm]', min_value=0, max_value=80, value=40)
tool_wear = st.slider('Tool Wear [min]', min_value=0, max_value=500, value=100)

# Create a DataFrame from user inputs
input_data = pd.DataFrame({
    'Air temperature [K]': [air_temp],
    'Process temperature [K]': [process_temp],
    'Rotational speed [rpm]': [rotational_speed],
    'Torque [Nm]': [torque],
    'Tool wear [min]': [tool_wear]
})

# Standardize the input data using the saved scaler
input_data_scaled = scaler.transform(input_data)

# Predict the multi-label outcomes
predictions = model.predict(input_data_scaled)

# Mapping labels to their corresponding failure types
failure_types = [
    "Heat Dissipation Failure", "Power Failure", 
    "Overstrain Failure", "Tool Wear Failure", 
    "Random Failures"
]

# Display the predictions
st.subheader("Predicted Failures")
for i, failure in enumerate(failure_types):
    if predictions[0][i] == 1:
        st.error(f"Predicted {failure}!")
    else:
        st.success(f"No {failure} detected.")
