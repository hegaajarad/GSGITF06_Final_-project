# Ramzi Jarad
# Python Basics Assignment 05
# Find The Max Mark and Average N ask for students Numbers N Marks numbers

num_students = int(input("[+] Enter the total number of students: "))
num_marks = int(input("[+] Enter the total number of marks: "))


averages = [] # Array for every student average
maxMarks = [] # array for every student Max Mark

# Loop through each student
for i in range(num_students):
    total = 0
    # Loop through each mark for this student
    marks = []
    for j in range(num_marks):
        mark = int(input(f"[+] Enter mark {j+1} for student {i+1}: "))
        total += mark
        marks.append(mark)
    # Calculate the average for this student and append it to the list of averages N append Max Mark
    average = total / num_marks
    averages.append(average)
    maxMarks.append(int(max(marks)))

    # print(f"Average for student {i+1}: {average}")

# print every student Max Mark and average
for stud in range(num_students):
    print(f"[I] Sudent Number {stud+1} his max mark = {maxMarks[stud]} and his avrage = {averages[stud]}")

# Find the maximum and minimum averages
max_avg = max(averages)
min_avg = min(averages)

print("\n\n","--"*20)
print("[I] Maximum Mark is :", max(maxMarks))
print("[I] Maximum average :", max_avg)
print("[I] Minimum average :", min_avg)

