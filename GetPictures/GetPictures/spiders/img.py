import re
import scrapy


class ImgSpider(scrapy.Spider):
    name = 'img'
    allowed_domains = ['duotoo.com']
    start_urls = ['https://www.duotoo.com/rentiyishu/']

    def parse(self, response):
        # //*[@id="imgList"]/ul/li[1]
        page_urls = response.xpath('//*[@id="imgList"]/ul/li/a/@href').extract()
        for page_url in page_urls:
            page_url = response.urljoin(page_url)
            print(page_url)
            yield scrapy.Request(page_url, callback=self.img_parse, dont_filter=True)

    def img_parse(self, response):
        # /html/body/div[3]/div[2]/article/section[1]/div[1]/h1
        title = response.xpath('//div[@class="ArticleH1"]//h1/text()').extract_first()
        title = re.sub('\d+/\d+', '', title).strip()
        print(title)