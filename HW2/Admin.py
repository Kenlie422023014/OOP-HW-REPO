class Admin:
    def __init__(self, admin_id, name):
        self.admin_id = admin_id
        self.name = name

    def input_announcement(self, announcement):
        self.announcement = announcement
        print(f"New Announcement: {self.announcement}")
        pass

    def input_student_count(self, student_count):
        self.student_count = student_count
        print(f"Total number of students: {self.student_count}")
        pass
