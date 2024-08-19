import streamlit as st
from data_loader import load_data
from maintenance_logic import check_maintenance

# Load the dummy data
data = load_data('data/dummy_data.csv')

# Streamlit app layout
st.title('Predictive Maintenance PoC')

# Sliders for adjusting sensor values
temperature = st.slider('Temperature (Celsius)', min_value=60, max_value=100, value=70)
pressure = st.slider('Pressure (kPa)', min_value=100, max_value=200, value=120)
vibration = st.slider('Vibration (mm/s)', min_value=0, max_value=10, value=3)
level = st.slider('Level (%)', min_value=50, max_value=100, value=65)

# Check if maintenance is due
maintenance_due = check_maintenance(temperature, pressure, vibration, level)

# Display result
if maintenance_due:
    st.error('Maintenance is due! Please schedule maintenance.')
else:
    st.success('No maintenance needed. All systems are normal.')
