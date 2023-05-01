"""Calculates the collatz series of any given Integer."""

# check if number>=1 and if type(number) = int
import numbers


while True:
    try:
        number = int(input("Please enter a positive integer: "))
        if number <= 0:
            raise ValueError("Number must be a positive integer")
        break
    except ValueError:
        if not isinstance(numbers, int):
            print("Invalid input. Please enter an integer.")
        else:
            print("Invalid input. Please enter a positive integer.")

# define logic for collatz serie calculation
def collatz(num):
    """Calculates the collatz series."""
    while num != 1:
        if num % 2 == 0:
            num = num // 2
        elif num % 2 == 1:
            num = 3 * num + 1
        print(str(num))

if number == 1:
    print("collatz sequence done.")

collatz(number) # call function
