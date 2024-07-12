# Author: Adson Mettler do Nascimento

# Prove Milestone: Grocery Store

##################### Exceeding Activity #######################
# Write code to discount the product prices by 10%
# if the current time of day is before 11:00 a.m.

import csv
from datetime import datetime

PRODUCT_NUMBER = 0
PRODUCT_NAME = 1
PRODUCT_PRICE = 2

def main():
    print()
    print("Welcome to Ginger Emporium")
    products_dict = read_dictionary("products.csv", PRODUCT_NUMBER)
    print()
    
    total_quantity = 0 # Initialize the total quantity variable
    subtotal_price = 0

    try:
        with open("request.csv", "rt") as csv_file:
            redear = csv.reader(csv_file)
            next(redear)

            print("Requested Items:")
            for row_list in redear:
                try:
                    product_number = row_list[PRODUCT_NUMBER]
                    product_quantity = int(row_list[1])
                    
                    if product_quantity != 0:
                        product_info = products_dict[product_number]
                        
                        product_name = product_info[PRODUCT_NAME]
                        product_price = float(product_info[PRODUCT_PRICE])

                        ##################### Exceeding Activity #######################
                        # Apply discount to the product price if the current time of day is before 11:00 a.m.
                        discounted_price = apply_discount(product_price)
                                
                        print(f"{product_name}: {product_quantity} @ {discounted_price:.2f}")
                        # Add the product quantity to the total
                        total_quantity += product_quantity
                        sum_price = product_quantity * product_price
                        # Add the sum price to the subtotal
                        subtotal_price += sum_price
                        # Calculate the sale tax of the subtotal price
                        sale_tax = subtotal_price * 0.06
                        # Get the total by adding the sale tax to the subtotal
                        total_price = subtotal_price + sale_tax

                        apply_discount(product_price)


                except KeyError:
                    print()
                    print(f"Error: Product number {product_number} not found in the products list.")
                    print()
            
            print(f"Number of items: {total_quantity}")
            print(f"Subtotal: {subtotal_price:.2f}")
            print(f"Sales tax: {sale_tax:.2f}")
            print(f"Total: {total_price:.2f}")
            print()
            print(f"Thank you for shopping at Ginger Emporium!")
            current_date_and_time = datetime.now()
            print(f"{current_date_and_time:%A %B %d} / {current_date_and_time:%I:%M %p}")
            print()

    except FileNotFoundError:
        print("Error: The file 'request.csv' was not found.")
    except PermissionError:
        print("Error: You do not have permission to read 'request.csv'.")



def read_dictionary(filename, key_column_index):
    """Read the contents of a CSV file into a compound
  dictionary and return the dictionary.
  Parameters
      filename: the name of the CSV file to read.
      key_column_index: the index of the column
          to use as the keys in the dictionary.
  Return: a compound dictionary that contains
      the contents of the CSV file.
  """

    dictionary = {}
    try:   
        with open(filename, "rt") as csv_file:
                
            reader = csv.reader(csv_file)

            next(reader)

            for row_list in reader:
                if len(row_list) != 0:
                    key = row_list[key_column_index]
                    dictionary[key] = row_list

    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
    except PermissionError:
        print(f"Error: You do not have permission to read '{filename}'.")

    return dictionary


##################### Exceeding Activity #######################
# This function will apply 10% of discount whenever the current time of day is before 11:00 a.m.

def apply_discount(product_price):
    current_time = datetime.now().time()
    if current_time < datetime.strptime("11:00", "%H:%M").time():
        product_price *= 0.90
    else:
        product_price *= 1

    return product_price





# Call main to start this program.
if __name__ == "__main__":
    main()