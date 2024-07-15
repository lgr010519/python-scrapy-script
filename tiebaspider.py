import random
import time
from urllib import request
from urllib import parse


class TiebaSpider:
    def __init__(self):
        # 定义常用变量
        self.url = 'http://tieba.baidu.com/f?kw={}&pn={}'
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                          "Chrome/126.0.0.0 Safari/537.36 Edg/126.0.0.0"}

    def get_html(self, url):
        # 获取相应内容
        req = request.Request(url=url, headers=self.headers)
        res = request.urlopen(req)
        html = res.read().decode()
        return html

    def parse_html(self):
        # 解析提取数据
        pass

    def save_html(self, filename, html):
        # 数据处理
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(html)

    def run(self):
        # 程序入口函数
        name = input('请输入贴吧名称：')
        start = int(input('请输入起始页：'))
        end = int(input('请输入终止页：'))
        params = parse.quote(name)

        for page in range(start, end + 1):
            pn = (page - 1) * 50
            url = self.url.format(params, pn)
            html = self.get_html(url)
            filename = f'{name}_第{page}页.html'
            self.save_html(filename, html)
            print(f'第 {page} 页抓取成功')

            time.sleep(random.randint(1, 2))


if __name__ == '__main__':
    spider = TiebaSpider()
    spider.run()
