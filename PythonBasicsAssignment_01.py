# Ramzi Jarad
# Python Basics Assignment 01

# Get user input
full_name = input("Enter your full name: ")
mobile_number = input("Enter your mobile number (format: 05x-xxxx-xxx): ")
year_of_birth = int(input("Enter your year of birth: "))

# Calculate user age
current_year = 2023
age = current_year - year_of_birth

# Split mobile number
mobile_number_list = mobile_number.split('-')

# Print user name, age, and mobile number as a list
print("\n\n\t\t\t ## User  info ##")
print(f"User name: {full_name}")
print(f"User current age: {age}")
print(f"Mobile number as a list of strings: {mobile_number_list}")

# waiting for input to close the window
input("\n\n\t\t ==> Press any key to close this Window :) <==")
# Easy ;)
