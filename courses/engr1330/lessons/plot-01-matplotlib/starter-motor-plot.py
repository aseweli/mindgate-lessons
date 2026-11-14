import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("motor_temps.csv")
plt.plot(df["Minute"], df["MotorA"], color="red", marker="o", label="Motor A")
# TODO: plot MotorB in blue with a dashed line and label "Motor B"
# TODO: x label "Time (minutes)", y label "Temperature (°C)", a title and a legend
plt.savefig("motors.png")
plt.show()

print("max A:", df["MotorA"].max())
print("max B:", df["MotorB"].max())
