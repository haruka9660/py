class Gun:

    def __init__(self, model):

        # 1.枪的型号
        self.model = model

        # 2. 子弹的数量
        self.bullet_count = 0

    def add_bullet(self, count):

        self.bullet_count += count

    def shoot(self):

        # 1.判断子弹的数量
        if self.bullet_count <= 0:
            print("[%s] 咩有子弹了..." % self.model)

            return
        
        # 2.发射子弹，-1
        self.bullet_count -= 1

        # 3.提示发射信息
        print("[%s] 突突突... 还有[%s]发子弹" % (self.model, self.bullet_count))

class Soldier:

    def __init__(self, name):

        self.name = name
        self.gun = None

    def fire(self):

        # 1.判断士兵是否有枪
        if self.gun is None:
            print("[%s] 还没有枪" % self.name)

        # 2.高喊口号
        print("冲啊...[%s]" % self.name)

        # 3.让枪装填子弹
        self.gun.add_bullet(50)

        # 4.让枪发射子弹
        self.gun.shoot()

# 1.创建枪对象
ak47 = Gun("AK47")

xusanduo = Soldier("许三多")

# 一个对象作为另一个对象的属性
xusanduo.gun = ak47

xusanduo.fire()