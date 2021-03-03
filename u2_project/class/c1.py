
class Person:
    def normal_method():  # 禁止使用，；
        print('normal')

    def method(self):  # 普通方法；
        print(self)

    @classmethod   # 类方法
    def class_method(cls):
        print('class method', cls, hex(id(cls)), hex(id(Person)))

    @staticmethod    # 静态方法
    def static_method():
        print('static method')

print('-' * 120)
Person.method(Person())
Person().method()

print('-' * 120)
Person().class_method()
Person.class_method()

print('-' * 120)
Person.static_method()
Person().static_method()
