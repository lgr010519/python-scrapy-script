# 导入urllib库
import urllib.request

# urllib爬取某网站首页的步骤：

# (1) 定义一个url  即目标地址
url = 'http://www.baidu.com'

# (2) 模拟浏览器向服务器发送请求
response = urllib.request.urlopen(url)

# (3) 获取响应中的页面的源码
# 这里read()函数可以获取响应，但是响应的格式是二进制的，需要解码
# 解码：decode('编码格式')  编码格式在 <head><meta chaset ></head>中显示
content = response.read().decode('utf-8')

# (4) 打印数据
# print(content)
