import random

# Generate a list of 10 random integers
random_integers = [random.randint(1, 100) for _ in range(10)]

# Create lists for odd and even numbers
odd_list = [num for num in random_integers if num % 2 != 0]
even_list = [num for num in random_integers if num % 2 == 0]

# Display the original list and the odd and even lists
print("Original List:", random_integers)
print("Odd List:", odd_list)
print("Even List:", even_list)
