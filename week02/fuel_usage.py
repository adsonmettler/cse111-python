# Author: Adson Mettler do Nascimento

# Program to calculate fuel efficiency of a vehicle

import math
# Main function
def main():
    start_point = float(input('Enter the starting odometer value in miles: '))
    end_point = float(input('Enter the ending odometer value in miles: '))
    gallons = float(input('Enter the amount of fuel in gallons: '))
    print()

    mpg = miles_per_gallon(start_point, end_point, gallons)
    lp100k = lp100k_from_mpg(mpg)

    print('The effiency of your vehucle is:')
    print(f'{mpg:.1f} miles per gallon')
    print(f'{lp100k:.2f} liters per 100 kilometers')
    print()

# Function to calculate miles per gallon
def miles_per_gallon(start_point, end_point, gallons):
    mpg = abs(end_point - start_point) / gallons
    return mpg

# Function to convert miles per gallon to liters per 100 kilometers
def lp100k_from_mpg(mpg):
    lp100k = 235.215 / mpg
    return lp100k

main()
print()