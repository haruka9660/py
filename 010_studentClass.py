class Student:
    def __init__(self, name, major):
        self.name = name
        self.major = major
        self.courses = []

    def enroll(self, course):
        if course.capacity > 0:
            self.courses.append(course)
            course.students.append(self)
            course.capacity -= 1
            print(f"{self.name}成功选修课程：{course.title}")
        else:
            print(f"选课失败：{course.title}的容量已满。")

    def drop(self, course):
        if course in self.courses:
            self.courses.remove(course)
            course.students.remove(self)
            course.capacity += 1
            print(f"{self.name}成功退选课程：{course.title}")
        else:
            print(f"退选失败：{self.name}未选修过课程：{course.title}")

class Course:
    def __init__(self, title, capacity):
        self.title = title
        self.capacity = capacity
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def remove_student(self, student):
        self.students.remove(student)

    def get_enrolled_students(self):
        return self.students

    def get_available_seats(self):
        return self.capacity

# 创建学生对象
student1 = Student("张三", "计算机科学")
student2 = Student("李四", "经济学")

# 创建课程对象
course1 = Course("数据结构", 30)
course2 = Course("微观经济学", 40)

# 学生选课
student1.enroll(course1)
student2.enroll(course1)
student2.enroll(course2)
student1.enroll(course2)

# 查看课程的选修学生和可用座位
enrolled_students = course1.get_enrolled_students()
available_seats = course1.get_available_seats()

print(f"{course1.title}的选修学生：")
for student in enrolled_students:
    print(f"{student.name} ({student.major})")

print(f"{course1.title}的可用座位：{available_seats}")

"""
创建了Student类，表示学生对象。构造函数接收学生姓名和专业作为参数，创建一个空的课程列表。
Student类定义了enroll()方法，用于将学生选修课程。如果课程的容量未满，将学生添加到课程的学生列表中，并将课程的容量减一。如果课程已满，打印选课失败的消息。
Student类还定义了drop()方法，用于学生退选课程。从学生的课程列表中移除课程，并将学生从课程的学生列表中移除。同时，将课程的容量加一。
创建了Course类，表示课程对象。构造函数接收课程名称和容量作为参数，创建一个空的学生列表。
Course类定义了add_student()方法，用于将学生添加到课程的学生列表中。
Course类还定义了remove_student()方法，用于从课程的学生列表中移除学生。
Course类定义了get_enrolled_students()方法，返回选修该课程的学生列表。
Course类定义了get_available_seats()方法，返回课程的可用座位数。
创建了学生对象student1和student2，以及课程对象course1和course2。
学生通过调用enroll()方法选修课程，并打印相应的消息。
使用get_enrolled_students()方法和get_available_seats()方法查看课程的选修学生和可用座位数，并打印相应的信息。

"""