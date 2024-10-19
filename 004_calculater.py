def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b != 0:
        return a / b
    else:
        return "错误：除数不能为零"

# 用户输入运算符和操作数
operator = input("请输入运算符（+、-、*、/）：")
num1 = float(input("请输入第一个操作数："))
num2 = float(input("请输入第二个操作数："))

# 根据运算符进行相应的计算
if operator == "+":
    result = add(num1, num2)
elif operator == "-":
    result = subtract(num1, num2)
elif operator == "*":
    result = multiply(num1, num2)
elif operator == "/":
    result = divide(num1, num2)
else:
    result = "错误：无效的运算符"

# 打印结果
print("计算结果:", result)


"""
1 定义了四个函数：add、subtract、multiply和divide，分别用于执行加法、减法、乘法和除法运算。
2 在主程序中，使用input函数让用户输入运算符，并将输入的结果保存在operator变量中。
3 使用float函数将用户输入的操作数转换为浮点数，并将第一个操作数保存在num1变量中，第二个操作数保存在num2变量中。
4 根据用户输入的运算符进行相应的计算。使用if-elif-else条件语句来判断运算符，并调用相应的函数执行对应的运算。
5 将计算结果保存在result变量中。
6 使用print函数打印出计算结果。

"""