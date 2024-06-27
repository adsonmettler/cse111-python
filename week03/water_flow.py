# Author: Adson Mettler do Nascimento

# Water flow program to support an engineer design a water distribution system.

import math

def water_column_height(tower_height, tank_height):
    t = tower_height
    w = tank_height
    h = t + ((3 * w) / 4)
    return h

def pressure_gain_from_water_height(height):
    density = 998.2  # density of water in kg/m^3
    gravity = 9.80665  # acceleration due to gravity in m/s^2
    pressure_gain = (density * gravity * height) / 1000
    return pressure_gain

def pressure_loss_from_pipe(pipe_diameter, pipe_length, friction_factor, fluid_velocity):
    density = 998.2  # density of water in kg/m^3
    lost_pressure = -(friction_factor * pipe_length * density * (fluid_velocity**2)) / (2000 * pipe_diameter)
    return lost_pressure

