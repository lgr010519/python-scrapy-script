# urllib下载文件的操作
import urllib.request

# (1) 下载网页
url_page = 'http://www.baidu.com'
# 使用urillib.request.urlretrieve() 函数，
# 传参分别是url(网页的地址路径)、filename(网页文件的名字)
urllib.request.urlretrieve(url_page, 'baidu.html')

# (2) 下载图片
# url_img = 'https://xxx'
# urllib.request.urlretrieve(url_img, 'xxx.jpg')

# (3) 下载视频
# url_video = 'https://xxx'
# urllib.request.urlretrieve(url_video, 'xxx.mov')
