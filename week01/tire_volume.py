# Author: Adson Mettler do Nascimento
# Date: 2024-06-14

##### TIRE VOLUME #####

"""
The volume of space inside a tire can be approximated with this formula:

v = (π w2 a (w a + 2,540 d)) / 10,000,000,000

    v is the volume in liters,
    π is the constant PI, which is the ratio of the circumference of a circle divided by its diameter (use math.pi),
    w is the width of the tire in millimeters,
    a is the aspect ratio of the tire, and
    d is the diameter of the wheel in inches.

"""

import math

def calculation_tire_volume(w, a, d):

    volume = (math.pi * w**2 * a * (w * a + 2540 * d)) / 10000000000
    return volume


w = int(input("Enter the width of the tire in mm (ex 205): "))
a = int(input("Enter the aspect ratio of the tire (ex 60): "))
d = int(input("Enter the diameter of the wheel in inches (ex 15): "))
print()
volume = calculation_tire_volume(w, a, d)
print(f"The approximate volume is {volume:.2f} liters")
print()



from datetime import datetime
current_date_and_time = datetime.now()

with open("volume.txt", "at") as volume_file:
    print(f"{current_date_and_time:%Y-%m-%d}, {w}, {a}, {d}, {volume:.2f}", file=volume_file)

call_to_action = input("Do you want to buy tires with this dimensions (yes or no)? ")

if call_to_action.lower() == "yes":
    print("Ok, we will get in touch with you.")
    user_name = input("Please, provide your full name: ")
    phone_number = input("And your phone number (ex 999 333 1234): ")
    with open("volume.txt", "at") as volume_file:
        print(f"User name: {user_name.title()}", file=volume_file)
        print(f"{user_name.title()}'s phone number: {phone_number}", file=volume_file)

elif call_to_action.lower() == "no":
    print("Ok, have a good day!")
    print()

