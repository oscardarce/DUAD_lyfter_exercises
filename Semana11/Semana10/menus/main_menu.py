from actions.add_student_info import add_student_info
from actions.show_students_list import show_students_list
from actions.top_three_average_grade import top_three_average_grade
from actions.students_average_grade import students_average_grade
from data.export_csv import create_csv
from data.import_csv import read_csv

from utils.utils import validate_bd


def main_menu(selection, students_db):

    while True:
        try:
            if selection == 1:
                add_student_info(students_db)

            elif selection == 2 and students_db:
                show_students_list(students_db)

            elif selection == 3 and students_db:
                top_three_average_grade(students_db)

            elif selection == 4 and students_db:
                students_average_grade(students_db)

            elif selection == 5 and students_db:
                create_csv(students_db)

            elif selection == 6:
                read_csv(students_db)

            else:
                validate_bd(students_db)

        except ValueError as error:
            print(error)

        return
