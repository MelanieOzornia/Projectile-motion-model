# projectile motion model

import math

# Constants 
ay = g = 9.81  # acceleration due to gravity (m/s^2)
ax = 0  # horizontal acceleration (m/s^2) (assuming no air resistance)
xi = 0  # initial vertical position (m)
yi = 0  # initial horizontal position (m)

# User Inputs
launchSpeed = float(input("Enter the launch speed (m/s): "))
O = launchAngle = float(input("Enter the launch angle (degrees): "))

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


# summary 
# will include the following calculations:
# 1. Time of flight
# 2. Maximum height
# 3. Horizontal range
# 4. Final velocity

print("\nProjectile Motion Summary:")
print(f"Time of Flight: {totalTime:.2f} seconds")
print(f"Maximum Height: {maxHeight:.2f} meters")
print(f"Horizontal Range: {horizontalRange:.2f} meters")
print(f"Final Velocity: {vf:.2f} m/s at an angle of {math.degrees(math.atan2(vyf, vxf)):.2f} degrees")

