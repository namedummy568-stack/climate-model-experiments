
def calculate_radiative_forcing(temperature, co2_concentration):
    """
    Calculates the radiative forcing based on temperature and CO2 concentration.

    Args:
        temperature (float): Global average temperature in Celsius.
        co2_concentration (float): CO2 concentration in parts per million (ppm).

    Returns:
        float: Radiative forcing in Watts per square meter (W/m^2).
    """
    # This is a simplified model for demonstration purposes.
    # A more complex model would involve atmospheric physics and radiative transfer equations.

    # Base radiative forcing (e.g., from pre-industrial levels)
    base_forcing = 1.5  # W/m^2

    # Temperature sensitivity (example: 0.1 W/m^2 per degree Celsius above a baseline)
    temp_sensitivity = 0.1
    baseline_temp = 15.0 # degrees Celsius

    # CO2 sensitivity (example: logarithmic relationship)
    # A common approximation for CO2 radiative forcing is 5.35 * ln(C/C0)
    co2_sensitivity_factor = 5.35
    pre_industrial_co2 = 280 # ppm

    # Calculate forcing components
    temp_forcing = temp_sensitivity * (temperature - baseline_temp)
    co2_forcing = co2_sensitivity_factor * (co2_concentration / pre_industrial_co2)

    # Total radiative forcing
    total_forcing = base_forcing + temp_forcing + co2_forcing
    return total_forcing

if __name__ == "__main__":
    # Example usage
    current_temp = 15.8
    current_co2 = 420

    forcing = calculate_radiative_forcing(current_temp, current_co2)
    print(f"Current Temperature: {current_temp}°C")
    print(f"Current CO2 Concentration: {current_co2} ppm")
    print(f"Calculated Radiative Forcing: {forcing:.2f} W/m^2")

    # Experiment with different parameters
    future_temp = 17.0
    future_co2 = 550
    future_forcing = calculate_radiative_forcing(future_temp, future_co2)
    print(f"\nFuture Temperature: {future_temp}°C")
    print(f"Future CO2 Concentration: {future_co2} ppm")
    print(f"Calculated Future Radiative Forcing: {future_forcing:.2f} W/m^2")

    # Save output to a file
    with open("model_output.txt", "w") as f:
        f.write(f"Current Temperature: {current_temp}°C\n")
        f.write(f"Current CO2 Concentration: {current_co2} ppm\n")
        f.write(f"Calculated Radiative Forcing: {forcing:.2f} W/m^2\n")
        f.write(f"\nFuture Temperature: {future_temp}°C\n")
        f.write(f"Future CO2 Concentration: {future_co2} ppm\n")
        f.write(f"Calculated Future Radiative Forcing: {future_forcing:.2f} W/m^2\n")
