import scrapy
from selenium import webdriver
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.common.by import By
import time


class SeleniumSpiderSpider(scrapy.Spider):
    name = "selenium_spider"
    # allowed_domains = ["www.xxx.com"]
    start_urls = ["https://juejin.cn"]

    # service = EdgeService(executable_path='edgedriver/msedgedriver.exe')

    driver = webdriver.Edge()

    def parse(self, response):
        # print(response)
        self.driver.get('https://bing.com')

        element = self.driver.find_element(By.ID, 'sb_form_q')
        element.send_keys('WebDriver')
        element.submit()
        time.sleep(5)
        self.driver.quit()
