students = {
    "Peter": 75,
    "John": 88,
    "Ram": 45,
    "Sita": 92,
    "Alex": 61
}


def view_all_students(students):
    if not students:
        print("No students record found.")
        return
    for x,y in students.items():
        print(f"{x}: {y}")

def search_student(students):
    student=input("Enter the student name: ")
    
    if student in students:
        print(f"{student} marks: {students[student]}")
    else:
        print(f"{student} not found")
        
def add_all_students(students):
    name=input("Enter your name: ")
    marks=int(input("Enter your marks: "))
    students[name]=marks
    print("Students added successfully!")
    
def update_students(students):
    name=input("Enter your name: ")
    updated_marks= int(input("Enter your updated marks: "))
    
    if name in students:
        students[name]=updated_marks
        print(f"The {name} is updated successfully.")
    else:
        print("No student found.")
        
def delete_student(students):
    name=input("Enter your name: ")
    if name in students:
        students.pop(name)
        print(f"{name} deleted successfully.")
    else:
        print(f"No student with {name} found.")

def average_marks(students):
    total=0
    for x in students.values():
        total +=x
    avg= total/len(students)
    print(f"Average marks: {avg}")

def highest_scorer(students):
    top_student=list(students.items())[0][0]
    marks=list(students.items())[0][1]
    
    for i,j in students.items():
        if j>marks:
            marks=j
            top_student=i
    print(f"Highest scorer: {top_student}")
    print(f"Marks: {marks}")
    
while True:
    print("\n==== STUDENT MANAGEMENT ====")
    print("1. View All Students")
    print("2. Search Student")
    print("3. Add Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Average Marks")
    print("7. Highest Scorer")
    print("8. Exit")
    
    choice = input("Enter your choice (1-8): ")
    
    if choice == "1":
        view_all_students(students)
    elif choice == "2":
        search_student(students)
    elif choice == "3":
        add_all_students(students)
    elif choice == "4":
        update_students(students)
    elif choice == "5":
        delete_student(students)
    elif choice == "6":
        average_marks(students)
    elif choice == "7":
        highest_scorer(students)
    elif choice == "8":
        print("Thank you for using Student Management System!")
        break  # Exit the loop
    else:
        print("Invalid choice! Please select a number from 1 to 8.")
    

        
        
