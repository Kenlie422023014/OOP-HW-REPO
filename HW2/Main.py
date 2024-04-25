from Student import Student
from Professor import Professor
from Operator import Operator
from Admin import Admin

def login(role):
    if role == "student":
        student_id = input("Enter Student ID: ")
        name = input("Enter Name: ")
        student = Student(student_id=student_id, name=name)
        student.data = [  # Data array untuk mahasiswa
        {"NIM": "12345", "Name": "Kenlie", "Major": "Computer Science"},
        {"NIM": "67890", "Name": "Vete", "Major": "Engineering"} ]
        return Student(student_id=student_id, name=name)
    elif role == "professor":
        professor_id = input("Enter Professor ID: ")
        name = input("Enter Name: ")
        professor = Professor(professor_id=professor_id, name=name)
        professor.data = [  # Data array untuk dosen
        {"NIP": "123", "Name": "Prof. Rusdi", "Course": "Computer Science"},
        {"NIP": "456", "Name": "Prof. Faiz", "Course": "Engineering"}]
        return Professor(professor_id=professor_id, name=name)
    elif role == "operator":
        operator_id = input("Enter Operator ID: ")
        name = input("Enter Name: ")
        return Operator(operator_id=operator_id, name=name)
    elif role == "admin":
        admin_id = input("Enter Admin ID: ")
        name = input("Enter Name: ")
        return Admin(admin_id=admin_id, name=name)
    else:
        print("Invalid role!")
        return None

def main():
    role = input("Login as (student/professor/admin/operator): ")
    user = login(role)
    if user:
        print(f"Welcome, {user.name}!")

        if role == "student":
            # Opsi yang diimplementasikan untuk siswa
            ips = 3.5
            ipk = 3.6
            attendance_count = 80  # Total kehadiran untuk semester

            option = input("Choose an option (ips/ipk/attendance): ")
            if option == "ips":
                print(f"IPS: {ips}")
            elif option == "ipk":
                print(f"IPK: {ipk}")
            elif option == "attendance":
                print(f"Total attendance: {attendance_count}")
            else:
                print("Invalid option!")

        elif role == "professor":
            professor = Professor(user.professor_id, user.name)
            option = input("Choose an option (input_grades/input_attendance): ")
            if option == "input_grades":
                student_id = input("Enter Student ID: ")
                course = input("Enter Course: ")
                grade = input("Enter Grade: ")
                professor.input_grades(student_id, course, grade)
            elif option == "input_attendance":
                student_id = input("Enter Student ID: ")
                course = input("Enter Course: ")
                date = input("Enter Date (YYYY-MM-DD): ")
                professor.input_attendance(student_id, course, date)
            else:
                print("Invalid option!")


        elif role == "operator":
            # Opsi yang diimplementasikan untuk operator
            print("Options for operator are not implemented yet.")
            operator = Operator(user.operator_id, user.name)
            # Implementasi fungsionalitas operator bisa ditambahkan di sini

        elif role == "admin":
            # Opsi yang diimplementasikan untuk admin
            print("Options for admin are not implemented yet.")
            admin = Admin(user.admin_id, user.name)
            # Implementasi fungsionalitas admin bisa ditambahkan di sini

if __name__ == "__main__":
    main()
