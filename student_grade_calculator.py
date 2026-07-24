def student_info():
    
    while True:
        name = input("Enter student full name: ").upper()
        if len(name) >= 5:
            break
        else:
            print("Please enter valid name that contains atleast 5 charaters")

    while True:
        try:
            clas = int(input("Enter class: "))
            if 1 <= clas <= 10:
                break
            else:
                print("Class must be between 1 and 10.")
        except ValueError:
            print("Please enter the class number in digits only.")

    rollnum = input("Enter roll number: ")

    return name,clas,rollnum


def student_marks():

    subjects_list = ["ENGLISH","MATHEMATICS","SCIENCE","SOCIAL","HINDI","TELUGU"]

    subjects = {}

   
    for subject in subjects_list:
        while True:
            try:
                marks = int(input(f"Enter the marks for {subject}: "))
                if 0 <= marks <= 100:
                    subjects[subject] = marks
                    break
                else:
                    print("Marks must be between 0 and 100.")
            except ValueError:
                print("Please enter marks in number only.")
       
    return subjects


def calculate_result(subjects):

    total = sum(subjects.values())
    max_marks = len(subjects)*100
    percentage = (total/max_marks) * 100

    if percentage >= 90:
        grade = "A+"
    elif percentage >= 80:
        grade = "A"
    elif percentage >= 70:
        grade = "B"
    elif percentage >= 60:
        grade = "C"
    elif percentage >= 50:
        grade = "D"
    elif percentage >= 40:
        grade = "E"
    else:
        grade = "F"
    
    status ="PASS 🎉" if percentage >= 40 else "FAIL ❌"

    return total,max_marks,percentage,grade,status


def display_result(name,clas,rollnum,subjects,total,max_marks,grade,status,percentage):
    print("\n================================")
    print("  🎓    STUDENT  RESULTS    🎓  ")
    print("=================================")
    print("Name   :",name)
    print("Class   :",clas)
    print("Roll No :",rollnum)
    print("=========Marks Summary==========")

    for key,val in subjects.items():
        print(f"{key} : {val}")
    
    print("----------------------------------")
    print(f"Total    : {total} / {max_marks}")
    print(f"Percentage : {(total/max_marks)*100}%")
    print(f"Grade : {grade}")
    print(f"Status : {status}")
    print("==============================")

    if percentage >= 40:
        print(f"Congratulations {name}! 🎉")
    else:
        print(f"Keep trying {name}! 💪")


def gradecalculator():
    print("🙏 Welcome to Student Grade Result System!\n")

    name,clas,rollnum = student_info()
    subjects = student_marks()

    total,max_marks,percentage,grade,status = calculate_result(subjects)
    display_result(name,clas,rollnum,subjects,total,max_marks,grade,status,percentage)

gradecalculator()