# Author: Adson Mettler do Nascimento

# Learning to create and call functions with Python for CSE 111 classes.

from datetime import datetime

# Function to print current date and time
def print_time(task_name):
    print(task_name)
    print(datetime.now())
    print()

# print timestamps to see how long sections of code
# take to run

first_name = 'Adson'
print_time('Printed fisrt name')

for x in range(0,10):
    print(x)
print_time('Completed for loop')
