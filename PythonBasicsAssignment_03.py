# Ramzi Jarad
# Python Basics Assignment 03
# Find The Max Number


numbers = []
for i in range(3):
    num = int(input(f"Enter a Number {i+1}: "))
    numbers.append(num)

# here I'll use max fun to get Max Number
max_num = max(numbers)
print("[+] Using max fun ==> The maximum Number is:", max_num)

# here I'll use if statment to get Max Number
max_num = numbers[0]
for num in numbers:
    if num > max_num:
        max_num = num

print("[+] Using if statment ==> The maximum number is:", max_num)