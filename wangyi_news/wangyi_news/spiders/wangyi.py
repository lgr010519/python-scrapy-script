import scrapy


class WangyiSpider(scrapy.Spider):
    name = "wangyi"
    # allowed_domains = ["news.163.com"]
    start_urls = ["https://news.163.com"]

    model_urls = []

    def parse(self, response):
        li_list = response.xpath('//*[@id="index2016_wrap"]/div[3]/div[2]/div[2]/div[2]/div/ul/li')
        indexs = [2, 3, 6, 7]

        for index in indexs:
            model_li = li_list[index]
            li = model_li.xpath('./a/@href').extract_first()
            self.model_urls.append(li)

        for url in self.model_urls:
            yield scrapy.Request(url=url, callback=self.parse_model)

    def parse_model(self, response):
        print(response)
