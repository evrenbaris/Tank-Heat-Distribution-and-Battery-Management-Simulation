import numpy as np
import matplotlib.pyplot as plt

# Time parameters
time = np.linspace(0, 10, 1000)  # 10 seconds, 1000 steps

# Heat sources (motor, electronics, environment)
motor_power = 200  # Motor power (Watt)
electronics_power = 50  # Electronics system power (Watt)
environment_temp = 30 + 5 * np.sin(2 * np.pi * 0.1 * time)  # Ambient temperature (Celsius)

# Heat generation (in Watts)
motor_heat = np.ones_like(time) * motor_power * 0.8  # 80% of motor power converted to heat
electronics_heat = np.ones_like(time) * electronics_power  # Constant heat from electronics
environment_heat = 10 * (environment_temp - 25)  # Environmental heat impact

# Total heat
total_heat = motor_heat + electronics_heat + environment_heat

# Battery consumption
battery_capacity = 5000  # Battery capacity in mAh
battery_consumption = (motor_power + electronics_power) / 12  # Current consumption in Amperes
battery_level = battery_capacity - np.cumsum(
    np.ones_like(time) * battery_consumption * (time[1] - time[0])
)  # Battery level calculation

# Plot: Heat Distribution
plt.figure(figsize=(12, 6))
plt.plot(time, motor_heat, label="Motor Heat (W)", color="red")
plt.plot(time, electronics_heat, label="Electronics Heat (W)", color="blue")
plt.plot(time, environment_heat, label="Environment Heat (W)", color="green")
plt.plot(time, total_heat, label="Total Heat (W)", linestyle="--", color="purple")
plt.title("Heat Distribution Over Time")
plt.xlabel("Time (s)")
plt.ylabel("Heat (W)")
plt.legend()
plt.grid()
plt.show()

# Plot: Battery Level
plt.figure(figsize=(12, 6))
plt.plot(time, battery_level, label="Battery Level (mAh)", color="orange")
plt.title("Battery Level Over Time")
plt.xlabel("Time (s)")
plt.ylabel("Battery Level (mAh)")
plt.legend()
plt.grid()
plt.show()
