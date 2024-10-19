def check_even_odd(num):
    if num % 2 == 0:
        return "偶数"
    else:
        return "奇数"

# 用户输入一个数字
user_input = input("请输入一个数字：")
number = int(user_input)

# 调用函数检查奇偶性
result = check_even_odd(number)

# 打印结果
print(f"{number} 是一个 {result}。")

"""
1 定义了一个名为check_even_odd的函数，它接受一个参数num，用于判断该数字的奇偶性。
2 使用取模运算符%将num除以2，如果余数为0，则说明它是偶数，返回字符串"偶数"；否则返回字符串"奇数"。
3 在主程序中，使用input函数让用户输入一个数字，并将输入的结果保存在user_input变量中。
4 使用int函数将user_input转换为整数类型，并将结果保存在number变量中。
5 调用check_even_odd函数，传入参数number，以检查该数字的奇偶性，并将结果保存在result变量中。
6 使用print函数打印出结果，显示用户输入的数字以及它是奇数还是偶数。

"""