import scrapy


class ImgSpider(scrapy.Spider):
    name = 'img'
    allowed_domains = ['duotoo.com']
    start_urls = ['https://www.duotoo.com/rentiyishu/']

    def parse(self, response):
        pass
