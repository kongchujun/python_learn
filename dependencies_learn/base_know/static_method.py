class MathUtility:
    @staticmethod
    def is_even(num):
        """Return True if the number is even, otherwise False."""
        return num % 2 == 0

# 使用静态方法，无需创建类的实例
print(MathUtility.is_even(4))  # 输出: True
print(MathUtility.is_even(5))  # 输出: False

