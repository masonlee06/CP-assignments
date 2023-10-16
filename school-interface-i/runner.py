from classes.school import School 

school = School('Ridgemont High') 

# print(school.name)
# print(school.students)
# print(school.staff)


while True:
    choice = input(print("\nWhat would you like to do?\nOptions:\n1. List All Students\n2. View Individual Student <student_id>\n3. Add a Student\n4. Remove a Student <student_id>\n5. Quit\nEnter:"))
    if choice == '5':
        print('Goodbye!')
        break
    elif choice == '2':
        student_id = input('Enter student id: ')
    if choice == '1':
        school.list_students()