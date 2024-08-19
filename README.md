# Predictive Maintenance PoC

This project is a proof of concept for predictive maintenance in the manufacturing industry. It uses dummy data to simulate sensor readings and allows users to adjust sensor values to see if maintenance is due.

## How to Run

1. Install the dependencies:

```
   pip install -r requirements.txt
```

2. Run the Streamlit app:

```
   streamlit run app/app.py
```

## Features

- Simulates data for temperature, pressure, vibration, and level sensors.
- Allows users to adjust sensor values via sliders.
- Checks if maintenance is due based on predefined thresholds.

## Dummy Data

The dummy data is stored in `data/dummy_data.csv` and is generated using a script.
