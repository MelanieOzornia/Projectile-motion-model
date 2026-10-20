# projectile motion model

import math

# Constants 
ay = g = 9.81  # acceleration due to gravity (m/s^2)
ax = 0  # horizontal acceleration (m/s^2) (assuming no air resistance)
dt = 0.01  # time step for calculations (s)

# User Inputs
launchSpeed = float(input("Enter the launch speed (m/s): "))
launchAngle = float(input("Enter the launch angle (degrees): "))
staringPosition = input("Does the projectile start form the origin? (yes/no): ")
yEnd = float(input("Enter the final vertical position (m): "))

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
x = [xi]  # horizontal position (m)
y = [yi]  # vertical position (m)
t = [0.0]  # time (s)
vx = [vxi]  # horizontal velocity (m/s)
vy = [vyi]  # vertical velocity (m/s)

# Calculations
totalTime = (2 * launchSpeed * math.sin(math.radians(launchAngle))) / g  # total time of flight (s)
horizontalRange = xi + vxi * totalTime  # horizontal range (m)
verticalDisplacement = yi + vyi * totalTime - 0.5 * g * totalTime ** 2  # vertical displacement (m)
maxHeight = (vyi ** 2) / (2 * g)  # maximum height (m)

def record(time):
    t.append(time)
    x.append(xi + vxi * time)
    y.append(yi + vyi * time - 0.5 * g * time ** 2)
    vx.append(vxi)
    vy.append(vyi - g * time)   
    
n = int(totalTime / dt)  # number of time steps
for i in range(1, n + 1):
    record(i * dt)
    
if t[-1] < totalTime:
    record(totalTime)

vxf = vx[-1]  # final horizontal velocity (m/s)
vyf = vy[-1]  # final vertical velocity (m/s)
vf = math.sqrt(vxf ** 2 + vyf ** 2)  # final velocity magnitude (m/s)

# summary 
# will include the following calculations:
# 1. Time of flight
# 2. Maximum height
# 3. Horizontal range
# 4. Final velocity
whatTime = float(input("what time would you like to see the results for? (in seconds): "))
print(f"\nResults at {whatTime:.2f} seconds:")
# calculate the horizontal and vertical positions at the specified time
x_at_time = xi + vxi * whatTime
y_at_time = yi + vyi * whatTime - 0.5 * g *whatTime ** 2
print(f"Horizontal Position: {x_at_time:.2f} m, Vertical Position: {y_at_time:.2f} m")
print("\nProjectile Motion Summary:")
print(f"Time of Flight: {totalTime:.2f} seconds")
print(f"Maximum Height: {maxHeight:.2f} meters")
print(f"Horizontal Range: {horizontalRange:.2f} meters")
print(f"Final Velocity: {vf:.2f} m/s at an angle of {math.degrees(math.atan2(vyf, vxf)):.2f} degrees")

