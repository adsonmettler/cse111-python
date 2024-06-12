# Author: Adson Mettler do Nascimento

"""
A manufacturing company needs a program that will help its employees pack manufactured
items into boxes for shipping. Write a Python program named boxes.py that asks the user
for two integers:

    1. the number of manufactured items
    2. the number of items that the user will pack per box

Your program must compute and print the number of boxes necessary to hold the items.
This must be a whole number. Note that the last box may be packed with fewer items than
the other boxes.
"""

number_items = int(input("Enter the number of items: "))
items_per_box = int(input("Enter the number of items per box: "))

import math

number_boxes = math.ceil(number_items / items_per_box)
print()

print(f"For {number_items}, packing {items_per_box} items in each box, you will need {number_boxes} boxes.")
print()

