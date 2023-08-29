# Taking input from the user
input_string = input("Enter a string: ")

# Initializing an empty dictionary to store character frequencies
char_frequency = {}

# Counting the frequency of each character
for char in input_string:
    if char in char_frequency:
        char_frequency[char] += 1
    else:
        char_frequency[char] = 1

# Displaying the result
print("Character frequency:", char_frequency)


# The user is prompted to enter a string.
# An empty dictionary char_frequency is initialized to store the frequencies of characters.
# A loop iterates through each character in the input string. If the character is already in the dictionary, its count is incremented. Otherwise, a new entry is added with a count of 1.
# Finally, the program displays the dictionary containing the frequency of each character.
