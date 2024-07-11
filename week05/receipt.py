# Author: Adson Mettler do Nascimento

# Prove Milestone: Grocery Store

import csv

PRODUCT_NUMBER = 0
PRODUCT_NAME = 1
PRODUCT_PRICE = 2

def main():
    print()
    print("All Products:")
    products_dict = read_dictionary("products.csv", PRODUCT_NUMBER)
    print(products_dict)
    print()
    
    with open("request.csv", "rt") as csv_file:
        redear = csv.reader(csv_file)
        next(redear)

        print("Requested Items:")
        for row_list in redear:
            product_number = row_list[PRODUCT_NUMBER]
            product_quantity = int(row_list[1])
            
            if product_quantity != 0:
                product_info = products_dict.get(product_number, None)
                
                if product_info:
                    product_name = product_info[PRODUCT_NAME]
                    product_price = float(product_info[PRODUCT_PRICE])
                        
                    print(f"{product_name}: {product_quantity} @ {product_price}")



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
        
    with open(filename, "rt") as csv_file:
            
        reader = csv.reader(csv_file)

        next(reader)

        for row_list in reader:
            if len(row_list) != 0:
                key = row_list[key_column_index]
                dictionary[key] = row_list

    return dictionary

# Call main to start this program.
if __name__ == "__main__":
    main()