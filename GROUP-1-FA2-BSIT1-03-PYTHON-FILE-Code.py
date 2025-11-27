import random

List_of_Courses = {     "BSA"       : [],
                        "BSHM"      : [],
                        "BSTM"      : [],
                        "BSBA"      : [],
                        "BSMA"      : [],
                        "BEED"      : [],
                        "BSED"      : [],
                        "BCHED"     : [],
                        "BSCRIM"    : [],
                        "BSARCH"    : [],
                        "BSCPE"     : [],
                        "BSCE"      : [],
                        "BSEE"      : [],
                        "BSME"      : [],
                        "BSN"       : [],
                        "BSPHARMA"  : [],
                        "BSMEDTECH" : [],
                        "BSPSYCH"   : [],
                        "BSIT"      : [] }

List_of_Instructors = { "BSA"       : ["blue","red"],
                        "BSHM"      : ["white","yellow"],
                        "BSTM"      : ["green","grey"],
                        "BSBA"      : ["cyan","green"],
                        "BSMA"      : ["brown","burgundy"],
                        "BEED"      : ["orange","beige"],
                        "BSED"      : ["maroon","indigo","magenta","beige","gold"],
                        "BCHED"     : ["cyan","red","violet"],
                        "BSCRIM"    : ["yellow","green"],
                        "BSARCH"    : ["blue","magenta"],
                        "BSCPE"     : ["maroon","indigo"],
                        "BSCE"      : ["cyan","white"],
                        "BSEE"      : ["black","burgundy"],
                        "BSME"      : ["pink","gold"],
                        "BSN"       : ["beige","grey"],
                        "BSPHARMA"  : ["orange","brown"],
                        "BSMEDTECH" : ["green","red"],
                        "BSPSYCH"   : ["magenta","blue"],
                        "BSIT"      : ["blue","green"] }

Admin_Data = {          "Acera"     : ["Gil"],
                        "Casona"    : ["Mike"],
                        "Moncano"   : ["Rob"],
                        "Rosal"     : ["Jeremy"],
                        "Masinger"  : ["Jhomadyane"] }                     

Student_Accounts         = {}
Registered_Students_Data = {}
Approved_Students_Data   = {}

def create_account():
    print("\n        **Create Student Account** \n")
    Create_User = input("Create Username: ")

    if Create_User in Student_Accounts:
        print("\n>>>>> Username already Exist\n")
        return

    Create_Pass  = input("Create Password: ")
    Full_name    = input("Enter Full Name: ")
    Email        = input("Enter Email: ")
    Phone_Number = input("Enter Phone Number: ")
    
    Student_Accounts[Create_User] = [Create_Pass, Full_name, Email, Phone_Number]
    print("\n---------------- Account Created Successfully ----------------")

def student_login():
    print("\n        **Student Login** \n")
    Student_User = input("Username: ")
    Student_Pass = input("Password: ")

    if Student_User not in Student_Accounts:
        print("\n>>>>> Username not found\n")
        return

    if Student_Accounts[Student_User][0] != Student_Pass:
        print("\n>>>>> Incorrect Password\n")
        return

    Student_Name = Student_Accounts[Student_User][1]
    Email        = Student_Accounts[Student_User][2]
    Phone_Number = Student_Accounts[Student_User][3]

    student_page(Student_Name, Email, Phone_Number)

def student_page(Student_Name, Email, Phone_Number):
    while True:
        print("\n        **Student Page** \n")
        student_Choice = input("Register    [1]\nView Status [2]\nLogout      [Any Key]\nEnter ===> : ")

        if student_Choice   == "1":
            choose_course(Student_Name, Email, Phone_Number)
        elif student_Choice == "2":
            print("==========================================")
            print("\n        **Registration Status ** \n")
            
            nakaSubmit = False
            for course in Registered_Students_Data:
                for student in Registered_Students_Data[course]:
                    if student["Name"] == Student_Name:
                        print("Course: ", student["Course"])
                        print("Status: ", student["Status"])
                        nakaSubmit = True
            if not nakaSubmit:      
                print("\n>>>>> No registration Found\n")
        else:
            print("\n---------------- Logged Out Successfully ----------------\n")
            break

