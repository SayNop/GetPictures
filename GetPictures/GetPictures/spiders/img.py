import scrapy


class ImgSpider(scrapy.Spider):
    name = 'img'
    allowed_domains = ['duotoo.com']
    start_urls = ['http://duotoo.com/']

    def parse(self, response):
        pass
