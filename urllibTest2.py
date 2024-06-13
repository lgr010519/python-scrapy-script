# HTTPResponse这个类型
# 六个方法：read、readline、readlines、getcode、geturl、getheaders
# print(type(response)) # response是HTTPResponse的类型
from urllibTest1 import response

# (1) 按照一个字节一个字节去读
# content = response.read()
# print(content)

# 读取具体的n个字节，在read()函数中传参即可
# content2 = response.read(5)
# print(content2)

# (2) 按行读取，但是只能读取一行
# content3 = response.readline()
# print(content3)

# (3) 按行读取，并且读取所有行
# content4 = response.readlines()
# print(content4)

# (4) 返回状态码的方法：200状态码没有问题，其他的状态码可能有问题
print(response.getcode())

# (5) 返回访问的目标的url地址
print(response.geturl())

# (6) 获取的是响应头
print(response.getheaders())
