# 导入urllib库
from urllib import request
from urllib import parse

# urllib爬取某网站首页的步骤：

# (1) 定义一个url  即目标地址
url = 'http://httpbin.org/get'

# (2) 模拟浏览器向服务器发送请求
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 "
                  "Safari/537.36 Edg/126.0.0.0"}
req = request.Request(url=url, headers=headers)
res = request.urlopen(req)

# (3) 获取响应中的页面的源码
# 这里read()函数可以获取响应，但是响应的格式是二进制的，需要解码
# 解码：decode('编码格式')  编码格式在 <head><meta chaset ></head>中显示
content = res.read().decode('utf-8')
url = res.geturl()
code = res.getcode()

# (4) 打印数据
# print(content)
print(url)
print(code)
