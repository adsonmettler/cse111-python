##### A compound list is a list that contains other lists.
# Compound lists are used to store lots of related data.


def main():
    # These are the indexes of each
    # element in the inner lists.
    YEAR_PLANTED_INDEX = 0
    HEIGHT_INDEX = 1
    GIRTH_INDEX = 2
    FRUIT_AMOUNT_INDEX = 3
    # Create a compound list that stores inner lists.
    apple_tree_data = [
        # [year_planted, height, girth, fruit_amount]
        [2012, 2.7, 3.6, 70.5],
        [2012, 2.4, 3.7, 81.3],
        [2015, 2.3, 3.6, 62.7],
        [2016, 2.1, 2.7, 42.1]
    ]
    # Retrieve one inner list from the compound list.
    one_tree = apple_tree_data[2]
    # Retrieve one value from the inner list.
    height = one_tree[HEIGHT_INDEX]
    # Print the tree's height.
    print(f"height: {height}")
# Call main to start this program.
if __name__ == "__main__":
    main()


# Another Example using FOR LOOP to get a data and interacting with that data.
# In this case the function is taking the numbers in th column fruit_amount and
# summing to have the TOTAL AMOUNT.


def main():
    # These are the indexes of each
    # element in the inner lists.
    YEAR_PLANTED_INDEX = 0
    HEIGHT_INDEX = 1
    GIRTH_INDEX = 2
    FRUIT_AMOUNT_INDEX = 3
    # Create a compound list that stores inner lists.
    apple_tree_data = [
        # [year_planted, height, girth, fruit_amount]
        [2012, 2.7, 3.6, 70.5],
        [2012, 2.4, 3.7, 81.3],
        [2015, 2.3, 3.6, 62.7],
        [2016, 2.1, 2.7, 42.1]
    ]
    total_fruit_amount = 0
    # This loop will repeat once for each inner list
    # in the apple_tree_data compound list.
    for inner_list in apple_tree_data:
        # Retrieve the fruit amount from
        # the current inner list.
        fruit_amount = inner_list[FRUIT_AMOUNT_INDEX]
        # Print the fruit amount for the current tree.
        print(fruit_amount)
        # Add the current fruit amount to the total.
        total_fruit_amount += fruit_amount
    # Print the total fruit amount.
    print(f"Total fruit amount: {total_fruit_amount:.1f}")
# Call main to start this program.
if __name__ == "__main__":
    main()