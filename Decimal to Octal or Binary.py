import time

# Display program introduction
print("Program to convert Decimal Number to Binary / Octal Number.\n")
time.sleep(2)  # Pause for 2 seconds to give the user time to read the introduction

initial_input = None

# Prompt the user to enter a decimal number, and handle potential input errors
while initial_input is None:
    try:
        initial_input = int(input("Enter a decimal number: "))
    except ValueError:
        print("Error: Invalid Input!")

# Ask the user which number system they want to convert the decimal to (binary or octal)
convert_to = input("\nWhat number system do you want to convert your decimal? (B/O): ")

# Convert the decimal to binary if the user chose 'B'
if convert_to == "B":
    binary_result = ""
    while initial_input // 2 != 0:
        # Build the binary result digit by digit
        binary_result = str(initial_input % 2) + binary_result
        initial_input = initial_input // 2
    # Add the last binary digit and reverse the result to get the correct order
    binary_result = str(initial_input % 2) + binary_result
    binary_result = binary_result[::-1]
    # Print the binary equivalent
    print(f"\nThe binary equivalent of {initial_input} is: {binary_result}")

# Convert the decimal to octal if the user chose 'O'
elif convert_to == "O":
    octal_result = ""
    while initial_input // 8 != 0:
        # Build the octal result digit by digit
        octal_result = str(initial_input % 8) + octal_result
        initial_input = initial_input // 8
    # Add the last octal digit and reverse the result to get the correct order
    octal_result = str(initial_input % 8) + octal_result
    octal_result = octal_result[::-1]
    # Print the octal equivalent
    print(f"\nThe octal equivalent of {initial_input} is: {octal_result}")

# Handle invalid user input
else:
    print("Error: Invalid Input!")
