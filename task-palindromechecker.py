# Taking input from the user
user_input = input("Enter a word: ")

# Reversing the input word
reversed_word = ""
for char in user_input:
    reversed_word = char + reversed_word

# Checking if the input word is a palindrome
if user_input == reversed_word:
    print("It's a palindrome!")
else:
    print("It's not a palindrome.")
