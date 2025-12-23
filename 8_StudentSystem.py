class StudentSystem:
    def __init__(self):
        self.students = []

    def add_student(self, student_id, name, marks):
        self.students.append({"id": student_id, "name": name, "marks": marks})

    def search_by_id(self, student_id):
        return next((s for s in self.students if s["id"] == student_id), "Student not found")

    def sort_by_marks(self):
        # Sorts in descending order (highest first)
        return sorted(self.students, key=lambda x: x["marks"], reverse=True)

    def count_fail(self, passing_marks=33):
        return len([s for s in self.students if s["marks"] < passing_marks])

    def find_top_5(self):
        sorted_list = self.sort_by_marks()
        return sorted_list[:5]

# Example Usage:
sys = StudentSystem()
sys.add_student(101, "Alice", 85)
sys.add_student(102, "Bob", 25)
sys.add_student(103, "Charlie", 92)
print(f"Top Student: {sys.find_top_5()[0]['name']}")
print(f"Failed count: {sys.count_fail()}")