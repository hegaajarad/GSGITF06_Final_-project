# Ramzi Jarad
# Python Basics Assignment 02


# Define the functions
def add(num1=1, num2=1):
    return num1 + num2

def sub(num1=1, num2=1):
    return num1 - num2

def mul(num1=1, num2=1):
    return num1 * num2

def div(num1=1, num2=1):
    return num1 / num2

def power(num1=1, num2=1):
    return num1 ** num2

num1 = 10
num2 = 5
result = 0

# Apply the functions
sum_result = add(num1, num2)
sub_result = sub(num1, num2)
mul_result = mul(num1, num2)
div_result = div(num1, num2)
power_result = power(num1, num2)

FinalResult = sum_result + sub_result + mul_result + div_result + power_result
# Print the results
print("Sum result: ", sum_result)
print("Subtraction result: ", sub_result)
print("Multiplication result: ", mul_result)
print("Division result: ", div_result)
print("Power result: ", power_result)

# Print Final results
print("Final Result: ", int(FinalResult))