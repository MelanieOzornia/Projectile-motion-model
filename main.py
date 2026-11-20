# projectile motion model

import math
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import seaborn as sns
# Constants 
g = 9.81  # acceleration due to gravity (m/s^2)
dt = 0.01  # time step for calculations (s)

# User Inputs
launchSpeed = float(input("Enter the launch speed (m/s): "))
launchAngle = float(input("Enter the launch angle (degrees): "))
startingPosition = input("Does the projectile start from the origin? (yes/no): ")

# optional initial position input
if startingPosition.lower() == "yes":
    xi = 0
    yi = 0
else:
    xi = float(input("Enter the initial horizontal position (m): "))
    yi = float(input("Enter the initial vertical position (m): "))
    
 # drag constant input   
while True:                                   
    dragK = float(input("Enter drag constant k (1/m), 0 for none (typical 0.001-0.05): "))
    if dragK >= 0:
        break                                 
    print("k can't be negative.")         
    print("Please enter a valid value.")
    
# inital velocity components (moved up from below)
vxi = launchSpeed * math.cos(math.radians(launchAngle))
vyi = launchSpeed * math.sin(math.radians(launchAngle))

# practice run: simulate until it starts falling to find the real max height with drag
pvx, pvy, py = vxi, vyi, yi
maxHeight = yi
while pvy > 0:
    speed = math.sqrt(pvx**2 + pvy**2)
    pvx += -dragK * speed * pvx * dt
    pvy += (-g - dragK * speed * pvy) * dt
    py += pvy * dt
    maxHeight = max(maxHeight, py)
while True: # giving the user the option to specify the final vertical position out of the range of the projectile
    yEnd = float(input("Enter the final vertical position (m): "))
    if 0 <= yEnd <= maxHeight:
        break
    else:
        print(f"Please enter a value between 0 and {maxHeight:.2f} meters.")

# inital velocity components
vxi = launchSpeed * math.cos(math.radians(launchAngle))
vyi = launchSpeed * math.sin(math.radians(launchAngle))

x=xi
y=yi
vx=vxi
vy=vyi
time=0.0

# lists to store the results of the calculations
data = { "x": [xi], "y": [yi], "t": [0.0], "vx": [vxi], "vy": [vyi] }

# Calculations
while True:
    speed = math.sqrt(vx**2 + vy**2)
    accelx = -dragK * speed * vx
    accely = -g - dragK * speed * vy
    vx += accelx * dt
    vy += accely * dt
    x += vx * dt
    y += vy * dt
    time += dt
    data["x"].append(x)
    data["y"].append(y)
    data["t"].append(time)
    data["vx"].append(vx)
    data["vy"].append(vy)
    if vy < 0 and y <= yEnd:
        break


totalTime = data["t"][-1]  # total time of flight (s)


vxf = data["vx"][-1]  # final horizontal velocity (m/s)
vyf = data["vy"][-1]  # final vertical velocity (m/s)
vf = math.sqrt(vxf ** 2 + vyf ** 2)  # final velocity magnitude (m/s)
horizontalRange = data["x"][-1]  # horizontal range (m)
maxHeight = max(data["y"])   # maximum height (m)

# asks the user for a specific time to see the results for

whatTime = float(input("what time would you like to see the results for? (in seconds): "))
lookUp = round(whatTime / dt)
if 0 <= lookUp < len(data["t"]):
    print(f"At time {data['t'][lookUp]:.2f} seconds:")
    print(f"Horizontal Position: {data['x'][lookUp]:.2f} m, Vertical Position: {data['y'][lookUp]:.2f} m")
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
fig, ax = plt.subplots()

sns.scatterplot(data=df, x="x", y="y", hue="t", palette="viridis")
plt.title("Projectile Motion Trajectory")
plt.xlabel("Horizontal Position (m)")
plt.ylabel("Vertical Position (m)")
plt.xlim(0, horizontalRange * 1.1)
plt.ylim(0, maxHeight * 1.1)

projectile, = ax.plot([], [],'o', color='white', markersize=8)
def update(frame):
    projectile.set_data([df["x"].iloc[frame]], [df["y"].iloc[frame]])
    return projectile,

step = 2
ani = FuncAnimation(fig=fig, func=update, frames=len(data["t"]), interval=dt*1000*step, blit=True)
plt.show()
