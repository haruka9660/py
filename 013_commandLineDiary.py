import datetime

def write_entry():
    entry = input("Write your entry: ")
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open("diary.txt", "a") as f:
        f.write(f"{timestamp}\n{entry}\n")
    print("Entry saved successfully!")

def read_entries():
    try:
        with open("diary.txt", "r") as f:
            entries = f.read()
        print("Diary entries:")
        print(entries)
    except FileNotFoundError:
        print("No entries found.")

while True:
    print("=== Diary App ===")
    print("1. Write entry")
    print("2. Read entries")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        write_entry()
    elif choice == "2":
        read_entries()
    elif choice == "3":
        print("Exiting...")
        break
    else:
        print("Invalid choice. Please try again.\n")

"""
1 def write_entry():：定义了一个函数 write_entry()，用于用户写入日记条目。
2 entry = input("Write your entry: ")：提示用户输入日记内容，并将其保存到 entry 变量中。
3 timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")：
 获取当前的日期和时间，并使用格式化字符串将其转换为指定格式的时间戳。
4 with open("diary.txt", "a") as f:：
 使用文件操作打开或创建一个名为 "diary.txt" 的文件，并将其附加模式打开
 （如果文件存在，则将新内容追加到文件末尾；如果文件不存在，则创建新文件）。

 
with open("diary.txt", "a") as f: 是一个常用的文件操作语句，在Python中用于打开文件并进行操作。下面是对这行代码的详细解释：
with 关键字是一个上下文管理器，它确保在代码块执行完毕后正确地关闭文件，无论发生任何错误。
open("diary.txt", "a") 是打开文件的函数调用，它接受两个参数：
"diary.txt" 是文件的路径和名称。这里的例子是以当前工作目录为基准，打开名为 "diary.txt" 的文件。你可以根据实际情况修改路径和文件名。
"a" 是文件的模式参数。在这个例子中，使用 "a" 表示以追加模式打开文件。追加模式意味着如果文件存在，新的内容将被追加到文件末尾，而不会覆盖原有内容。如果文件不存在，它将被创建。
as f 是将打开的文件对象赋值给变量 f。通过这个变量，你可以在 with 代码块中对文件进行读取或写入操作。
: 是 Python 中代码块开始的标志。
在 with 代码块中，你可以执行与文件相关的操作，例如读取或写入数据。一旦代码块结束，无论是正常执行还是发生异常，with 语句会自动关闭文件。这样确保了文件资源的正确释放和关闭，无需手动调用 f.close() 方法。
在你提供的代码中，with open("diary.txt", "a") as f: 的作用是以追加模式打开名为 "diary.txt" 的文件，并将文件对象赋值给变量 f。在接下来的代码中，使用变量 f 来写入日记内容。当代码块结束时，文件将自动关闭，确保数据被正确写入并释放文件资源。


5 f.write(f"{timestamp}\n{entry}\n")：将时间戳和用户输入的日记内容写入文件，使用换行符进行分隔。
6 print("Entry saved successfully!")：打印成功保存日记条目的消息。
7 def read_entries():：定义了一个函数 read_entries()，用于读取并显示已保存的日记条目。
8 try:：使用异常处理，以防止文件不存在时出现错误。


try 是 Python 中的异常处理机制。try 语句用于捕获可能引发异常的代码块，并提供相应的处理方式。下面是对 try 语句的详细解释：
try 是一个关键字，用于开始异常处理代码块。
try 语句后面紧跟着一个代码块，包含可能引发异常的代码。
在 try 代码块中，当遇到异常时，解释器会立即跳到 try 语句的下一个部分，即 except 语句块，跳过 try 代码块中异常之后的代码。
如果在 try 代码块中没有发生任何异常，那么 except 语句块将被跳过，程序会继续执行 try 代码块后面的代码。
一个 try 语句可以包含一个或多个 except 语句块，用于处理不同类型的异常。
try 语句可以单独出现，也可以与 except 和 finally 语句联合使用。


9 with open("diary.txt", "r") as f:：使用文件操作打开 "diary.txt" 文件，并以只读模式打开。
10 entries = f.read()：读取文件中的所有内容，并将其保存到 entries 变量中。
11 print("Diary entries:")：打印标题 "Diary entries:"。
12 print(entries)：打印读取到的日记条目内容。
13 except FileNotFoundError:：如果文件不存在，则捕获 FileNotFoundError 异常，并打印找不到日记条目的消息。
14 在主程序中使用循环，打印日记应用的菜单选项。
15 choice = input("Enter your choice: ")：获取用户输入的选项。
16 根据用户的选择执行相应的操作。
17 print("Exiting...")：如果用户选择退出，则打印退出消息，并跳出循环。
18 else:：如果用户选择了无效的选项，则打印无效选择的消息，并开始下一次循环。
这段代码实现了一个简单的命令行日记应用。用户可以选择写入新的日记条目或者读取已保存的日记条目。写入的日记条目会被保存在 "diary.txt" 文件中，并带有时间戳。读取日记条目时，应用会将文件中的内容显示在命令行中。
 
"""