from traits.api import HasTraits, Int, Str, on_trait_change

class Employee(HasTraits):
    name = Str()
    age = Int()

    @on_trait_change('name,age')
    def update(self, object, name, old, new):
        print(f"{name} changed from {old} to {new}")

# 使用示例
emp = Employee(name="John", age=30)
emp.name = "Doe"  # 输出: name changed from John to Doe
emp.age = 31       # 输出: age changed from 30 to 31
