import random

def guess_number():
    target_number = random.randint(1, 100)  # 生成一个1到100之间的随机整数
    attempts = 0

    while True:
        guess = int(input("请输入你猜测的数字："))
        attempts += 1

        if guess == target_number:
            print("恭喜你，猜对了！")
            print("你猜测了", attempts, "次")
            break
        elif guess < target_number:
            print("猜的数字太小了，请继续尝试。")
        else:
            print("猜的数字太大了，请继续尝试。")

# 调用猜数字函数开始游戏
guess_number()

"""
首先，我们导入了random模块，以便生成随机数。
定义了一个名为guess_number的函数，用于执行猜数字游戏的逻辑。
在函数中，使用random.randint(1, 100)生成一个1到100之间的随机整数，并将其赋值给target_number变量，作为目标数字。
使用attempts变量来记录猜测的次数，初始值为0。
使用while循环创建一个猜数字的游戏循环，直到猜对数字为止。
在循环内部，使用input函数提示用户输入猜测的数字，并使用int()函数将输入的字符串转换为整数类型。
每次猜测后，将猜测次数加1。
使用条件语句判断用户猜测的数字与目标数字的关系，根据不同的情况给出相应的提示。
如果猜对了目标数字，打印出猜对的消息以及猜测的次数，并使用break语句跳出循环。
如果猜测的数字不正确，继续循环，提示用户继续尝试。
在主程序中，调用guess_number函数开始猜数字游戏。

"""