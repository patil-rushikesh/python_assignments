def getdata():
    marks = []
    print("Enter the marks for 5 subjects:")
    for j in range(5):
        while True:
            try:
                mark = int(input(f"Mark for Subject {j+1}: "))
                if mark < 0 or mark > 100:
                    raise ValueError("Mark must be between 0 and 100.") 
                break  
            except ValueError as e:
                print(e)
                print("Please enter a valid integer between 0 and 100.")
        marks.append(mark)
    return marks

def is_passed(marks):
    for mark in marks:
        if mark <= 40:
            return False
    return True

def collectData(num_students):
    passed_students = []
    for i in range(num_students):
        name = input(f"Enter the name of student {i+1}: ")
        marks = getdata()
        if is_passed(marks):
            passed_students.append(name)
    return passed_students

def copyfile(passed_students):
    with open("passed_students.txt", "w") as file:
        for student in passed_students:
            file.write(student + "\n")
    print("The list of students who passed all subjects has been saved.")

def main():
    num_students = int(input("Enter the number of students: "))
    passed_students = collectData(num_students)
    copyfile(passed_students)

if __name__ == "__main__":
    main()
