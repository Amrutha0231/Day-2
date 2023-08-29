def count_vowels(input_string):
    vowels = "aeiouAEIOU"  # List of vowels in both lowercase and uppercase
    vowel_count = 0
    
    for char in input_string:
        if char in vowels:
            vowel_count += 1
    
    return vowel_count

# Taking input
user_input = input("Enter a string: ")

# Counting the number of vowels
vowel_count = count_vowels(user_input)

# Displaying the result
print("Number of vowels:", vowel_count)

