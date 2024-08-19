import pandas as pd
import numpy as np

# Define the number of records
num_records = 100

# Generate random data for sensors
data = {
    'Temperature': np.random.uniform(60, 100, num_records),  # Temperature in Celsius
    'Pressure': np.random.uniform(100, 200, num_records),  # Pressure in kPa
    'Vibration': np.random.uniform(0, 10, num_records),  # Vibration in mm/s
    'Level': np.random.uniform(50, 100, num_records)  # Level in percentage
}

# Create a DataFrame
df = pd.DataFrame(data)

# Save to CSV
df.to_csv('data/dummy_data.csv', index=False)
