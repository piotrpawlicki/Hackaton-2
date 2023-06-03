import openpyxl as xl
import pandas as pd

def read_class_details(choosen_sheet):
    try:
        data = pd.read_excel('lista uczniow.xlsx', sheet_name=choosen_sheet)
        student_name = data['Name'] + ' ' + data['Surname']
        tasks = data['Tasks']
        grades = data['Grades']
        potential_grade = [grade + 1 for grade in grades]
        return student_name, tasks, grades,  potential_grade

    except FileNotFoundError:
        print("Plik nie został znaleziony.")
        return None, None, None, None
    except Exception as e:
        print("Wystąpił błąd podczas wczytywania pliku:", str(e))
        return None, None, None, None


def list_od_worksheets():
    try:
        workbook = xl.load_workbook('lista uczniow.xlsx')
        worksheets = workbook.sheetnames
        return worksheets
    except FileNotFoundError:
        print("Plik nie został znaleziony.")
        return None
    except Exception as e:
        print("Wystąpił błąd podczas wczytywania pliku:", str(e))
        return None

def choose_class():
    worksheets = list_od_worksheets()
    print("Wybierz klasę: ")
    for i in range(len(worksheets)):
        print(str(i+1) + ". " + worksheets[i])
    choosen_sheet = int(input())
    return worksheets[choosen_sheet-1]

def convert_to_string(list_of_numbers):
    if isinstance(list_of_numbers, int):  # Sprawdzenie, czy to pojedyncza liczba
        return str(list_of_numbers)
    else:  # Jeśli to lista liczb
        return [str(number) for number in list_of_numbers]


# worksheets = list_od_worksheets()
# students_class = choose_class()
# student_name, tasks, grades = read_class_details(students_class)
#
# print(student_name)
# print(tasks)
# print(grades)
# print(tasks)