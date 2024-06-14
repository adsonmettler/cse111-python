# Author: Adson Mettler do Nascimento
# Date: 2024-06-13

"""
Problem Statement

You work for a retail store that wants to increase sales on
Tuesday and Wednesday, which are the store’s slowest sales days.
On Tuesday and Wednesday, if a customer’s subtotal is $50 or
greater, the store will discount the customer’s subtotal by 10%.

Core Requirements

    1. Your program asks the user for the subtotal but does not ask the user for the
    day of the week. Your program gets the day of the week from your computer’s
    operating system.

    2. Your program correctly computes and prints the discount amount if applicable.

    3. Your program correctly computes and prints the sales tax amount and the total
    amount due.
"""

# Import the datetime class from the datetime
# module so that it can be used in this program.
from datetime import datetime
# Call the now() method to get the current
# date and time as a datetime object from
# the computer's operating system.
current_date_and_time = datetime.now()
# Call the weekday() method to get the day of the
# week from the current_date_and_time object.
day_of_week = current_date_and_time.weekday()
# Print the day of the week for the user to see.


subtotal = float(input("Please enter the subtotal: "))
tax_amount = subtotal * 0.06
total = subtotal + tax_amount
discount = subtotal * 0.1
day_of_week = 1


if day_of_week == 1 and day_of_week == 2:
    print(f"Discount amount: {discount:.2f}")
    print(f"Sales tax amount: {tax_amount:.2f}")
    print(f"Total: {total:.2f}")

else:
    print(f"Sales tax amount: {tax_amount:.2f}")
    print(f"Total: {total:.2f}")


