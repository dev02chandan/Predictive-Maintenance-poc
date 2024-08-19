def check_maintenance(temperature, pressure, vibration, level):
    """Check if maintenance is due based on sensor thresholds."""
    # Define maintenance thresholds
    temp_threshold = 80
    pressure_threshold = 150
    vibration_threshold = 7
    level_threshold = 75

    # Check conditions
    if (temperature > temp_threshold or
        pressure > pressure_threshold or
        vibration > vibration_threshold or
        level > level_threshold):
        return True
    else:
        return False
