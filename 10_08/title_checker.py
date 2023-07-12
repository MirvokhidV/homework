def is_upperletter(func):
    def wrapper(student, *args, **kwargs):
        name = student.get('name', 'x')
        sure_name = student.get('sure_name', 'x')
        if name.istitle() and sure_name.istitle():
            print()
            func(student, *args, **kwargs)
            print("Both are started with upper letters")
        else:
            print("Error")
    return wrapper


@is_upperletter
def print_student(student):
    print(f"Name: {student['name']}\nSureName: {student['sure_name']}")


students = {}
for i in range(int(input("Students number: "))):
    name = input("Name: ")
    sure_name = input("SureName: ")

    students[name] = {
        "name": name,
        "sure_name": sure_name
    }

while name := input():
    choosen_user = students.get(name, None)
    if choosen_user is None:
        print("Bunday student yo'q")
    else:
        print_student(choosen_user)