def choose_course(Student_Name, Email, Phone_Number):
    while True:
        Chosen_Course = input("Course: ").upper()

        if Chosen_Course in List_of_Courses:
            return submit_information(Student_Name, Chosen_Course, Email, Phone_Number)
        else:
            print("\n>>>>> Course not found\n")

def submit_information(Student_Name, Chosen_Course, Email, Phone_Number):
    Instructor = random.choice(List_of_Instructors.get(Chosen_Course))

    print("==========================================")
    print("\n        **Student Information**           \n")
    print("Name         :", Student_Name)
    print("Year Level   :","First Year")
    print("Course       :", Chosen_Course)
    print("Instructor   :", Instructor)
    print("Email        :", Email)
    print("Phone Number :", Phone_Number)
    print("\n==========================================\n")

    submit_Choice = input("\nSubmit [1]\nCancel [Any Key]\nEnter ===> : ")

    if submit_Choice == '1':
        if Chosen_Course not in Registered_Students_Data:
            Registered_Students_Data[Chosen_Course] = []

        Registered_Students_Data[Chosen_Course].append({
            "Name"         : Student_Name,
            "Course"       : Chosen_Course,
            "Instructor"   : Instructor,
            "Email"        : Email,
            "Phone Number" : Phone_Number,
            "Status"       : "Pending"
        })
        print("\n---------------- Submitted Successfully ----------------\n")
    else:
        print("\n---------------- Entry Canceled ----------------\n")

def admin_page():
    while True:
        admin_Choice = input("\n        **Admin Page** \n\nView and Approve [1]\nLogout Admin     [Any Key]\nEnter ===> : ")

        if admin_Choice == "1":
            if not Registered_Students_Data:
                print("\n>>>>> No registered Students to Approve\n")
            else:
                approve_submitted_info()    
        else:
            print ("\n---------------- Logged Out Successfully ----------------\n")
            break

def approve_submitted_info():
    for Course, Students in Registered_Students_Data.items():
        for Student in Students:
            name         = Student["Name"]
            course_info  = Student["Course"]
            instructor   = Student["Instructor"]
            email        = Student["Email"]
            phone_number = Student["Phone Number"]
            status       = Student["Status"]

            print("==========================================")
            print("\n        **Approval Page** \n")
            print("Name         :", name)
            print("Course       :", course_info)
            print("Instructor   :", instructor)
            print("Email        :", email)
            print("Phone Number :", phone_number)
            print("Status       :", status)

            if status == "Pending":
                Approve_Choice = input("\nApprove student?\n\nApprove [1]\nReject  [Any Key]:\nEnter ===> : ")

                if Approve_Choice == '1':
                    Student["Status"] = "Approved"
                    if Course not in Approved_Students_Data:
                        Approved_Students_Data[Course] = []

                    Approved_Students_Data[Course].append(Student)
                    print("\n---------------- Approved ----------------\n")
                else:
                    Student["Status"] = "Rejected"
                    print("\n---------------- Rejected ----------------\n")

def main_page():
    while True:
        print("\nStudent Enlistment System\n")
        main_Choice = input("Create Account [1]\nStudent Login  [2]\nAdmin Page     [3]\nExit           [Any Key]\nEnter ===> : ")

        if   main_Choice == '1':
            create_account()
        elif main_Choice == '2':      
            student_login()
        elif main_Choice == '3':
            Admin_User = input("Username: ")
            Admin_Pass = input("Password: ")

            if Admin_User in Admin_Data and Admin_Data[Admin_User][0] == Admin_Pass:
                admin_page()
            else:
                print("\nUsername or Password not found\n")
        else:
                print ("\n---------------- Exit Successfully ----------------\n")
                break

if __name__ == "__main__":
    main_page()
