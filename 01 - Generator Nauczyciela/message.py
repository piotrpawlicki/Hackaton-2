import datetime as dt
import read_data as rd

##otwieranie pliku txt
def open_message_txt():
    with open('message.txt', 'r') as file:
        return file.read()

def create_final_date(n):
    date = dt.datetime.now() + dt.timedelta(days=n)
    return date.strftime("%Y-%m-%d")

def insert_student_data(message, student_name, tasks, grades, potential_grade):
    messages = []
    for name, task, grade, potential in zip(student_name, tasks, grades, potential_grade):
        temp_message = message
        temp_message = temp_message.replace("[insert student name]", name)
        temp_message = temp_message.replace("[insert one date for all students]", create_final_date(7))
        temp_message = temp_message.replace("[insert number of missing tasks]", rd.convert_to_string(task))
        temp_message = temp_message.replace("[insert current grade]", rd.convert_to_string(grade))
        temp_message = temp_message.replace("[insert potential grade]", rd.convert_to_string(potential))
        messages.append(temp_message)
    return messages


def main():
    worksheets = rd.list_od_worksheets()
    students_class = rd.choose_class()
    student_name, tasks, grades, potential_grade = rd.read_class_details(students_class)
    message = open_message_txt()

    message_to_students = insert_student_data(message, student_name, tasks, grades, potential_grade)
    for each in message_to_students:
        print(f'{each} \n\n')

if __name__ == "__main__":
    main()