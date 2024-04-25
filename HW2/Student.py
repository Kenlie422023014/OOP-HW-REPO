class Student:
    def __init__(self, student_id, name):
        self.student_id = student_id
        self.name = name

    def view_announcements(self, announcements):
        for announcement in announcements:
            print(announcement)

    def view_grades(self, grades):
        print("Grades:")
        for course, grade in grades.items():
            print(f"{course}: {grade}")

    def view_student_count(self, student_count):
        print(f"Total number of students: {student_count}")


