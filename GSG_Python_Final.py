# Ramzi Jarad
# Final project - GSG ITF 06 - Class 01 with Muhannad Alkrunz

class Course:
    next_id = 1
    def __init__(self, name, level):
        self.id = Course.next_id
        Course.next_id += 1
        self.name = str(name)
        self.level = str(level).upper()

    def __str__(self):
        return f"{self.name} ({self.level})"


class Student:
    next_id = 1

    def __init__(self, name, level):
        self.id = Student.next_id
        Student.next_id += 1
        self.name = str(name)
        self.level = str(level).upper()
        self.courses = []

    def add_course(self, course):
        if course.level != self.level:
            raise ValueError("Cannot add course with different level")
        self.courses.append(course)

    def remove_course(self, course):
        self.courses.remove(course)

    def update_details(self, name, level):
        self.name = name
        self.level = level.upper()

    def get_details(self):
        course_names = ", ".join(str(c) for c in self.courses)
        return f"ID: {self.id}\nName: {self.name}\nLevel: {self.level}\nCourses: {course_names}"


class School:
    def __init__(self):
        self.students = []
        self.courses = []

    def add_student(self, name, level):
        student = Student(name, level)
        self.students.append(student)
        print(f"Student '{student.name}' saved successfully.")

    def remove_student(self, id):
        for student in self.students:
            if student.id == id:
                self.students.remove(student)
                print(f"Student with ID {id} deleted successfully.")
                return
        print("Student not found.")

    def edit_student(self, id):
        for student in self.students:
            if student.id == id:
                name = input("\n\t [+] Enter new name: ")
                level = input("\n\t [+] Select new level (A-B-C): ").upper()
                student.update_details(name, level)
                print("Student updated successfully.")
                return
        print("Student not found.")

    def display_students(self):
        print("\n\t ### Student List ###.")
        for student in self.students:
            print(student.get_details())
            print("-" * 4)

    def add_course(self, name, level):
        course = Course(name, level)
        self.courses.append(course)
        print(f"Course '{course.name}' saved successfully.")

    def add_course_to_student(self, student_id, course_id):
        student = None
        for s in self.students:
            if s.id == student_id:
                student = s
                break

        if not student:
            print("Student not found.")
            return

        course = None
        for c in self.courses:
            if c.id == course_id:
                course = c
                break

        if not course:
            print("Course not found.")
            return

        try:
            student.add_course(course)
            print(f"Course '{course.name}' added to student '{student.name}' successfully.")
        except ValueError as e:
            print(str(e))


school = School()

while True:
    print("\n\t ### Welcome to School Management System ### ")
    print("1. Add new student")
    print("2. Remove student")
    print("3. Edit student")
    print("4. Display all students")
    print("5. Create new course")
    print("6. Add course to student")
    print("7. Exit")

    choice = input("\n\t [+] Enter your choice: ")

    if choice == "1":
        name = input("\n\t [+] Enter student name: ")
        while True:
            level = input("\n\t [+] Select student level (A-B-C): ").upper()
            if level in ["A", "B", "C"]:
                break
            else:
                print("Invalid level. Please select A, B, or C.")
        school.add_student(name, level)

    elif choice == "2":
        id = int(input("\n\t [+] Enter student ID: "))
        school.remove_student(id)

    elif choice == "3":
        id = int(input("\n\t [+] Enter student ID: "))
        school.edit_student(id)

    elif choice == "4":
        school.display_students()

    elif choice == "5":
        name = input("\n\t [+] Enter course name: ")
        while True:
            level = input("Select course level (A-B-C): ").upper()
            if level in ["A", "B", "C"]:
                break
            else:
                print("Invalid level. Please select A, B, or C.")
        school.add_course(name, level)

    elif choice == "6":
        student_id = int(input("\n\t [+] Enter student ID: "))
        course_id = int(input("\n\t [+] Enter course ID: "))
        school.add_course_to_student(student_id, course_id)

    elif choice == "7":
        print("\t\t######### Goodbye! #########")
        break

    else:
        print("\t\t######### Invalid choice. Please try again. #########")
