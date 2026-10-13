
class BatterySOHEstimator:
    def __init__(self, rated_capacity, current_capacity,
                 battery_voltage, temperature):
        self.rated_capacity = rated_capacity
        self.current_capacity = current_capacity
        self.battery_voltage = battery_voltage
        self.temperature = temperature

    def calculate_soh(self):
        if self.rated_capacity <= 0:
            return None

        soh = (self.current_capacity / self.rated_capacity) * 100
        return soh

    def estimate_condition(self, soh):
        if soh is None:
            return "INVALID CAPACITY"

        if soh >= 80:
            return "GOOD"
        elif soh >= 60:
            return "MODERATE"
        else:
            return "POOR - BATTERY REPLACEMENT CHECK"

    def display_result(self):
        soh = self.calculate_soh()
        condition = self.estimate_condition(soh)

        print("\n----- Battery SOH Estimator -----")
        print(f"Rated Capacity   : {self.rated_capacity:.2f} Ah")
        print(f"Current Capacity : {self.current_capacity:.2f} Ah")
        print(f"Battery Voltage  : {self.battery_voltage:.2f} V")
        print(f"Temperature      : {self.temperature:.2f} °C")

        if soh is not None:
            print(f"Battery SOH      : {soh:.2f}%")

        print(f"Battery Condition: {condition}")

        if soh is not None and self.current_capacity > self.rated_capacity:
            print("Note: Check capacity measurements and input values.")

        if self.temperature > 45:
            print("Warning: Battery temperature is high.")
        elif self.temperature < 0:
            print("Warning: Battery temperature is below freezing.")


# Example input values
rated_capacity = 100       # Ah
current_capacity = 85      # Ah
battery_voltage = 48       # V
temperature = 30            # °C

estimator = BatterySOHEstimator(
    rated_capacity,
    current_capacity,
    battery_voltage,
    temperature
)

estimator.display_result()
