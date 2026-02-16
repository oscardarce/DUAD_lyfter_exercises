class Student:
    def __init__(self, student_name, student_section_class, spanish_grade, english_grade, history_grade, science_grade):
        self.student_name = student_name
        self.student_section_class = student_section_class
        self.spanish_grade = spanish_grade
        self.english_grade = english_grade
        self.history_grade = history_grade
        self.science_grade = science_grade

    def __str__(self):
        return f"{self.student_name} - {self.student_section_class} -Calificaciones: Español: {self.spanish_grade}, Inglés: {self.english_grade}, Historia: {self.history_grade}, Ciencias: {self.science_grade}"
