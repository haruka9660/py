# 定义一个空的TODO列表
todo_list = []

while True:
    print("====== TODO列表 ======")
    print("1. 添加任务")
    print("2. 查看任务")
    print("3. 完成任务")
    print("4. 退出")

    choice = input("请选择操作（输入对应数字）：")

    if choice == "1":
        task = input("请输入任务：")
        todo_list.append(task)
        print("任务已添加。")

    elif choice == "2": 
        if len(todo_list) == 0:
            print("TODO列表为空。")
        else:
            print("当前任务列表：")
            for index, task in enumerate(todo_list, start=1):
                print(f"{index}. {task}")

    elif choice == "3":
        if len(todo_list) == 0:
            print("TODO列表为空。")
        else:
            task_index = int(input("请输入要完成的任务编号："))
            if task_index < 1 or task_index > len(todo_list):
                print("无效的任务编号。")
            else:
                completed_task = todo_list.pop(task_index - 1)
                print(f"任务'{completed_task}'已完成。")

    elif choice == "4":
        print("退出程序。")
        break

    else:
        print("无效的选择，请重新输入。")

"""
1 定义一个空的TODO列表，用于存储任务。
2 使用while True创建一个无限循环，以便用户可以不断执行操作。
3 打印菜单选项，提示用户可用的操作。
4 使用input函数获取用户输入的选择。
5 根据用户的选择执行相应的操作。
  如果选择是"1"，则提示用户输入任务，并将任务添加到TODO列表中。
  如果选择是"2"，则检查TODO列表是否为空，如果不为空，则遍历TODO列表并打印出每个任务。
  如果选择是"3"，则检查TODO列表是否为空，如果不为空，则要求用户输入要完成的任务编号，并将该任务从TODO列表中删除。
  如果选择是"4"，则打印退出消息，并使用break语句跳出循环。
  如果选择无效，则提示用户重新输入。
6 循环回到步骤3，等待用户下一次操作。


当解释for index, task in enumerate(todo_list, start=1):这行代码时，我们需要了解enumerate()函数的功能以及for循环的用法。
enumerate()函数是一个内置函数，用于同时获取序列（如列表、字符串等）中元素的索引和值。它将返回一个可迭代的枚举对象，每个元素都是一个包含索引和对应值的元组。
具体解释如下：
1 todo_list是一个包含任务的列表，例如：["任务1", "任务2", "任务3"]。
2 enumerate()函数的语法结构是enumerate(iterable, start=0)，其中iterable是一个可迭代对象，start是可选参数，表示起始索引的值，默认为0。
3 在这个for循环中，我们使用enumerate(todo_list, start=1)来枚举todo_list列表中的每个任务。
4 index和task是for循环中的两个变量，index表示任务的索引，task表示任务的值。
5 enumerate(todo_list, start=1)将返回一个可迭代的枚举对象，每个元素都是一个包含索引和对应值的元组。
6 在循环的每次迭代中，将使用当前迭代的元组解包，并将索引赋值给index，将任务的值赋值给task。
7 循环将遍历todo_list列表中的每个任务，并执行相应的操作。
例如，如果todo_list的值是["任务1", "任务2", "任务3"]，则for循环将依次迭代以下内容：
第一次迭代：index为1，task为"任务1"
第二次迭代：index为2，task为"任务2"
第三次迭代：index为3，task为"任务3"
通过这种方式，我们可以在循环中同时访问任务的索引和值，方便进行处理和打印输出。


当解释completed_task = todo_list.pop(task_index - 1)这行代码时，我们需要了解pop()方法的功能和列表的索引。
pop()方法是列表对象的一个方法，用于从列表中移除指定索引位置的元素，并返回被移除的元素。
具体解释如下：
1 todo_list是一个包含任务的列表，例如：["任务1", "任务2", "任务3"]。
2 task_index是要完成的任务的索引，它是一个整数。
3 在这个表达式中，task_index - 1表示从任务索引中减去1，以适应列表的索引，因为列表的索引是从0开始的。
4 pop()方法被调用，参数传入task_index - 1，它将移除todo_list列表中指定索引位置的任务，并返回被移除的任务。
5 completed_task变量被赋值为被移除的任务，即完成的任务。
例如，如果todo_list的值是["任务1", "任务2", "任务3"]，而task_index的值是2，那么completed_task的值将是"任务2"，同时，todo_list列表将变为["任务1", "任务3"]，因为任务"任务2"被从列表中移除了。
通过这种方式，我们可以从列表中移除指定索引位置的元素，并将其用于后续的处理或输出。
"""