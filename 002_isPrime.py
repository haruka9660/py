def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

start = 1  # 范围起始值
end = 20  # 范围结束值

print(f"质数范围 {start} 到 {end}:")
for num in range(start, end + 1):
    if is_prime(num):
        print(num)

"""

1 定义了一个名为is_prime的函数，它接受一个参数num，用于判断该数字是否为质数。
2 如果num小于等于1，直接返回False，因为质数定义为大于1的自然数。
3 使用for循环遍历从2到num的平方根的整数部分加1的范围。这是因为如果存在num的因子大于其平方根，那么一定存在一个小于平方根的因子，所以只需要遍历到平方根即可。
4 在循环中，如果num能够被当前的循环变量i整除，则说明num不是质数，返回False。
5 如果循环结束后没有找到num的因子，那么它是质数，返回True。
6 在主程序中，将变量start设置为1，表示质数范围的起始值。
7 将变量end设置为20，表示质数范围的结束值。
8 打印出质数范围的标题。
9 使用for循环遍历从start到end（包括end）的范围中的每个数字。
10 对于每个数字，调用is_prime函数来检查它是否为质数。
11 如果是质数，则打印出该数字。

"""