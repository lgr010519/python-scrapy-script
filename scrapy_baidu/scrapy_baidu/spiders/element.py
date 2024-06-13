import scrapy


class ElementSpider(scrapy.Spider):
    name = "element"
    allowed_domains = ["element-plus.org"]
    start_urls = ["https://element-plus.org/zh-CN/component/overview.html"]

    def parse(self, response):
        ele_list = response.xpath('/html/body/div[1]/div/main/div/div/div[1]/div/div/div[2]/div[1]/div/div/div/span/text()')
        print('=====================================')
        for ele in ele_list:
            print(ele.extract())
