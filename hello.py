# print('hello')
# print('''
#     aaa
#     sss
#     ddd
# ''')
# a = input('请输入：')
# print(isinstance(a, str))

# s1 = '123456789'
# print(s1[::-1])
# s2 = 'aaa'
# print(s1 and s2)
#
# if s1 != s2:
#     print(111)
#
# match s1:
#     case 1:
#         print(111)
#     case _:
#         print(000)
#
# while True:
#     print(111)range(10)

# for i in range(11):
#     print(1111111)

# list1 = [1, 2, 3, 4, 5]
# for i, j in enumerate(list):
#     print(i, j)

# for i in range(len(list)):
#     print(i)

# print(list(range(10)))
#
#
# def f(a, b):
#     return a ** b
#
#
# a = f(4, 2)
# print(a)

# fn = lambda a, b: a + b
#
# print(fn(8, 8))

# import turtle
#
# pen = turtle.Turtle()
# pen.forward(10)
# input()

class User(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age


user = User('aaa', 18)
print(user.__dict__)
