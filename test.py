import sys

# Using command-line arguments instead of input()
if len(sys.argv) == 3:
    num1 = float(sys.argv[1])
    num2 = float(sys.argv[2])
else:
    # Default values if no arguments provided
    num1 = 10.5
    num2 = 20.3

# Adding the numbers
sum = num1 + num2

# Displaying the result
print("The sum of", num1, "and", num2, "is:", sum)