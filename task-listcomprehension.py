# Taking input from the user
input_numbers = input("Enter numbers separated by spaces: ").split()

# Converting input strings to integers
numbers = [int(num) for num in input_numbers]

# Generating a new list of even numbers using list comprehension
even_numbers = [num for num in numbers if num % 2 == 0]

# Displaying the result
print("Even numbers:", even_numbers)


