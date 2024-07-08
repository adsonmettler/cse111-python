# Author: Adson Mettler do Nascimento

###### Python program that reads the contents of provinces.txt into a list and then modifies it. ########

def main():
    text_list = read_list("provinces.txt")
    print()
    print(text_list)
    print()
    print(len(text_list))
    print()
    # Remove the first element from the list.
    text_list.pop(0)
    print()
    print(text_list)
    print()
    # Remove the last element from the list.
    text_list.pop()
    print()
    print(text_list)
    print()
    print(len(text_list))
    print()
    
    old_string = "AB"
    new_string = "Alberta"
    for i in range(len(text_list)):
        if text_list[i] == old_string:
            text_list[i] = new_string

    length_alberta = text_list.count("Alberta")
    print(f'Alberta occurs {length_alberta} times in the modified list.')
    print()



def read_list(filename):

    text_list = []

    with open(filename, "rt") as text_file:

        for row_list in text_file:
            clean_line = row_list.strip()
            text_list.append(clean_line)
    return text_list

# Call main to start this program.
if __name__ == "__main__":
    main()