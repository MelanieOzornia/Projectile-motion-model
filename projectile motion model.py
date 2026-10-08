# projectile motion model

import math

# Constants 
ay = g = 9.81  # acceleration due to gravity (m/s^2)
ax = 0  # horizontal acceleration (m/s^2) (assuming no air resistance)
dt = 0.01  # time step for calculations (s)

# lists to store the results of the calculations
x = {}  # horizontal position (m)
y = {}  # vertical position (m)
t= {}  # time (s)

# User Inputs
launchSpeed = float(input("Enter the launch speed (m/s): "))
O = launchAngle = float(input("Enter the launch angle (degrees): "))
xi = float(input("Enter the initial horizontal position (m): "))
yi = float(input("Enter the initial vertical position (m): "))

# inital velocity components
vxi = launchSpeed * math.cos(math.radians(launchAngle))
vyi = launchSpeed * math.sin(math.radians(launchAngle))

# Calculations
totalTime = (2 * launchSpeed * math.sin(math.radians(launchAngle))) / g  # total time of flight (s)
horizontalRange = xi + vxi * totalTime  # horizontal range (m)
verticalDisplacement = yi + vyi * totalTime - 0.5 * g * totalTime ** 2  # vertical displacement (m)
maxHeight = (vyi ** 2) / (2 * g)  # maximum height (m)

# Final velocity components
vxf = vxi  # final horizontal velocity (m/s)
vyf = vyi - (g * totalTime)  # final vertical velocity (m/s)

# final velocity magnitude
vf = math.sqrt(vxf ** 2 + vyf ** 2)  # final velocity magnitude (m/s)

def main():
    while y>= 0:
        # update time
        t[0] = 0
        t[0] += dt

        # update horizontal position
        x[0] = xi + vxi * t[0]

        # update vertical position
        y[0] = yi + vyi * t[0] - 0.5 * g * t[0] ** 2

        # print the results
        print(f"Time: {t[0]:.2f} s, Horizontal Position: {x[0]:.2f} m, Vertical Position: {y[0]:.2f} m")


# summary 
# will include the following calculations:
# 1. Time of flight
# 2. Maximum height
# 3. Horizontal range
# 4. Final velocity
whatTime = float(input("what time would you like to see the results for? (in seconds): "))
print("\nProjectile Motion Summary:")
print(f"Time of Flight: {totalTime:.2f} seconds")
print(f"Maximum Height: {maxHeight:.2f} meters")
print(f"Horizontal Range: {horizontalRange:.2f} meters")
print(f"Final Velocity: {vf:.2f} m/s at an angle of {math.degrees(math.atan2(vyf, vxf)):.2f} degrees")

