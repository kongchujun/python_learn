# 类方法 (@classmethod)：操作类属性或需要类对象（而非实例）的方法。
# 静态方法 (@staticmethod)：不需要类或实例参与的方法，就像是普通函数，只是为了组织的方便放在类里。
# 实例方法：需要访问或操作实例属性的常规方法
class Vehicle:
    def __init__(self, category, wheels):
        self.category = category
        self.wheels = wheels

    @classmethod
    def motorcycle(cls):
        return cls('motorcycle', 2)

    @classmethod
    def car(cls):
        return cls('car', 4)

    @classmethod
    def truck(cls):
        return cls('truck', 6)

# 使用类方法创建不同类型的车辆
bike = Vehicle.motorcycle()
sedan = Vehicle.car()
big_truck = Vehicle.truck()

print(bike.category, bike.wheels)  # 输出: motorcycle 2
print(sedan.category, sedan.wheels)  # 输出: car 4
print(big_truck.category, big_truck.wheels)  # 输出: truck 6
