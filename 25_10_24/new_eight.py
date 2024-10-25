students = {}

for i in range(2):
    print(f"\nEnter details for Student {i + 1}:")
    name = input("Enter student name: ")
    
    while name in students:
        print("Sorry please enter another name ")
        name = input("Enter student name: ")
    marks = {
        "English": int(input("Enter marks in English: ")),
        "Physics": int(input("Enter marks in Physics: ")),
        "Chemistry": int(input("Enter marks in Chemistry: ")),
        "Maths": int(input("Enter marks in Maths: ")),
        "Hindi": int(input("Enter marks in Hindi: ")),
    }

    totalmarks=sum(marks.values())
    result=totalmarks/5
    students[name] = {"Marks":marks,"Result":result}


print("\nStudent Data in Ascending Order:")
for student, data in sorted(students.items(), key=lambda x: x[1]["Result"]):
    print(f"{student}: Average Result = {data['Result']:.2f}")

# print(students)
