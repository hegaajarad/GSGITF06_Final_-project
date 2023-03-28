# Ramzi Jarad
# Python Basics Assignment 04
# Find The Max Mark and Average



total_marks = int(input("Enter the total number of marks: "))

marks = []
for i in range(total_marks):
    mark = int(input(f"Enter mark {i+1}: "))
    marks.append(mark)


max_mark = max(marks)
average_mark = sum(marks) / len(marks)

print("The maximum mark is:", max_mark)
print("The average mark is:", average_mark)