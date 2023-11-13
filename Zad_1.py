

class student:
    def __init__ (self, name, marks):
        self.name = name
        self.marks = marks
    
    def is_passed (self):
        average = sum(self.marks) / len(self.marks)
        return average > 50
    
    
student_1 = student("Marek", [50, 50, 60])
student_2 = student("Orzeł", [2, 4, 5])


print(f"{student_1.name}: passed: {student_1.is_passed()}\n")
print ("-" * 50)
print(f"{student_2.name}: passed: {student_2.is_passed()}\n")
