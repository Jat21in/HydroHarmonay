def control_water_valve(nitrogen, phosphorous, potassium, temperature, humidity, ph):
    # Define threshold values
    nitrogen_threshold = 20
    phosphorous_threshold = 10
    potassium_threshold = 30
    temperature_threshold = 25
    humidity_threshold = 60
    ph_threshold = 7.0

    # Check if parameters are below the threshold values
    if (nitrogen < nitrogen_threshold and
        phosphorous < phosphorous_threshold and
        potassium < potassium_threshold and
        temperature < temperature_threshold and
        humidity < humidity_threshold and
        ph < ph_threshold):
        # Open the water valve
        print("Water valve opened.")
    else:
        # Keep the water valve closed
        print("Water valve closed.")

# Example usage:
nitrogen_value = float(input("Enter nitrogen value: "))
phosphorous_value = float(input("Enter phosphorous value: "))
potassium_value = float(input("Enter potassium value: "))
temperature_value = float(input("Enter temperature value: "))
humidity_value = float(input("Enter humidity value: "))
ph_value = float(input("Enter pH value: "))

control_water_valve(nitrogen_value, phosphorous_value, potassium_value, temperature_value, humidity_value, ph_value)




class IrrigationSystem:
    def __init__(self, nitrogen, phosphorus, potassium, temperature, ph, humidity):
        self.nitrogen = nitrogen
        self.phosphorus = phosphorus
        self.potassium = potassium
        self.temperature = temperature
        self.ph = ph
        self.humidity = humidity

    def calculate_water_needed(self):
        # Hypothetical model to calculate water needed based on environmental factors
        water_needed = (
            self.nitrogen * 0.2 +
            self.phosphorus * 0.3 +
            self.potassium * 0.2 +
            self.temperature * 0.1 +
            self.ph * 0.1 +
            self.humidity * 0.1
        )
        return water_needed

    def adjust_valve_open_time(self, water_needed):
        # Hypothetical model to adjust valve open time based on water needed
        valve_open_time = water_needed * 0.02  # Adjust as needed
        return valve_open_time

    def calculate_fertilizers_used(self, valve_open_time):
        # Hypothetical model to calculate the number of fertilizers used
        fertilizers_used = valve_open_time * 0.5  # Adjust as needed
        return fertilizers_used

    def irrigate(self):
        water_needed = self.calculate_water_needed()
        valve_open_time = self.adjust_valve_open_time(water_needed)
        fertilizers_used = self.calculate_fertilizers_used(valve_open_time)

        print(f"Water Needed: {water_needed} units")
        print(f"Valve Open Time: {valve_open_time} mins")
        print(f"Fertilizers Used: {fertilizers_used} units")


# Example usage:
nitrogen_level = 5
phosphorus_level = 3
potassium_level = 4
temperature_value = 30
ph_value = 6.5
humidity_value = 60

irrigation_system = IrrigationSystem(
    nitrogen_level, phosphorus_level, potassium_level, temperature_value, ph_value, humidity_value
)
irrigation_system.irrigate()
