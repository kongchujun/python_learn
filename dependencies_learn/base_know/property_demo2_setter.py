class Circle:
    def __init__(self, radius):
        self._radius = radius

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, value):
        if value < 0:
            raise ValueError("Radius cannot be negative")
        self._radius = value

# 创建一个圆的实例
circle = Circle(5)
print(circle.radius)  # 输出: 5

# 修改半径
circle.radius = 10
print(circle.radius)  # 输出: 10

# 尝试设置一个负值
circle.radius = -2  # 将引发 ValueError
