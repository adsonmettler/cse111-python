# Author: Adson Mettler do Nascimento

# This program is dedicated for practice of using methods to change objects with Python


def main():
  # Create and print a list named fruit.
  fruit_list = ["pear", "banana", "apple", "mango"]
  print()
  print(f"original: {fruit_list}")

  fruit_list.reverse()
  print(f"reversed: {fruit_list}")
  
  fruit_list.append("orange")
  print(f"append orange: {fruit_list}")

  i = fruit_list.index("apple")
  fruit_list.insert(i, "cherry")
  print(f"insert cherry: {fruit_list}")
  
  fruit_list.remove("banana")
  print(f"remove banana: {fruit_list}")

  last = fruit_list.pop()
  print(f"pop {last}: {fruit_list}")

  fruit_list.sort(key=None, reverse=False)
  print(f"sorted: {fruit_list}")

  fruit_list.clear()
  print(f"cleared: {fruit_list}")


if __name__ == "__main__":
    main()