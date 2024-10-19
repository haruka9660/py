class BankAccount:
    def __init__(self, account_number, account_holder, balance=0):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"成功存入{amount}元。当前余额为{self.balance}元。")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"成功取出{amount}元。当前余额为{self.balance}元。")
        else:
            print("余额不足，取款失败。")

    def display_account_info(self):
        print(f"账号：{self.account_number}")
        print(f"账户名：{self.account_holder}")
        print(f"当前余额：{self.balance}元")


# 创建银行账户对象
account = BankAccount("123456789", "John Doe")

while True:
    print("====== 银行账户管理系统 ======")
    print("1. 存款")
    print("2. 取款")
    print("3. 查询账户")
    print("4. 退出")

    choice = input("请选择操作（输入对应数字）：")

    if choice == "1":
        amount = float(input("请输入存款金额："))
        account.deposit(amount)
    elif choice == "2":
        amount = float(input("请输入取款金额："))
        account.withdraw(amount)
    elif choice == "3":
        account.display_account_info()
    elif choice == "4":
        print("退出程序。")
        break
    else:
        print("无效的选择，请重新输入。")

"""
首先定义了一个名为BankAccount的类，用于表示银行账户对象。
在类的构造函数__init__中，初始化了账户号、账户名和余额属性。余额的默认值为0。
deposit方法用于存款操作。它接受一个amount参数，将存款金额加到余额上，并打印存款成功的消息。
withdraw方法用于取款操作。它接受一个amount参数，首先检查余额是否足够，如果足够，则从余额中减去取款金额，并打印取款成功的消息；否则打印余额不足的消息。
display_account_info方法用于显示账户信息。它打印账户号、账户名和当前余额。

创建一个银行账户对象account，并传入账户号和账户名作为参数。

进入一个无限循环，用于提供菜单选项供用户选择操作。

根据用户的选择，执行相应的操作。
如果选择是"1"，则要求用户输入存款金额，并调用deposit方法进行存款操作。
如果选择是"2"，则要求用户输入取款金额，并调用withdraw方法进行取款操作。
如果选择是"3"，则调用display_account_info方法显示账户信息。
如果选择是"4"，则打印退出程序的消息并跳出循环。
如果选择是其他无效的选项，则打印无效选择的消息。

"""