def fibonacci(n):
    fib_sequence = [0, 1]  # 斐波那契数列的前两个数字
    for i in range(2, n):
        fib_sequence.append(fib_sequence[i-1] + fib_sequence[i-2])  # 添加下一个斐波那契数到数列中
    return fib_sequence

n = 10  # 要计算斐波那契数列的前n个数字
fib_nums = fibonacci(n)  # 调用fibonacci函数计算斐波那契数列
for num in fib_nums:
    print(num)  # 打印每个斐波那契数

"""
1 定义了一个名为fibonacci的函数,它接受一个参数n,表示要计算斐波那契数列的前n个数字。
2 创建一个列表fib_sequence,初始包含斐波那契数列的前两个数字:0和1。
3 使用for循环遍历从2到n-1的范围(不包括n),依次计算并添加下一个斐波那契数到fib_sequence列表中。新的斐波那契数是前两个斐波那契数之和，通过索引i-1和i-2来访问。
4 循环结束后,返回完整的斐波那契数列fib_sequence。
5 在主程序中,将变量n设置为10,表示要计算斐波那契数列的前10个数字。
6 调用fibonacci函数,传入参数n,得到斐波那契数列,将结果赋值给变量fib_nums。
7 使用for循环遍历fib_nums中的每个斐波那契数,将每个数打印出来。
"""