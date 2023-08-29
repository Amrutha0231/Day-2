# Taking input from the user
num = int(input("Enter a number: "))

# Check if the number is less than 2 (not prime)
if num < 2:
    print("It's not a prime number.")
else:
    is_prime = True

    # Check for factors from 2 to the square root of the number
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            is_prime = False
            break

    # Display the result
    if is_prime:
        print("It's a prime number!")
    else:
        print("It's not a prime number.")

