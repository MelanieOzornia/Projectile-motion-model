# projectile motion model

import math
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
# Constants 
ay = g = 9.81  # acceleration due to gravity (m/s^2)
dt = 0.01  # time step for calculations (s)

# User Inputs
launchSpeed = float(input("Enter the launch speed (m/s): "))
launchAngle = float(input("Enter the launch angle (degrees): "))
staringPosition = input("Does the projectile start form the origin? (yes/no): ")

# giving the user the option to specify the final vertical position out of the range of the projectile
maxHeight = (launchSpeed ** 2) * (math.sin(math.radians(launchAngle)) ** 2) / (2 * g)
print(f"The maximum height of the projectile is: {maxHeight:.2f} meters.")
while True:
    yEnd = float(input("Enter the final vertical position (m): "))
    if 0 <= yEnd <= maxHeight:
        break
    else:
        print(f"Please enter a value between 0 and {maxHeight:.2f} meters.")

if staringPosition.lower() == "yes":
    xi = 0
    yi = 0
else:
    xi = float(input("Enter the initial horizontal position (m): "))
    yi = float(input("Enter the initial vertical position (m): "))

# inital velocity components
vxi = launchSpeed * math.cos(math.radians(launchAngle))
vyi = launchSpeed * math.sin(math.radians(launchAngle))

# lists to store the results of the calculations
data = { "x": [xi], "y": [yi], "t": [0.0], "vx": [vxi], "vy": [vyi] }

# Calculations
disc = vyi ** 2 + 2 * g * (yi - yEnd)
if disc < 0:
    print("The projectile never reaches that height.")
    raise SystemExit
totalTime = (vyi + math.sqrt(disc)) / g

def record(time):
    data["t"].append(time)
    data["x"].append(xi + vxi * time)
    data["y"].append(yi + vyi * time - 0.5 * g * time ** 2)
    data["vx"].append(vxi)
    data["vy"].append(vyi - g * time)   
    
n = int(totalTime / dt)  # number of time steps
for i in range(1, n + 1):
    record(i * dt)
    
if data["t"][-1] < totalTime:
    record(totalTime)

vxf = data["vx"][-1]  # final horizontal velocity (m/s)
vyf = data["vy"][-1]  # final vertical velocity (m/s)
vf = math.sqrt(vxf ** 2 + vyf ** 2)  # final velocity magnitude (m/s)
horizontalRange = data["x"][-1]  # horizontal range (m)
maxHeight = max(data["y"])   # maximum height (m)

# asks the user for a specific time to see the results for

whatTime = float(input("what time would you like to see the results for? (in seconds): "))
i = round(whatTime / dt)
if 0 <= i < len(data["t"]):
    print(f"At time {data['t'][i]:.2f} seconds:")
    print(f"Horizontal Position: {data['x'][i]:.2f} m, Vertical Position: {data['y'][i]:.2f} m")
else:
    print("Time is out of range. Please enter a time between 0 and {:.2f} seconds.".format(totalTime))

# summary printout

print("\nProjectile Motion Summary:")
print(f"Time of Flight: {totalTime:.2f} seconds")
print(f"Maximum Height: {maxHeight:.2f} meters")
print(f"Horizontal Range: {horizontalRange:.2f} meters")
print(f"Final Velocity: {vf:.2f} m/s at an angle of {math.degrees(math.atan2(vyf, vxf)):.2f} degrees")

# Plotting the trajectory

df = pd.DataFrame(data)
plt.style.use('dark_background')
sns.scatterplot(data=df, x="x", y="y", palette="viridis")
plt.title("Projectile Motion Trajectory")
plt.xlabel("Horizontal Position (m)")
plt.ylabel("Vertical Position (m)")
plt.xlim(0, horizontalRange * 1.1)
plt.ylim(0, maxHeight * 1.1)
plt.show()
