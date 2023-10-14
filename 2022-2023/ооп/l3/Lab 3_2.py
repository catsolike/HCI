class Students:
    name = "Alex"
    group = "13.02.21"
    course = 3
    
    def questionnaire():
        print("Информация о студентах:")


setattr(Students, 'student_ticket', 1298)

student_one = Students()
student_two = Students()

student_two.name = 'Michael'
student_two.student_ticket = 1301


print(Students.name, Students.group, Students.course, Students.student_ticket)
print(student_one.name, student_one.group, student_one.course, student_one.student_ticket)
print(student_two.name, student_two.group, student_two.course, student_two.student_ticket, '\n')

Students.questionnaire()
print('Студент:', student_one.name + '.', 
      'Группа:', student_one.group + '.', 
      'Курс:', str(student_one.course) + '.',
      'Студенческий билет:', str(student_one.student_ticket) + '.')

print('Студент:', student_two.name + '.', 
      'Группа:', student_two.group + '.', 
      'Курс:', str(student_two.course) + '.',
      'Студенческий билет:', str(student_two.student_ticket) + '.')