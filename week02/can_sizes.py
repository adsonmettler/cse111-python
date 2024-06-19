
# Program to calculate return cylinder volume

import math
import csv

def main():
    name = "#1 Picnic"
    radius = 6.83
    height = 10.16
    volume = compute_volume(radius, height)
    surface_area = compute_surface_area(radius, height)
    storage_eficiency = volume / surface_area
    print(f"{name} {storage_eficiency:.2f}")


def compute_volume(radius, height):
   
    volume = math.pi * (radius**2) * height
    return volume

def compute_surface_area(radius, height):

    surface_area = 2 * math.pi * radius * (radius + height)
    return surface_area

main()


