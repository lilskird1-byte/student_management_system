print("My First Student Management System using Python")
print()

students={}
def save_students():
    with open("students.txt","w") as file:
        for student_id, details in students.items():
            file.write(f"{student_id},{details['name']},{details['age']},{details['program']},{details['gpa']}\n")
    
            
def load_students():
    try:
        with open("students.txt","r")as file:

            for line in file:
                student_id, name, age, program, gpa = line.strip().split(",")

                students[student_id]={
                "name":name,
                "age":int(age),
                "program":program,
                "gpa":float(gpa)
                }
    except FileNotFoundError:
        pass
load_students()

    
while True:
    print("====MENU====")
    print("1.Add Student")
    print("2.View Students")
    print("3.Search Student")
    print("4.Edit Student")
    print("5.Delete Student")
    print("6.Total Students")
    print("7.GPA Records")
    print("8.Exit")

    option=int(input("Select Option :"))
    print()

    if option==1:
        print("====Add Students====")
        student_id=(input("Enter Student ID :"))
        name=input("Enter Student Name :")
        age=int(input("Enter Students Age :"))
        program=input("Enter Students Program :")
        gpa=float(input("Enter Student's GPA :"))
        students[student_id]= {
            "name":name,
            "age":age,
            "program":program,
            "gpa":float(gpa)
        }
        save_students()
        print("Student added successfully!")
        print()
    elif option==2:
        print("====Students Records====")

        if len(students)==0:
            print("No students in records.")
        else:
            for student_id, details in sorted(students.items(), key=lambda x:x[1]["name"]):
                print("Student ID:",student_id)
                print("Name:",students[student_id]["name"])
                print("Age:",students[student_id]["age"])
                print("Program:",students[student_id]["program"])
                print("GPA:",students[student_id]["gpa"])
                print()
    elif option==3:
        while True:
            print("====Search Student====")
            print("1.By Student ID")
            print("2.By Program")
            print("3.Exit Search")
            choice=int(input("Select your choice :"))
            print()
            if choice==1:
                search_id=input("Enter Student's ID :")
                print()
                if search_id in students:
                    print("===Search Results===")
                    print("Student ID:",search_id)
                    print("Name:",students[search_id]["name"])
                    print("Age:",students[search_id]["age"])
                    print("Program:",students[search_id]["program"])
                    print("GPA:",students[search_id]["gpa"])
                    print()
                else:
                    print("ID not found!")
            elif choice==2:
                program=input("Enter Student Program :")
                found= False

                for student_id,details in students.items():
                        if details["program"]==program:
                            print(program)
                            print(f"Name :{details["name"]}")
                            print()

                            found=True

                if not found:
                    print("Program not found!")
                
                    
            elif choice==3:
                print()
                break
    elif option==4:
        print("====Edit Student====")
        while True:
            print("1.Edit Student Name")
            print("2.Edit Student Age")
            print("3.Edit Student Program")
            print("4.Quit Editting")

            choice=int(input("Enter Your Choice :"))
            if choice==1:
                print("===Edit Student Name===")
                student_id=input("Enter Student's ID :")
                print()
                if student_id in students:
                    print("Student found!")
                    new_name=input("Enter New Name :")
                    students[student_id]["name"]=new_name
                    print("Name edited successfully!")
                    print()
            elif choice==2:
                print("===Edit Student Age===")
                student_id=input("Enter Student's ID :")
                print()
                if student_id in students:
                    print("===Student found===")
                    new_age=input("Enter New Age :")
                    students[student_id]["age"]=new_age
                    print("Age updated successfully!")
                    print()
            elif choice==3:
                print("===Edit Program===")
                student_id=input("Enter Student's ID :")
                print()
                if student_id in students:
                    print("Student found")
                    new_program=input("Enter New Program :")
                    students[student_id]["program"]=new_program
                    print("Program updated successfully!")
                    print()
            else:
                choice==4
                print("Updates Done!")
                save_students()
                print()
                break
    elif option==5:
        print("====Delete Student====")
        delete_id=input("Enter Students ID :")
        if delete_id in students:
            del(students[delete_id])
            save_students()
            print("Student deleted successfully!")
        else:
            print("No student found.")
            save_students()
    elif option==6:
        print(f"Total Students:{len(students)}")
    elif option==7:
        print("====GPA Records====")
        while True:
            print("1.Students GPA")
            print("2.Highest GPA")
            print("3.Lowest GPA")
            print("4.Leave Section")

            option= int(input("Choose your option :"))
            print()

            if option==1:
                print("====Students GPA====")
                for student_id, details in sorted(students.items(), key= lambda x:x[1]["gpa"]):
                    print("Student ID :",student_id)
                    print("Name :",students[student_id]["name"])
                    print("GPA :",students[student_id]["gpa"])
                    print()
            elif option==2:
                print("====Highest GPA====")
                highest_gpa=max(students.items(), key=lambda x:x[1]["gpa"])
                student_id,details =highest_gpa
                print(f"Name :{details["name"]}")
                print(f"GPA :{details["gpa"]}")
                print()
            elif option==3:
                print("====Lowest GPA====")
                lowest_gpa=min(students.items(),key =lambda x:x[1]["gpa"])
                student_id,details =lowest_gpa
                print(f"Name :{details["name"]}")
                print(f"GPA :{details["gpa"]}")
                print()
            elif option==4:
                break

    elif option==8:
        print("Updates Complted")
        break
    else:
        print("Invalid Option!!!")
        
    
        

            
            

























