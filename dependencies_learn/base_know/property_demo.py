# Python 中的 @property 装饰器允许你将类的方法转化为属性，这样可以在不改变类接口的情况下增加方法的功能。
# 使用 @property 可以使得对方法的访问看起来像是对属性的访问，这有助于实现数据的封装和保护

class Circle:
    def __init__(self, radius):
        self._radius = radius

    @property
    def radius(self):
        """Get the radius of the circle."""
        return self._radius

    @property
    def area(self):
        """Calculate and return the area of the circle."""
        return 3.14159 * (self._radius ** 2)

# 创建一个圆的实例
circle = Circle(5)

# 访问属性
print(circle.radius)  # 输出: 5
print(circle.area)    # 输出: 78.53975
