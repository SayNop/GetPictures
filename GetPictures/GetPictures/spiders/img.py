import scrapy


class ImgSpider(scrapy.Spider):
    name = 'img'
    allowed_domains = ['duotoo.com']
    start_urls = ['https://www.duotoo.com/rentiyishu/']

    def parse(self, response):
        # //*[@id="imgList"]/ul/li[1]
        page_urls = response.xpath('//*[@id="imgList"]/ul/li/a/@href').extract()
        for page_url in page_urls:
            print(response.urljoin(page_url))

