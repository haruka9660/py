students = []

class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

    def display_info(self):
        print(f"姓名：{self.name}")
        print(f"年龄：{self.age}")
        print(f"年级：{self.grade}")

def add_student():
    name = input("请输入学生姓名：")
    age = int(input("请输入学生年龄："))
    grade = input("请输入学生年级：")

    student = Student(name, age, grade)
    students.append(student)
    print("学生已添加。")

def display_students():
    if len(students) == 0:
        print("学生列表为空。")
    else:
        for index, student in enumerate(students, start=1):
            print(f"学生编号：{index}")
            student.display_info()
            print()

while True:
    print("====== 学生管理系统 ======")
    print("1. 添加学生")
    print("2. 查看学生")
    print("3. 退出")

    choice = input("请选择操作（输入对应数字）：")

    if choice == "1":
        add_student()
    elif choice == "2":
        display_students()
    elif choice == "3":
        print("退出程序。")
        break
    else:
        print("无效的选择，请重新输入。")


"""
定义了一个空的students列表，用于存储学生对象。
定义了一个Student类，用于表示学生对象。类中包含了初始化方法__init__()和显示信息方法display_info()。
__init__()方法接收学生的姓名、年龄和年级作为参数，并将其存储为对象的属性。
display_info()方法用于打印学生的信息。
定义了add_student()函数，用于添加学生信息。在函数中，使用input()函数获取学生的姓名、年龄和年级，并创建一个Student对象，然后将其添加到students列表中。
定义了display_students()函数，用于显示学生列表。如果学生列表为空，则打印相应的提示信息；否则，使用enumerate()函数遍历students列表中的每个学生对象，并打印出学生的编号和信息。
使用while True创建一个无限循环，以便用户可以不断执行操作。
打印学生管理系统的菜单选项。
使用input()函数获取用户的选择。
根据用户的选择执行相应的操作：添加学生、查看学生或退出。
如果选择的操作需要输入信息，程序会相应地要求用户提供输入。
执行操作后，程序会返回到菜单选项，并等待用户下一次操作。

"""